[app]
# Название приложения
title = Munchkin Helper

# Package name (только латиница, цифры и подчеркивания)
package.name = munchkinhelper

# Package domain (домен автора в обратном порядке)
package.domain = org.munchkinhelper

# Исходная директория
source.dir = .

# Расширения файлов, которые будут включены в APK
source.include_exts = py,png,jpg,kv,atlas,ttf,md,txt,json

# Версия приложения
version = 1.0.0

# Точка входа (адаптированный скрипт для Android)
entrypoint = android_entry.py

# Python-зависимости
# pg8000 — чистый Python драйвер PostgreSQL (работает на Android)
# cryptography — для шифрования сессий
# passlib + bcrypt — для хеширования паролей
requirements = python3,kivy==2.3.0,sqlalchemy==2.0.29,pg8000==1.30.2,pydantic==2.6.2,pydantic-settings==2.2.1,cryptography==42.0.5,passlib==1.7.4,bcrypt==4.1.2,typing-extensions

# Ориентация экрана (горизонтальная, как в десктопной версии 1280x720)
orientation = landscape

# Не полноэкранный режим (чтобы видеть системные кнопки)
fullscreen = 0

# Уровень логирования (0-2)
log_level = 2

# Предупреждать о запуске от root (0 — не предупреждать)
warn_on_root = 0

# Android настройки
# API уровень целевого Android
android.api = 33

# Минимальный поддерживаемый API
android.minapi = 21

# Версия NDK
android.ndk = 25b

# Разрешения Android
# INTERNET — обязательно для подключения к PostgreSQL
# ACCESS_NETWORK_STATE — проверка наличия сети
# WRITE/READ_EXTERNAL_STORAGE — для сохранения сессии
android.permissions = INTERNET,ACCESS_NETWORK_STATE,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

# Архитектуры (arm64-v8a для современных устройств)
android.archs = arm64-v8a, armeabi-v7a

# Ветка python-for-android
p4a.branch = master

[buildozer]
# Директория для временных файлов сборки
build_dir = ./.buildozer

# Директория для готовых APK
bin_dir = ./bin

# Уровень логирования buildozer
log_level = 2