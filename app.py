"""
Журнал домашней лаборатории — простой сайт на Flask.

Запуск:
    pip install -r requirements.txt
    python app.py
Потом открой в браузере: http://127.0.0.1:5000
"""

import json
from datetime import datetime
from pathlib import Path

from flask import Flask, redirect, render_template, request, url_for

# Создаём приложение. __name__ подсказывает Flask, где искать папки templates и static
app = Flask(__name__)

# Файл, в котором хранятся записи (появится сам при первом сохранении)
DATA_FILE = Path(__file__).parent / "entries.json"


def load_entries():
    """Читает записи из JSON-файла. Если файла нет — возвращает пустой список."""
    if not DATA_FILE.exists():
        return []
    with open(DATA_FILE, encoding="utf-8") as f:
        return json.load(f)


def save_entries(entries):
    """Записывает список записей обратно в JSON-файл."""
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(entries, f, ensure_ascii=False, indent=2)


# Маршрут "/" — главная страница. Принимает два типа запросов:
#   GET  — браузер просто открыл страницу
#   POST — пользователь отправил форму
@app.route("/", methods=["GET", "POST"])
def index():
    error = None

    if request.method == "POST":
        title = request.form.get("title", "").strip()
        text = request.form.get("text", "").strip()

        if not title:
            error = "Введи заголовок записи."
        elif len(title) > 100:
            error = "Заголовок не должен быть длиннее 100 символов."
        else:
            entries = load_entries()
            entries.insert(0, {  # новые записи — сверху
                "title": title,
                "text": text,
                "date": datetime.now().strftime("%d.%m.%Y %H:%M"),
            })
            save_entries(entries)
            # Паттерн Post/Redirect/Get: после сохранения перенаправляем,
            # чтобы обновление страницы (F5) не отправило форму повторно
            return redirect(url_for("index"))

    return render_template("index.html", entries=load_entries(), error=error)


@app.route("/delete/<int:number>", methods=["POST"])
def delete(number):
    """Удаляет запись по её порядковому номеру в списке."""
    entries = load_entries()
    if 0 <= number < len(entries):
        entries.pop(number)
        save_entries(entries)
    return redirect(url_for("index"))


@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    # debug=True — сервер сам перезапускается, когда ты меняешь код.
    # Только для разработки, не для настоящего сервера!
    app.run(debug=True)
