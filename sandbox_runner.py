"""Executa o código do aluno em um processo separado e restrito.

Lê um JSON da entrada padrão: {"code", "function", "tests"}
Escreve um JSON na saída padrão com o resultado de cada teste.

Camadas de proteção (ver README):
1. Análise da AST: bloqueia import, acesso a atributos "__dunder__" e nomes perigosos.
2. Builtins reduzidos: o código só enxerga funções seguras.
3. Processo isolado (python -I) com timeout, definido por quem chama este arquivo.
"""
import ast
import builtins
import contextlib
import io
import json
import sys

try:  # limite de memória (somente Linux/macOS)
    import resource

    resource.setrlimit(resource.RLIMIT_AS, (256 * 1024 * 1024, 256 * 1024 * 1024))
except Exception:
    pass

BLOCKED_NAMES = {
    "eval", "exec", "compile", "open", "input", "__import__", "globals", "locals",
    "vars", "getattr", "setattr", "delattr", "breakpoint", "exit", "quit", "help",
    "memoryview", "type", "object", "super",
}

ALLOWED = (
    "abs", "all", "any", "bool", "dict", "divmod", "enumerate", "filter", "float",
    "int", "isinstance", "len", "list", "map", "max", "min", "pow", "print",
    "range", "reversed", "round", "set", "sorted", "str", "sum", "tuple", "zip",
    "Exception", "ValueError", "TypeError", "__build_class__",
)
SAFE_BUILTINS = {name: getattr(builtins, name) for name in ALLOWED}


def validate(code):
    """Devolve uma mensagem de erro (str) ou None se o código for aceitável."""
    try:
        tree = ast.parse(code)
    except SyntaxError as e:
        return f"Erro de sintaxe na linha {e.lineno}: {e.msg}"

    for node in ast.walk(tree):
        if isinstance(node, (ast.Import, ast.ImportFrom)):
            return "Nesta plataforma não é permitido usar import."
        if isinstance(node, ast.Attribute) and node.attr.startswith("__"):
            return "Acesso a atributos especiais (__nome__) não é permitido."
        if isinstance(node, ast.Name) and node.id in BLOCKED_NAMES:
            return f"O uso de '{node.id}' não é permitido nesta plataforma."
    return None


def main():
    payload = json.load(sys.stdin)
    code, func_name, tests = payload["code"], payload["function"], payload["tests"]

    problem = validate(code)
    if problem:
        print(json.dumps({"ok": False, "error": problem, "results": []}))
        return

    env = {"__builtins__": SAFE_BUILTINS, "__name__": "aluno"}
    captured = io.StringIO()
    try:
        with contextlib.redirect_stdout(captured):
            exec(compile(code, "<aluno>", "exec"), env)
    except Exception as e:
        print(json.dumps({"ok": False, "error": f"{type(e).__name__}: {e}", "results": []}))
        return

    func = env.get(func_name)
    if not callable(func):
        msg = f"Não encontrei a função '{func_name}'. Confira se o nome está exatamente igual ao do enunciado."
        print(json.dumps({"ok": False, "error": msg, "results": []}))
        return

    results = []
    for args, expected in tests:
        item = {"args": args, "expected": expected, "got": None, "passed": False, "error": None}
        try:
            with contextlib.redirect_stdout(captured):
                got = func(*args)
            item["got"] = got
            item["passed"] = got == expected and type(got) == type(expected)
        except Exception as e:
            item["error"] = f"{type(e).__name__}: {e}"
        results.append(item)

    # repr() garante que qualquer valor devolvido possa ser exibido/serializado
    for item in results:
        item["got"] = repr(item["got"])
        item["expected"] = repr(item["expected"])
        item["args"] = ", ".join(repr(a) for a in item["args"])

    print(json.dumps({"ok": True, "error": None, "results": results}))


if __name__ == "__main__":
    main()