# Базовый образ Python 3.11, оптимальный и легковесный
FROM python:3.11-slim

# Указываем рабочую папку внутри контейнера
WORKDIR /app

# Копируем файлы проекта внутрь контейнера
COPY . .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Запускаем бота
CMD ["python", "bot.py"]
