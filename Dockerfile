# Установка базового образа
FROM python:3.6

# Установка рабочей дериктории
WORKDIR /app

# Копирование зависимостей
COPY requirements.txt .
RUN pip install -U pip
RUN pip install -r requirements.txt

# Копирование проекта
COPY . .

# Предустанавливаем команду pytest и отчёт
ENTRYPOINT ["pytest", "--alluredir", "allure-report"]

# В качестве адреса --executor необходимо указывать адрес selenoid
CMD ["--browser", "chrome", "--bversion", "88.0", "--executor", "192.168.0.5"]
