import os

from flask import Flask, abort, flash, redirect, render_template, request, session, url_for

from exercises import EXERCISES, get_exercise
from runner_client import run_student_code

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "chave-de-desenvolvimento-troque-em-producao")

MAX_CODE_LENGTH = 3000
ATTEMPTS_FOR_HINT = 2


def _solved():
    return set(session.get("solved", []))


@app.route("/")
def index():
    solved = _solved()
    progress = round(100 * len(solved) / len(EXERCISES))
    return render_template(
        "index.html", exercises=EXERCISES, solved=solved, progress=progress
    )


@app.route("/exercicio/<int:exercise_id>", methods=["GET", "POST"])
def exercise(exercise_id):
    ex = get_exercise(exercise_id)
    if ex is None:
        abort(404)

    code = ex["codigo_inicial"]
    result = None
    attempts = session.get("attempts", {})
    key = str(exercise_id)

    if request.method == "POST":
        code = request.form.get("code", "")
        if not code.strip():
            flash("Escreva algum código antes de enviar.", "erro")
        elif len(code) > MAX_CODE_LENGTH:
            flash(f"Código muito longo (máximo de {MAX_CODE_LENGTH} caracteres).", "erro")
        else:
            result = run_student_code(code, ex)
            all_passed = (
                result["ok"]
                and result["results"]
                and all(r["passed"] for r in result["results"])
            )
            if all_passed:
                solved = _solved()
                solved.add(exercise_id)
                session["solved"] = sorted(solved)
                flash("Parabéns! Todos os testes passaram. 🎉", "sucesso")
            else:
                attempts[key] = attempts.get(key, 0) + 1
                session["attempts"] = attempts

    is_solved = exercise_id in _solved()
    show_hint = attempts.get(key, 0) >= ATTEMPTS_FOR_HINT and not is_solved
    next_id = exercise_id + 1 if get_exercise(exercise_id + 1) else None

    return render_template(
        "exercise.html",
        ex=ex,
        code=code,
        result=result,
        is_solved=is_solved,
        show_hint=show_hint,
        attempts=attempts.get(key, 0),
        next_id=next_id,
    )


@app.route("/reiniciar", methods=["POST"])
def reset():
    session.clear()
    flash("Progresso reiniciado.", "sucesso")
    return redirect(url_for("index"))


@app.errorhandler(404)
def not_found(_):
    return render_template("404.html"), 404


if __name__ == "__main__":
    app.run(debug=True)