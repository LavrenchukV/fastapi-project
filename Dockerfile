FROM python:3.11-slim

WORKDIR /app

# Встановити залежності
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Скопіювати весь код у контейнер
COPY . .

# Логи одразу виводити в консоль
ENV PYTHONUNBUFFERED=1

# URL бази будемо передавати при запуску контейнера
ENV DATABASE_URL=""  
# DATABASE_URL приходить з .env або з секретів у GitHub Actions

# ЗАПУСК:
# 1) Прогнати Alembic міграції
# 2) Запустити FastAPI через uvicorn
CMD ["sh", "-c", "alembic upgrade head && uvicorn app.main:app --host 0.0.0.0 --port 8000"]