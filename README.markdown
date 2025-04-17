JarvisAI
JarvisAI — твой личный ИИ: локальный, мощный, мультимодальный. Умеет обрабатывать текст, голос, видео, код, генерировать картинки, искать в интернете, управлять устройствами, создавать ассеты для Unreal Engine и автоматически учиться. Это приватный проект, храни его в безопасности!
Возможности

Генерация текста, кода, ответов с RAG.
DeepSearch: умный поиск в интернете (как Grok 3).
Распознавание и синтез речи с диалоговым контекстом.
Обработка видео (субтитры, укорачивание).
Генерация картинок (как DALL·E).
Автообучение на веб-данных.
Управление устройствами (MQTT).
Генерация ассетов для Unreal Engine.
Веб-дэшборд и REST API.

Установка
Локально

Убедись, что есть Python 3.11.6:
python --version

Нет? Скачай с python.org.

Установи Git:
# MacOS
brew install git
# Linux
sudo apt-get install git
# Windows: скачай с git-scm.com


Клонируй приватный репозиторий:
git clone https://github.com/TidesLuck/JarvisAI.git
cd JarvisAI


Создай виртуальное окружение:
python -m venv jarvisai_env
source jarvisai_env/bin/activate  # Linux/MacOS
jarvisai_env\Scripts\activate     # Windows


Установи зависимости:
pip install -r requirements.txt
pip install diffusers==0.21.4 transformers==4.33.2 speechrecognition==3.10.0 pyttsx3==2.90


Установи FFmpeg:
# MacOS
brew install ffmpeg
# Linux
sudo apt-get install ffmpeg
# Windows: скачай с ffmpeg.org, добавь в PATH


Скачай модели:
pip install huggingface_hub
huggingface-cli download meta-llama/Llama-2-7b --local-dir checkpoints/llama
huggingface-cli download openai/whisper-large --local-dir checkpoints/whisper-large
huggingface-cli download openai/clip-vit-base-patch32 --local-dir checkpoints/clip
huggingface-cli download stabilityai/stable-diffusion-2-1 --local-dir checkpoints/sd


Настрой config.yaml:

Укажи security_key (любой секрет).
Добавь serpapi_key (serpapi.com).
Проверь пути к моделям (checkpoints/llama, checkpoints/whisper-large, checkpoints/clip, checkpoints/sd).


Запусти:
python main.py


Дэшборд: http://localhost:8000/static/index.html
API: http://localhost:8080



Google Colab

Создай ноутбук в Google Colab.
Выполни:!git clone https://твой_токен@github.com/TidesLuck/JarvisAI.git
%cd JarvisAI
!apt-get update
!apt-get install -y python3.11 python3.11-dev python3.11-distutils ffmpeg
!curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
!python3.11 get-pip.py
!python3.11 -m pip install -r requirements.txt
!python3.11 -m pip install diffusers==0.21.4 transformers==4.33.2 speechrecognition==3.10.0 pyttsx3==2.90
!python3.11 -m pip install huggingface_hub
!huggingface-cli download meta-llama/Llama-2-7b --local-dir checkpoints/llama
!huggingface-cli download openai/whisper-large --local-dir checkpoints/whisper-large
!huggingface-cli download openai/clip-vit-base-patch32 --local-dir checkpoints/clip
!huggingface-cli download stabilityai/stable-diffusion-2-1 --local-dir checkpoints/sd
!python3.11 -m pip install pyngrok
from pyngrok import ngrok
ngrok.set_auth_token("твой_ngrok_токен")
public_url = ngrok.connect(8000).public_url
print(f"Дэшборд: {public_url}/static/index.html")
!python3.11 main.py



Использование
Через дэшборд

Открой http://localhost:8000/static/index.html.
Примеры команд:
привет, Джарвис → "Привет! Чем могу помочь?"
поиск квантовые компьютеры → Умный поиск с уточнением.
сгенерируй картинку кота в космосе → Картинка в data/output/.
учись data/input/learn/doc.txt → Обучение на файле.
учись искусственный интеллект → Автообучение на веб-данных.
измени data/input/modify/video.mp4 добавь субтитры → Видео с субтитрами.



Через API

Текст:curl -X POST -H "Content-Type: application/json" -d '{"prompt":"привет, Джарвис"}' http://localhost:8080/api/v1/text


Картинка:curl -X POST -H "Content-Type: application/json" -d '{"prompt":"сгенерируй картинку кота в космосе"}' http://localhost:8080/api/v1/image


Голос:curl -X POST -H "Content-Type: application/json" -d '{"action":"stream"}' http://localhost:8080/api/v1/audio


Код:curl -X POST -H "Content-Type: application/json" -d '{"code":"print(\"Hello\")"}' http://localhost:8080/api/v1/code



Через папки

data/input/learn/ — для обучения (кидай .txt, .pdf, .docx).
data/input/modify/ — для изменения файлов.
data/input/analyze/ — для анализа.
data/output/ — результаты (картинки, видео, код).

Если что-то непонятно

Читай INSTRUCTIONS.md в корне проекта. Там всё: установка, обучение, новые фичи, устранение ошибок.

Примечания

Приватность: Репозиторий приватный, не дели security_key, serpapi_key, токены.
Модели: LLaMA-2-7B (14 ГБ), Whisper-large (3 ГБ), Stable Diffusion (~5 ГБ). Используй GPU (≥16 ГБ VRAM).
Colab: Бесплатный Colab может отключать GPU, попробуй Colab Pro+.

Создано: 17 апреля 2025
