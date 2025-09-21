# djangorlar

Учебный Django-проект (Practice #2).

## Установка и запуск

```bash
# 1. Создаём виртуальное окружение
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# 2. Устанавливаем зависимости
pip install -r requirements.txt

# 3. Создаём файл .env (см. .env.example)
SECRET_KEY=your-secret-key
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost

# 4. Выполняем миграции
python src/manage.py migrate

# 5. Запускаем сервер
python src/manage.py runserver
```
