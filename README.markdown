# JarvisAI

JarvisAI — твой личный ИИ, сравнимый с Grok 3 и GPT-4. Локальный, мультимодальный, гибкий. Умеет обрабатывать текст, голос, видео, код, генерировать картинки, искать с DeepSearch, управлять устройствами, создавать ассеты для Unreal Engine и автоматически учиться. Это приватный проект, храни его в безопасности!

## Возможности

- Генерация текста, кода, ответов с RAG.
- DeepSearch: итеративный поиск (как Grok 3).
- Think Mode: глубокое обдумывание (как Grok 3).
- Распознавание и синтез речи с диалоговым контекстом (как GPT-4).
- Генерация картинок (как DALL·E).
- Обработка видео (субтитры, укорачивание).
- Автообучение на файлах и вебе.
- Управление устройствами (MQTT).
- Генерация ассетов для Unreal Engine (Blueprint, меши).
- Веб-дэшборд и REST API.

## Установка

### Локально

1. Убедись, что есть Python 3.11.6:

   ```bash
   python --version
   ```

   Нет? Скачай с python.org.

2. Установи Git:

   ```bash
   # MacOS
   brew install git
   # Linux
   sudo apt-get install git
   # Windows: скачай с git-scm.com
   ```

3. Клонируй приватный репозиторий:

   ```bash
   git clone https://github.com/TidesLuck/JarvisAI.git
   cd JarvisAI
   ```

4. Создай виртуальное окружение:

   ```bash
   python -m venv jarvisai_env
   source jarvisai_env/bin/activate  # Linux/MacOS
   jarvisai_env\Scripts\activate     # Windows
   ```

5. Установи зависимости:

   ```bash
   pip install -r requirements.txt
   pip install diffusers==0.21.4 transformers==4.33.2 speechrecognition==3.10.0 pyttsx3==2.90
   ```

6. Установи FFmpeg:

   ```bash
   # MacOS
   brew install ffmpeg
   # Linux
   sudo apt-get install ffmpeg
   # Windows: скачай с ffmpeg.org, добавь в PATH
   ```

7. Скачай модели:

   ```bash
   pip install huggingface_hub
   huggingface-cli download meta-llama/Llama-2-7b --local-dir checkpoints/llama
   huggingface-cli download openai/whisper-large --local-dir checkpoints/whisper-large
   huggingface-cli download openai/clip-vit-base-patch32 --local-dir checkpoints/clip
   huggingface-cli download stabilityai/stable-diffusion-2-1 --local-dir checkpoints/sd
   ```

8. Настрой `config.yaml`:

   - Укажи `security_key` (любой секрет).
   - Добавь `serpapi_key` (serpapi.com).
   - Укажи `unreal_config.engine_path` (если используешь Unreal Engine).
   - Проверь пути к моделям (`checkpoints/llama`, `checkpoints/whisper-large`, `checkpoints/clip`, `checkpoints/sd`).

9. Запусти:

   ```bash
   python main.py
   ```

   - Дэшборд: `http://localhost:8000/static/index.html`
   - API: `http://localhost:8080`

### Google Colab

1. Создай ноутбук в Google Colab.

2. Выполни:

   ```python
   !git clone https://твой_токен@github.com/TidesLuck/JarvisAI.git
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
   ```

## Использование

### Через дэшборд

- Открой `http://localhost:8000/static/index.html`.
- Примеры команд:
  - `привет, Джарвис` → "Привет! Чем могу помочь?"
  - `поиск квантовые компьютеры` → DeepSearch с точными результатами.
  - `сгенерируй картинку кота в космосе` → Картинка в `data/output/`.
  - `учись data/input/learn/doc.txt` → Обучение на файле.
  - `учись искусственный интеллект` → Автообучение на вебе.
  - `измени video.mp4 добавь субтитры` → Видео с субтитрами.
  - `включи лампу device_123` → Управление IoT.
  - `сгенерируй blueprint для куба` → Unreal Engine ассет.

### Через API

- Текст:

  ```bash
  curl -X POST -H "Content-Type: application/json" -d '{"prompt":"привет, Джарвис"}' http://localhost:8080/api/v1/text
  ```

- Картинка:

  ```bash
  curl -X POST -H "Content-Type: application/json" -d '{"prompt":"сгенерируй картинку кота в космосе"}' http://localhost:8080/api/v1/image
  ```

- Голос:

  ```bash
  curl -X POST -H "Content-Type: application/json" -d '{"action":"stream"}' http://localhost:8080/api/v1/audio
  ```

- Код:

  ```bash
  curl -X POST -H "Content-Type: application/json" -d '{"code":"print(\"Hello\")"}' http://localhost:8080/api/v1/code
  ```

### Через папки

- `data/input/learn/` — для обучения (.txt, .pdf, .docx).
- `data/input/modify/` — для изменения файлов.
- `data/input/analyze/` — для анализа.
- `data/output/` — результаты (картинки, видео, код).

## Если что-то непонятно

- Читай `INSTRUCTIONS.md` в корне проекта. Там всё: установка, обучение, новые фичи, устранение ошибок.

## Примечания

- **Приватность**: Репозиторий приватный, не дели `security_key`, `serpapi_key`, токены.
- **Модели**: LLaMA-2-7B (\~14 ГБ), Whisper-large (\~3 ГБ), Stable Diffusion (\~5 ГБ). Используй GPU (≥16 ГБ VRAM).
- **Colab**: Бесплатный Colab может отключать GPU, попробуй Colab Pro+.

*Создано: 17 апреля 2025*