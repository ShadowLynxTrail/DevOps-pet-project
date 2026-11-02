[![Build and Test](https://github.com/ShadowLynxTrail/DevOps-pet-project/actions/workflows/deploy.yml/badge.svg)](https://github.com/ShadowLynxTrail/DevOps-pet-project/actions/workflows/deploy.yml)

# DevOps Pet Project 🚀

Учебный проект, созданный для демонстрации базовых DevOps-практик, контейнеризации приложений и настройки пайплайнов CI/CD.

> **Внимание:** Вставь сюда свой бейджик статуса сборки, если ты уже сгенерировал его в Actions (инструкция ниже). Если нет — просто удали эту строку.

## 🎯 Цель проекта
Показать на практике понимание жизненного цикла разработки ПО (SDLC), изоляции среды и автоматизации процессов. 

## 🛠 Использованный стек технологий
*   **Python 3.9** — язык написания основного скрипта.
*   **Docker** — контейнеризация приложения (создание `Dockerfile`).
*   **GitHub Actions** — настройка пайплайна CI/CD (Continuous Integration).
*   **Git** — контроль версий.

## ⚙️ Как работает CI/CD пайплайн
В проекте настроен автоматический пайплайн (файл `.github/workflows/deploy.yml`), который запускается при каждом пуше в ветку `main`.
Он выполняет следующие шаги:
1.  **Checkout code**: Клонирует код из репозитория.
2.  **Set up Docker Buildx**: Подготавливает окружение для работы с Docker.
3.  **Build Docker image**: Собирает Docker-образ на основе `Dockerfile`.
4.  **Test Docker image (Run it)**: Запускает контейнер и проверяет, что скрипт выполняется без ошибок (если скрипт падает с ошибкой, пайплайн помечается как Failed).

## 💻 Как запустить проект локально
Для запуска вам понадобится установленный **Docker**.

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/ShadowLynxTrail/DevOps-pet-project.git

2. Перейдите в папку с проектом:

bash
cd DevOps-pet-project

3. Соберите Docker-образ:

bash
docker build -t my-devops-app .

4. Запустите контейнер:

bash
docker run my-devops-app

## 📂 Структура проекта
* `app.py` — исходный код приложения (генератор случайных фраз).

* `Dockerfile` — инструкция для сборки Docker-образа.

* `.github/workflows/deploy.yml` — конфигурация CI/CD пайплайна.
