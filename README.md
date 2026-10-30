# 🐍 PyGym: plataforma de exercícios Python com feedback automático


## O que o projeto faz

O aluno escolhe um desafio, escreve uma função Python direto no navegador e recebe,
na hora, o resultado de uma bateria de testes: o que foi enviado, o que era esperado e
o que a função devolveu.

Funcionalidades pensadas para o ensino:

- **Dificuldade progressiva:** cinco desafios (Fácil → Médio → Desafio), cada um com os conceitos trabalhados.
- **Feedback detalhado:** a tabela de testes mostra entrada, resultado esperado e resultado obtido, além de mensagens de erro em português.
- **Dica gradual:** a dica só aparece depois de 2 tentativas sem sucesso, para o aluno tentar antes de ser ajudado.
- **Solução comentada:** após acertar, o aluno vê uma solução de referência e uma explicação do raciocínio, incluindo erros comuns.
- **Progresso salvo na sessão:** barra de progresso na página inicial.

## Funções integradas do Flask utilizadas

`Flask`, `render_template`, `request`, `redirect`, `url_for`, `session`, `flash`,
`abort`, `errorhandler` e `get_flashed_messages`, além de templates Jinja2 com herança (`extends`/`block`).

## Como executar

```bash
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

Depois, abra http://127.0.0.1:5000 no navegador.

## Estrutura

```
app.py              rotas do Flask
exercises.py        banco de exercícios (enunciado, testes, dica, solução)
runner_client.py    chama o executor em um subprocesso, com timeout
sandbox_runner.py   executa o código do aluno de forma restrita
templates/          páginas HTML (Jinja2)
static/style.css    estilos
requirements.txt    dependências
```

## Ideias de evolução

- Cadastro de alunos e salvamento de progresso em banco de dados (SQLite).
- Painel do tutor com os exercícios em que os alunos mais erram.
- Novos desafios em arquivos separados, por tema (listas, dicionários, funções).
