# Журнал домашней лаборатории

Учебный сайт на Python и Flask: записываешь, что настроил в домашней лаборатории, а записи сохраняются в файл.

## Запуск

```bash
python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # Linux / macOS
pip install -r requirements.txt
python app.py
```

Открой в браузере http://127.0.0.1:5000

## Структура

```
lab-journal/
├── app.py              # логика сайта: маршруты, чтение и запись записей
├── requirements.txt    # зависимости Python
├── templates/          # HTML-шаблоны (Jinja2)
│   ├── base.html       # общий каркас страницы
│   ├── index.html      # главная: форма и список записей
│   └── about.html      # страница "О проекте"
└── static/
    └── style.css       # оформление
```
