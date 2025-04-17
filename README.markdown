# JarvisAI

JarvisAI — твой личный ИИ: локальный, мощный, мультимодальный. Умеет обрабатывать текст, голос, видео, код, управлять устройствами, интегрироваться с Unreal Engine и учиться на данных. Это приватный проект, храни его в безопасности!

## Возможности
- Генерация текста, кода, ответов с RAG.
- Распознавание и синтез речи.
- Обработка видео (субтитры, укорачивание).
- Управление устройствами (MQTT).
- Генерация ассетов для Unreal Engine.
- Веб-поиск (SerpAPI).
- Веб-дэшборд и REST API.

## Установка

### Локально
1. Убедись, что есть Python 3.11.6:
   ```bash
   python --version
   ```
   Нет? Скачай с [python.org](https://www.python.org/downloads/).

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
   huggingface-cli download openai/whisper-base --local-dir checkpoints/whisper
   huggingface-cli download openai/clip-vit-base-patch32 --local-dir checkpoints/clip
   ```

8. Настрой `config.yaml`:
   - Укажи `security_key` (любой секрет).
   - Добавь `serpapi_key` ([serpapi.com](https://serpapi.com)).
   - Проверь пути к моделям.

9. Запусти:
   ```bash
   python main.py
   ```
   - Дэшборд: `http://localhost:8000/static/index.html`
   - API: `http://localhost:8080`

### Google Colab
1. Создай ноутбук в [Google Colab](https://colab.research.google.com).
2. Выполни:
   ```python
   !git clone https://github.com/TidesLuck/JarvisAI.git
   %cd JarvisAI
   !apt-get update
   !apt-get install -y python3.11 python3.11-dev python3.11-distutils ffmpeg
   !curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
   !python3.11 get-pip.py
   !python3.11 -m pip install -r requirements.txt
   !python3.11 -m pip install huggingface_hub
   !huggingface-cli download meta-llama/Llama-2-7b --local-dir checkpoints/llama
   !huggingface-cli download openai/whisper-base --local-dir checkpoints/whisper
   !huggingface-cli download openai/clip-vit-base-patch32 --local-dir checkpoints/clip
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
  - `учись data/input/learn/doc.txt` → "Обучился на файле doc.txt!"
  - `поиск квантовые компьютеры` → "Квантовые компьютеры используют кубиты..."
  - `измени data/input/modify/video.mp4 добавь субтитры` → "Видео с субтитрами: data/output/modified_video_..."

### Через API
- Текст:
  ```bash
  curl -X POST -H "Content-Type: application/json" -d '{"prompt":"привет, Джарвис"}' http://localhost:8080/api/v1/text
  ```
- Код:
  ```bash
  curl -X POST -H "Content-Type: application/json" -d '{"code":"print(\"Hello\")"}' http://localhost:8080/api/v1/code
  ```
- Голос:
  ```bash
  curl -X POST -H "Content-Type: application/json" -d '{"action":"voice_command", "audio_path":"data/input/command.wav"}' http://localhost:8080/api/v1/audio
  ```

### Через папки
- `data/input/learn/` — для обучения (кидай .txt, .pdf, .docx).
- `data/input/modify/` — для изменения файлов.
- `data/input/analyze/` — для анализа.

## Если что-то непонятно
- Читай `INSTRUCTIONS.md` в корне проекта. Там всё: обучение, интеграция, внедрение, устранение ошибок.

## Примечания
- **Приватность**: Храни репозиторий приватным. Не дели `security_key`, `serpapi_key`, токены.
- **Модели**: LLaMA-2-7B требует ~14 ГБ, используй GPU (≥8 ГБ VRAM).
- **Colab**: Бесплатный Colab может отключать GPU, попробуй Colab Pro.

*Создано: 17 апреля 2025*
