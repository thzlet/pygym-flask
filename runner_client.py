"""Chama o sandbox_runner.py em um subprocesso, com timeout."""
import json
import subprocess
import sys
from pathlib import Path

RUNNER = Path(__file__).with_name("sandbox_runner.py")
TIMEOUT_SECONDS = 3


def run_student_code(code, exercise):
    payload = json.dumps(
        {"code": code, "function": exercise["funcao"], "tests": exercise["testes"]}
    )
    try:
        proc = subprocess.run(
            [sys.executable, "-I", str(RUNNER)],
            input=payload,
            capture_output=True,
            text=True,
            timeout=TIMEOUT_SECONDS,
        )
    except subprocess.TimeoutExpired:
        return {
            "ok": False,
            "error": f"Seu código demorou mais de {TIMEOUT_SECONDS} segundos. "
                     "Será que existe um laço infinito (while sem fim)?",
            "results": [],
        }

    try:
        return json.loads(proc.stdout)
    except json.JSONDecodeError:
        return {
            "ok": False,
            "error": "Não consegui executar seu código. Verifique se ele usa muita memória ou tem algum erro grave.",
            "results": [],
        }