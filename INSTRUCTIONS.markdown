# JarvisAI: Инструкции по использованию

JarvisAI — твой локальный ИИ, сравнимый с Grok 3 и GPT-4. Он обрабатывает текст, голос, видео, код, генерирует картинки, ищет в интернете с DeepSearch, управляет устройствами, создаёт ассеты для Unreal Engine и автоматически учится. Этот гид поможет тебе установить, использовать и прокачать ИИ. Всё просто, даже для новичков!

---

## 1. Что такое JarvisAI?

JarvisAI — твой личный ИИ, работающий на компе или в Google Colab. Он:

- **Мультимодальный**: Текст, голос, видео, картинки, код.
- **Самообучаемый**: Учится на файлах, вебе, через API.
- **Умный поиск**: DeepSearch для точных результатов.
- **Интуитивный**: Управляй через дэшборд, API, папки.
- **Гибкий**: Интеграция с Unreal Engine, IoT, облаком.
- **Безопасный**: Локальные данные, шифрование, этика.

**Возможности**:

- Генерация текста, кода, картинок (Stable Diffusion).
- DeepSearch: итеративный поиск в интернете.
- Распознавание и синтез речи с диалоговым контекстом.
- Обработка видео (субтитры, укорачивание).
- Автообучение на веб-данных.
- Управление устройствами (MQTT).
- Генерация ассетов для Unreal Engine (Blueprint, меши).
- REST API и веб-дэшборд.

---

## 2. Установка

### Локальный компьютер

1. **Проверь Python**: Убедись, что есть Python 3.11.6:

   ```bash
   python --version
   ```

   Нет? Скачай с python.org.

2. **Установи Git**:

   ```bash
   # MacOS
   brew install git
   # Linux
   sudo apt-get install git
   # Windows: скачай с git-scm.com
   ```

3. **Клонируй репозиторий**:

   ```bash
   git clone https://github.com/TidesLuck/JarvisAI.git
   cd JarvisAI
   ```

4. **Создай виртуальное окружение**:

   ```bash
   python -m venv jarvisai_env
   source jarvisai_env/bin/activate  # Linux/MacOS
   jarvisai_env\Scripts\activate     # Windows
   ```

5. **Установи зависимости**:

   ```bash
   pip install -r requirements.txt
   pip install diffusers==0.21.4 transformers==4.33.2 speechrecognition==3.10.0 pyttsx3==2.90
   ```

6. **Установи FFmpeg**:

   ```bash
   # MacOS
   brew install ffmpeg
   # Linux
   sudo apt-get install ffmpeg
   # Windows: скачай с ffmpeg.org, добавь в PATH
   ```

7. **Скачай модели**:

   ```bash
   pip install huggingface_hub
   huggingface-cli download meta-llama/Llama-2-7b --local-dir checkpoints/llama
   huggingface-cli download openai/whisper-large --local-dir checkpoints/whisper-large
   huggingface-cli download openai/clip-vit-base-patch32 --local-dir checkpoints/clip
   huggingface-cli download stabilityai/stable-diffusion-2-1 --local-dir checkpoints/sd
   ```

8. **Настрой** `config.yaml`:

   - Открой `config.yaml`.
   - Укажи:
     - `security_key`: Любой секретный ключ.
     - `serpapi_key`: Получи на serpapi.com.
     - `unreal_config.engine_path`: Путь к Unreal Engine (если используешь).
     - Проверь пути к моделям (`checkpoints/llama`, `checkpoints/whisper-large`, `checkpoints/clip`, `checkpoints/sd`).

9. **Запусти**:

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

**Структура проекта**:

```
JarvisAI/
├── main.py
├── config.yaml
├── README.md
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
│   ├── image_generator.py
│   ├── auto_learn.py
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
│   │   ├── barriers.json
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

### Автоматическое обучение

1. **Через папки**:

   - Положи файлы (.txt, .pdf, .docx) в `data/input/learn/`.
   - JarvisAI сам обработает и сохранит знания в `data/knowledge/`.
   - Пример: Скопируй `doc.txt` в `data/input/learn/`.

2. **Через веб-дэшборд**:

   - Открой `http://localhost:8000/static/index.html`.
   - Введи: `учись data/input/learn/doc.txt`.
   - Ответ: "Обучился на файле doc.txt!"

3. **Через API**:

   ```bash
   curl -X POST -H "Content-Type: application/json" -d '{"prompt":"учись data/input/learn/doc.txt"}' http://localhost:8080/api/v1/text
   ```

4. **Автообучение**:

   - Запусти: `python modules/auto_learn.py --topic "artificial intelligence"`
   - Или через дэшборд: `учись искусственный интеллект`.
   - Знания сохраняются в `data/knowledge/artificial_intelligence.json`.

### Обучение на веб-контенте

- Через дэшборд: `учись https://example.com`

- Через API:

  ```bash
  curl -X POST -H "Content-Type: application/json" -d '{"prompt":"учись https://example.com"}' http://localhost:8080/api/v1/text
  ```

### Настройка

- В `config.yaml`:

  ```yaml
  learning:
    thinking_depth: 10
    recursive_thinking: 20
    auto_learn: true
    clustering_enabled: true
  ```

---

## 4. Использование

### Текстовые команды

- Через дэшборд: `привет, Джарвис` → "Привет! Чем могу помочь?"

- Через API:

  ```bash
  curl -X POST -H "Content-Type: application/json" -d '{"prompt":"привет, Джарвис"}' http://localhost:8080/api/v1/text
  ```

### DeepSearch

- Через дэшборд: `поиск квантовые компьютеры`

- Через API:

  ```bash
  curl -X POST -H "Content-Type: application/json" -d '{"prompt":"поиск квантовые компьютеры"}' http://localhost:8080/api/v1/text
  ```

- Ответ: Точные результаты с уточнением запросов.

### Голосовые команды

- Запиши аудио (`command.wav`) в `data/input/`.

- Через API:

  ```bash
  curl -X POST -H "Content-Type: application/json" -d '{"action":"voice_command", "audio_path":"data/input/command.wav"}' http://localhost:8080/api/v1/audio
  ```

- Потоковое распознавание:

  ```bash
  curl -X POST -H "Content-Type: application/json" -d '{"action":"stream"}' http://localhost:8080/api/v1/audio
  ```

- Синтез речи:

  ```bash
  curl -X POST -H "Content-Type: application/json" -d '{"action":"synthesize", "audio_path":"Hello"}' http://localhost:8080/api/v1/audio
  ```

### Генерация картинок

- Через дэшборд: `сгенерируй картинку кота в космосе`

- Through API:

  ```bash
  curl -X POST -H "Content-Type: application/json" -d '{"prompt":"сгенерируй картинку кота в космосе"}' http://localhost:8080/api/v1/image
  ```

- Результат: `data/output/generated_image.png`

### Обработка видео

- Положи `video.mp4` в `data/input/modify/`.

- Через дэшборд: `измени data/input/modify/video.mp4 добавь субтитры`

- Through API:

  ```bash
  curl -X POST -H "Content-Type: application/json" -d '{"prompt":"измени data/input/modify/video.mp4 добавь субтитры"}' http://localhost:8080/api/v1/text
  ```

### Генерация кода

- Через дэшборд: `запустить код print("Hello, World!")`

- Through API:

  ```bash
  curl -X POST -H "Content-Type: application/json" -d '{"code":"print(\"Hello, World!\")"}' http://localhost:8080/api/v1/code
  ```

### Unreal Engine

- Через дэшборд: `сгенерируй blueprint для куба`

- Through API:

  ```bash
  curl -X POST -H "Content-Type: application/json" -d '{"prompt":"сгенерируй blueprint для куба"}' http://localhost:8080/api/v1/text
  ```

### Управление устройствами

- Через дэшборд: `включи лампу device_123`

- Through API:

  ```bash
  curl -X POST -H "Content-Type: application/json" -d '{"prompt":"включи лампу device_123"}' http://localhost:8080/api/v1/text
  ```

---

## 5. Интеграция

### API

- Текст: `POST /api/v1/text`

- Картинки: `POST /api/v1/image`

- Аудио: `POST /api/v1/audio`

- Код: `POST /api/v1/code`

- Пример (Python):

  ```python
  import requests
  response = requests.post("http://localhost:8080/api/v1/text", json={"prompt": "привет, Джарвис"})
  print(response.json())
  ```

### Unreal Engine

- Укажи путь в `config.yaml`:

  ```yaml
  unreal_config:
    engine_path: "/path/to/UnrealEngine"
  ```

### Облако

- Настрой AWS S3 в `config.yaml`:

  ```yaml
  cloud_config:
    provider: "aws"
    bucket: "jarvisai-backup"
  ```

---

## 6. Полезные советы

### Оптимизация

- **GPU**: ≥16 ГБ VRAM для Stable Diffusion и LLaMA.
- **Квантование**: `quantization: true` в `config.yaml`.
- **LoRA**: `lora: true` для быстрого обучения.

### Устранение ошибок

- **Модели не грузятся**: Проверь пути в `config.yaml`.
- **Ошибки зависимостей**: `pip install -r requirements.txt --no-cache-dir`
- **API не отвечает**: `lsof -i :8080`, затем перезапусти `python main.py`.

### Безопасность

- Храни `security_key` и `serpapi_key` в секрете.
- Репозиторий приватный, не дели доступ.

---

## 7. Что дальше?

JarvisAI готов к работе и сравним с Grok 3 и GPT-4! Ты можешь:

- Добавить LLaMA-3-70B для большей мощи.
- Расширить дэшборд (`frontend/index.html`).
- Настроить автообучение на X/Twitter.
- Развернуть на AWS с Docker.

Проблемы? Читай логи в `data/logs/` или пиши в Issues на GitHub. JarvisAI — твой ИИ, рули им! 🚀

*Создано: 17 апреля 2025*