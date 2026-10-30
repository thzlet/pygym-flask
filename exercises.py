"""Banco de exercícios da plataforma.

Cada exercício é um dicionário com:
- id, titulo, nivel, conceitos: metadados exibidos na tela
- enunciado: texto para o aluno
- funcao: nome da função que o aluno deve escrever
- codigo_inicial: esqueleto que aparece no editor
- testes: lista de (argumentos, resultado_esperado)
- dica: aparece depois de 2 tentativas erradas
- solucao / explicacao: aparecem depois que o aluno acerta
"""

EXERCISES = [
    {
        "id": 1,
        "titulo": "Par ou ímpar?",
        "nivel": "Fácil",
        "conceitos": ["funções", "if/else", "operador %"],
        "enunciado": (
            "Escreva a função `par_ou_impar(n)` que recebe um número inteiro "
            "e devolve a string `\"par\"` ou `\"ímpar\"`."
        ),
        "funcao": "par_ou_impar",
        "codigo_inicial": "def par_ou_impar(n):\n    # escreva seu código aqui\n    pass\n",
        "testes": [([2], "par"), ([7], "ímpar"), ([0], "par"), ([-3], "ímpar"), ([100], "par")],
        "dica": "O operador % devolve o resto da divisão. Qual é o resto de um número par dividido por 2?",
        "solucao": (
            "def par_ou_impar(n):\n"
            "    if n % 2 == 0:\n"
            "        return \"par\"\n"
            "    return \"ímpar\"\n"
        ),
        "explicacao": (
            "Todo número par tem resto 0 na divisão por 2. Usamos `if` para testar isso e "
            "`return` para devolver a resposta. Note que `-3 % 2` vale 1 em Python, "
            "então números negativos também funcionam."
        ),
    },
    {
        "id": 2,
        "titulo": "Soma de uma lista",
        "nivel": "Fácil",
        "conceitos": ["listas", "for", "acumulador"],
        "enunciado": (
            "Escreva a função `somar_lista(numeros)` que recebe uma lista de números "
            "e devolve a soma de todos eles. Desafio: tente resolver com um `for`, "
            "sem usar a função `sum`."
        ),
        "funcao": "somar_lista",
        "codigo_inicial": "def somar_lista(numeros):\n    # escreva seu código aqui\n    pass\n",
        "testes": [([[1, 2, 3]], 6), ([[]], 0), ([[10]], 10), ([[-1, 1]], 0), ([[2.5, 2.5]], 5.0)],
        "dica": "Crie uma variável `total = 0` antes do laço e vá somando cada elemento nela.",
        "solucao": (
            "def somar_lista(numeros):\n"
            "    total = 0\n"
            "    for n in numeros:\n"
            "        total += n\n"
            "    return total\n"
        ),
        "explicacao": (
            "Esse padrão se chama acumulador: começamos de um valor neutro (0) e atualizamos "
            "a cada volta do laço. Repare que a lista vazia funciona sozinha, o laço "
            "simplesmente não roda e devolvemos 0. Na prática, `sum(numeros)` faz o mesmo."
        ),
    },
    {
        "id": 3,
        "titulo": "Contando vogais",
        "nivel": "Médio",
        "conceitos": ["strings", "for", "in", "lower()"],
        "enunciado": (
            "Escreva a função `contar_vogais(texto)` que devolve quantas vogais "
            "(a, e, i, o, u) existem no texto, sem diferenciar maiúsculas de minúsculas. "
            "Considere apenas vogais sem acento."
        ),
        "funcao": "contar_vogais",
        "codigo_inicial": "def contar_vogais(texto):\n    # escreva seu código aqui\n    pass\n",
        "testes": [(["banana"], 3), (["PYTHON"], 1), ([""], 0), (["rhythm"], 0), (["Aeiou"], 5)],
        "dica": "Converta o texto para minúsculas com `.lower()` e pergunte, para cada letra, se ela está em `\"aeiou\"`.",
        "solucao": (
            "def contar_vogais(texto):\n"
            "    total = 0\n"
            "    for letra in texto.lower():\n"
            "        if letra in \"aeiou\":\n"
            "            total += 1\n"
            "    return total\n"
        ),
        "explicacao": (
            "Strings são sequências, então podemos percorrê-las com `for`. "
            "Normalizar o texto com `.lower()` evita escrever as vogais maiúsculas também. "
            "O operador `in` verifica se um caractere pertence a outra string."
        ),
    },
    {
        "id": 4,
        "titulo": "Palíndromo",
        "nivel": "Médio",
        "conceitos": ["strings", "fatiamento", "replace()", "booleanos"],
        "enunciado": (
            "Escreva a função `eh_palindromo(texto)` que devolve `True` se o texto "
            "é lido igual de trás para frente, ignorando maiúsculas e espaços, "
            "e `False` caso contrário."
        ),
        "funcao": "eh_palindromo",
        "codigo_inicial": "def eh_palindromo(texto):\n    # escreva seu código aqui\n    pass\n",
        "testes": [
            (["arara"], True),
            (["Python"], False),
            (["A cara rac a"], True),
            ([""], True),
            (["Socorram me subi no onibus em marrocos"], True),
        ],
        "dica": "Limpe o texto (minúsculas, sem espaços) e compare com ele mesmo invertido: `texto[::-1]`.",
        "solucao": (
            "def eh_palindromo(texto):\n"
            "    limpo = texto.lower().replace(\" \", \"\")\n"
            "    return limpo == limpo[::-1]\n"
        ),
        "explicacao": (
            "O fatiamento `[::-1]` percorre a string de trás para frente. "
            "Como a comparação `==` já devolve `True` ou `False`, podemos retornar "
            "direto o resultado, sem precisar de `if`."
        ),
    },
    {
        "id": 5,
        "titulo": "FizzBuzz",
        "nivel": "Desafio",
        "conceitos": ["laços", "condicionais encadeados", "listas", "ordem das condições"],
        "enunciado": (
            "Escreva a função `fizzbuzz(n)` que devolve uma lista com os valores de 1 até n. "
            "Para múltiplos de 3 coloque `\"Fizz\"`, para múltiplos de 5 coloque `\"Buzz\"` "
            "e para múltiplos de 3 e de 5 ao mesmo tempo coloque `\"FizzBuzz\"`. "
            "Os demais números ficam como estão."
        ),
        "funcao": "fizzbuzz",
        "codigo_inicial": "def fizzbuzz(n):\n    # escreva seu código aqui\n    pass\n",
        "testes": [
            ([5], [1, 2, "Fizz", 4, "Buzz"]),
            ([1], [1]),
            ([15], [1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz", 11, "Fizz", 13, 14, "FizzBuzz"]),
            ([0], []),
        ],
        "dica": "A ordem importa: teste primeiro se o número é múltiplo de 3 e de 5 ao mesmo tempo.",
        "solucao": (
            "def fizzbuzz(n):\n"
            "    resultado = []\n"
            "    for i in range(1, n + 1):\n"
            "        if i % 15 == 0:\n"
            "            resultado.append(\"FizzBuzz\")\n"
            "        elif i % 3 == 0:\n"
            "            resultado.append(\"Fizz\")\n"
            "        elif i % 5 == 0:\n"
            "            resultado.append(\"Buzz\")\n"
            "        else:\n"
            "            resultado.append(i)\n"
            "    return resultado\n"
        ),
        "explicacao": (
            "O erro mais comum é testar `% 3` antes de `% 15`: o 15 cairia em \"Fizz\" e nunca "
            "chegaria ao \"FizzBuzz\". Em cadeias `if/elif`, a condição mais específica vem primeiro. "
            "Note também que `range(1, n + 1)` inclui o n."
        ),
    },
]


def get_exercise(exercise_id):
    for ex in EXERCISES:
        if ex["id"] == exercise_id:
            return ex
    return None