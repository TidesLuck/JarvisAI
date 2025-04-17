# JarvisAI: Инструкции по использованию

JarvisAI — это твой личный богоподобный ИИ: локальный, мощный, модульный. Он умеет обрабатывать текст, голос, видео, код, управлять устройствами, интегрироваться с Unreal Engine и учиться на твоих данных. Этот файл — твой гид по установке, обучению, интеграции и использованию JarvisAI. Всё просто и понятно, даже если ты не гуру программирования.

---

## 1. Что такое JarvisAI?

JarvisAI — это ИИ, который работает у тебя на компе или в облаке (например, Google Colab). Он:
- **Мультимодальный**: Текст, голос, видео, изображения, код.
- **Самообучаемый**: Учится на файлах, сайтах, через API.
- **Интуитивный**: Управляй через команды, папки, веб-дэшборд.
- **Гибкий**: Интеграция с Unreal Engine, устройствами, облаком.
- **Безопасный**: Локальное хранение, шифрование, этические барьеры.

Ключевые возможности:
- Генерация текста, кода, ответов с RAG (поиск в знаниях).
- Распознавание и синтез речи.
- Обработка видео (субтитры, укорачивание).
- Управление устройствами через MQTT.
- Генерация ассетов для Unreal Engine (Blueprint, меши).
- Веб-поиск через SerpAPI.
- Автоматическая кластеризация знаний.
- REST API и веб-дэшборд для управления.

---

## 2. Установка

### Локальный компьютер
1. **Проверь Python**:
   Убедись, что установлен Python 3.11.6:
   ```bash
   python --version
   ```
   Нет? Скачай с [python.org](https://www.python.org/downloads/).

2. **Установи Git**:
   - Windows: Скачай [Git for Windows](https://git-scm.com/download/win).
   - MacOS: `brew install git`
   - Linux: `sudo apt-get install git`
   Проверь: `git --version`

3. **Создай виртуальное окружение**:
   ```bash
   python -m venv jarvisai_env
   source jarvisai_env/bin/activate  # Linux/MacOS
   jarvisai_env\Scripts\activate     # Windows
   ```

4. **Скачай проект**:
   Если проект на GitHub:
   ```bash
   git clone https://github.com/TidesLuck/JarvisAI.git
   cd JarvisAI
   ```
   Или создай папку `JarvisAI` и скопируй файлы (структура ниже).

5. **Установи зависимости**:
   ```bash
   pip install -r requirements.txt
   ```
   Если проблемы с `torch` или `bitsandbytes`:
   ```bash
   pip install torch==2.0.1 --index-url https://download.pytorch.org/whl/cu118
   pip install bitsandbytes==0.41.1 --no-binary bitsandbytes
   ```

6. **Установи FFmpeg** (для видео/аудио):
   - Windows: Скачай с [ffmpeg.org](https://ffmpeg.org/download.html), добавь `ffmpeg/bin` в PATH.
   - MacOS: `brew install ffmpeg`
   - Linux: `sudo apt-get install ffmpeg`
   Проверь: `ffmpeg -version`

7. **Скачай модели**:
   ```bash
   pip install huggingface_hub
   huggingface-cli download meta-llama/Llama-2-7b --local-dir checkpoints/llama
   huggingface-cli download openai/whisper-base --local-dir checkpoints/whisper
   huggingface-cli download openai/clip-vit-base-patch32 --local-dir checkpoints/clip
   ```

8. **Настрой `config.yaml`**:
   - Открой `config.yaml` в корне проекта.
   - Укажи:
     - `security_key`: Любой секретный ключ.
     - `serpapi_key`: Получи на [serpapi.com](https://serpapi.com).
     - `unreal_config.engine_path`: Путь к Unreal Engine (если используешь).
     - Проверь пути к моделям (`checkpoints/llama`, `checkpoints/whisper`, `checkpoints/clip`).

9. **Запусти**:
   ```bash
   python main.py
   ```
   - Дэшборд: `http://localhost:8000/static/index.html`
   - API: `http://localhost:8080`

### Google Colab
1. Создай новый ноутбук в [Google Colab](https://colab.research.google.com).
2. Выполни команды в ячейках:

   ```python
   # Настрой Git
   !git config --global user.name "Твоё_Имя"
   !git config --global user.email "твой_email@example.com"

   # Клонируй приватный репозиторий (вставь токен GitHub)
   !git clone https://github.com/TidesLuck/JarvisAI.git
   %cd JarvisAI

   # Установи Python 3.11 и зависимости
   !apt-get update
   !apt-get install -y python3.11 python3.11-dev python3.11-distutils
   !curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
   !python3.11 get-pip.py
   !python3.11 -m pip install -r requirements.txt
   !python3.11 -m pip install torch==2.0.1 --index-url https://download.pytorch.org/whl/cu118
   !python3.11 -m pip install bitsandbytes==0.41.1 --no-binary bitsandbytes

   # Установи FFmpeg
   !apt-get install -y ffmpeg

   # Скачай модели
   !python3.11 -m pip install huggingface_hub
   !huggingface-cli download meta-llama/Llama-2-7b --local-dir checkpoints/llama
   !huggingface-cli download openai/whisper-base --local-dir checkpoints/whisper
   !huggingface-cli download openai/clip-vit-base-patch32 --local-dir checkpoints/clip

   # Настрой ngrok для дэшборда
   !python3.11 -m pip install pyngrok
   from pyngrok import ngrok
   ngrok.set_auth_token("твой_ngrok_токен")  # Получи на ngrok.com
   public_url = ngrok.connect(8000).public_url
   print(f"Дэшборд: {public_url}/static/index.html")

   # Запусти
   !python3.11 main.py
   ```

3. Открой дэшборд по ссылке `{public_url}/static/index.html`.

**Структура проекта**:
```
JarvisAI/
├── main.py
├── config.yaml
├── INSTRUCTIONS.md
├── requirements.txt
├── modules/
│   ├── text_processor.py
│   ├── vision_processor.py
│   ├── audio_processor.py
│   ├── device_control.py
│   ├── file_analyzer.py
│   ├── web_scraper.py
│   ├── memory_manager.py
│   ├── learning_manager.py
│   ├── personalization.py
│   ├── meta_learning.py
│   ├── scenario_modeler.py
│   ├── game_controller.py
│   ├── ethics_manager.py
│   ├── code_analyzer.py
│   ├── cognitive_engine.py
│   ├── physics_simulator.py
│   ├── security_manager.py
│   ├── multimodal_engine.py
│   ├── folder_monitor.py
│   ├── dialog_manager.py
│   ├── api_manager.py
│   ├── python_interpreter.py
│   ├── critical_thinking.py
│   ├── model_loader.py
│   ├── cloud_sync.py
│   ├── external_models.py
│   ├── search_engine.py
│   ├── unreal_bridge.py
│   ├── knowledge_clustering.py
│   ├── external/
├── models/
│   ├── text_model.py
│   ├── vision_model.py
│   ├── emotion_model.py
│   ├── physics_model.py
├── checkpoints/
├── data/
│   ├── input/
│   │   ├── learn/
│   │   ├── modify/
│   │   ├── analyze/
│   ├── output/
│   ├── dialogs/
│   ├── web_content/
│   ├── user_profile/
│   ├── knowledge/
│   ├── barriers/
│   ├── logs/
├── utils/
│   ├── tokenizer.py
│   ├── logger.py
│   ├── web_interface.py
│   ├── blockchain.py
│   ├── api_connector.py
│   ├── crypto.py
├── frontend/
│   ├── index.html
```

---

## 3. Обучение JarvisAI

JarvisAI учится автоматически или по твоим командам. Он использует RAG (поиск в знаниях) и кластеризацию для организации данных.

### Автоматическое обучение
1. **Через папки**:
   - Положи файлы (.txt, .pdf, .docx, .csv) в:
     - `data/input/learn/` — для обучения.
     - `data/input/modify/` — для изменения (например, формат).
     - `data/input/analyze/` — для анализа.
   - JarvisAI сам обработает файлы и обновит базу знаний (`data/knowledge/`).
   Пример: Скопируй `doc.txt` в `data/input/learn/`, и через пару секунд ИИ обучится.

2. **Через веб-дэшборд**:
   - Открой `http://localhost:8000/static/index.html`.
   - Введи: `учись data/input/learn/doc.txt`.
   - Ответ: "Обучился на файле doc.txt!"

3. **Через API**:
   ```bash
   curl -X POST -H "Content-Type: application/json" -d '{"prompt":"учись data/input/learn/doc.txt"}' http://localhost:8080/api/v1/text
   ```

### Обучение на веб-контенте
- Через дэшборд:
  - Введи: `учись https://example.com`
  - Ответ: "Обучился на сайте https://example.com!"
- Через API:
  ```bash
  curl -X POST -H "Content-Type: application/json" -d '{"prompt":"учись https://example.com"}' http://localhost:8080/api/v1/text
  ```

### Настройка обучения
- Измени параметры в `config.yaml`:
  ```yaml
  learning:
    thinking_depth: 3  # Глубина анализа (1-5)
    recursive_thinking: 9  # Рекурсивные шаги (1-20)
    auto_learn: true  # Автообучение
    clustering_enabled: true  # Кластеризация знаний
  ```
- Через дэшборд:
  - Введи: `настрой обучение сколько раз думать 5`
  - Ответ: "thinking_depth: 5, recursive_thinking: 9"

---

## 4. Интеграция

### Unreal Engine
1. Установи Unreal Engine (4.27 или 5.x) и укажи путь в `config.yaml`:
   ```yaml
   unreal_config:
     engine_path: "/path/to/UnrealEngine"
   ```
2. Генерируй ассеты:
   - Через дэшборд: `сгенерируй blueprint для куба`
   - Через API:
     ```bash
     curl -X POST -H "Content-Type: application/json" -d '{"prompt":"сгенерируй blueprint для куба"}' http://localhost:8080/api/v1/text
     ```
   - Результат: `data/output/unreal_blueprint_2025-04-17.py`

### Устройства (IoT)
- Подключи устройства через MQTT (брокер: `broker.hivemq.com`).
- Пример команды:
  - Через дэшборд: `включи лампу device_123`
  - Через API:
    ```bash
    curl -X POST -H "Content-Type: application/json" -d '{"prompt":"включи лампу device_123"}' http://localhost:8080/api/v1/text
    ```

### Облако
- Настрой AWS S3 для синхронизации знаний:
  - В `config.yaml`:
    ```yaml
    cloud_config:
      provider: "aws"
      bucket: "jarvisai-backup"
    ```
  - Укажи AWS-ключи в переменных окружения:
    ```bash
    export AWS_ACCESS_KEY_ID="твой_ключ"
    export AWS_SECRET_ACCESS_KEY="твой_секрет"
    ```
  - Знания автоматически синхронизируются каждые 3600 секунд.

### Внешние API
- Используй SerpAPI для поиска:
  - Зарегистрируйся на [serpapi.com](https://serpapi.com).
  - Укажи ключ в `config.yaml`:
    ```yaml
    search_config:
      serpapi_key: "твой_ключ"
    ```

---

## 5. Использование

### Текстовые команды
- Через дэшборд:
  - Введи: `привет, Джарвис`
  - Ответ: "Привет! Чем могу помочь?"
- Через API:
  ```bash
  curl -X POST -H "Content-Type: application/json" -d '{"prompt":"привет, Джарвис"}' http://localhost:8080/api/v1/text
  ```

### Голосовые команды
- Запиши аудио (например, `command.wav`) и положи в `data/input/`.
- Через API:
  ```bash
  curl -X POST -H "Content-Type: application/json" -d '{"action":"voice_command", "audio_path":"data/input/command.wav"}' http://localhost:8080/api/v1/audio
  ```
- Ответ: Например, "Обучился на файле doc.txt!" (если сказано "учись doc.txt").

### Обработка видео
- Положи видео (`video.mp4`) в `data/input/modify/`.
- Через дэшборд: `измени data/input/modify/video.mp4 добавь субтитры`
- Через API:
  ```bash
  curl -X POST -H "Content-Type: application/json" -d '{"prompt":"измени data/input/modify/video.mp4 добавь субтитры"}' http://localhost:8080/api/v1/text
  ```
- Результат: `data/output/modified_video_2025-04-17.mp4`

### Генерация кода
- Через дэшборд: `запустить код print("Hello, World!")`
- Через API:
  ```bash
  curl -X POST -H "Content-Type: application/json" -d '{"code":"print(\"Hello, World!\")"}' http://localhost:8080/api/v1/code
  ```
- Ответ: "Hello, World!"

### Поиск
- Через дэшборд: `поиск квантовые компьютеры`
- Через API:
  ```bash
  curl -X POST -H "Content-Type: application/json" -d '{"prompt":"поиск квантовые компьютеры"}' http://localhost:8080/api/v1/text
  ```
- Ответ: "Квантовые компьютеры используют кубиты для..."

---

## 6. Внедрение

### В свои проекты
1. **API**:
   - Используй REST API для интеграции:
     - Текст: `POST /api/v1/text`
     - Изображения: `POST /api/v1/image`
     - Аудио: `POST /api/v1/audio`
     - Код: `POST /api/v1/code`
   - Пример (Python):
     ```python
     import requests
     response = requests.post("http://localhost:8080/api/v1/text", json={"prompt": "привет, Джарвис"})
     print(response.json())
     ```

2. **Веб-дэшборд**:
   - Расширь `frontend/index.html` (React/Tailwind) под свои нужды.
   - Добавь новые виджеты для задач, статистики, управления.

3. **Модули**:
   - Используй модули (`text_processor.py`, `vision_processor.py`) как библиотеки:
     ```python
     from modules.text_processor import TextProcessor
     text_processor = TextProcessor(config["text_model"], device, ...)
     response = await text_processor.process("привет")
     ```

### Масштабирование
- **Облако**:
  - Разверни на AWS/GCP с помощью Docker:
    ```bash
    docker build -t jarvisai .
    docker run -p 8000:8000 -p 8080:8080 jarvisai
    ```
  - Настрой автоскейлинг для API.
- **Кластер**:
  - Используй Kubernetes для распределенного обучения моделей.
- **Больше моделей**:
  - Добавь LLaMA-13B или GPT-4 в `external_models.py`.

---

## 7. Полезные советы

### Оптимизация
- **GPU**: Используй GPU с ≥8 ГБ VRAM для ускорения моделей.
- **Квантование**: В `config.yaml` включи `quantization: true` для экономии памяти.
- **LoRA**: `lora: true` ускоряет обучение на новых данных.
- **CPU**: Если нет GPU, включи `optimize_cpu: true`.

### Устранение ошибок
- **Модели не грузятся**:
  - Проверь пути в `config.yaml`.
  - Убедись, что `checkpoints/` содержит модели.
- **Ошибки зависимостей**:
  - Переустанови: `pip install -r requirements.txt --no-cache-dir`
- **Colab отключается**:
  - Перейди на Colab Pro или запускай локально.
- **API не отвечает**:
  - Проверь порт: `lsof -i :8080`
  - Перезапусти: `python main.py`

### Безопасность
- Храни `security_key` и `serpapi_key` в секрете.
- Регулярно обновляй `data/barriers/barriers.json` для этических ограничений.
- Используй шифрование (`utils/crypto.py`) для данных.

---

## 8. Что дальше?

JarvisAI готов к работе! Ты можешь:
- Добавить новые модели (например, LLaMA-13B).
- Расширить дэшборд (новые виджеты, графики).
- Настроить CI/CD на GitHub Actions.
- Интегрировать с другими платформами (Discord, Telegram).

Если что-то не работает, пиши в Issues на GitHub или проверяй логи в `data/logs/`. JarvisAI — твой личный ИИ, и ты его хозяин! 🚀

*Создано: 17 апреля 2025*
