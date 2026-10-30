[app]
title = Munchkin Helper
package.name = munchkinhelper
package.domain = org.munchkinhelper

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,ttf,md,txt,json
version = 1.0.0

# Точка входа — адаптированный скрипт
entrypoint = android_entry.py

# Все зависимости для Android
# pg8000 вместо psycopg2 — чистый Python, работает на Android
requirements = python3,kivy==2.3.0,sqlalchemy==2.0.29,pg8000==1.30.2,pydantic==2.6.2,pydantic-core==2.16.3,pydantic-settings==2.2.1,cryptography==42.0.5,passlib==1.7.4,bcrypt==4.1.2,typing-extensions==4.10.0,annotated-types==0.6.0

# Ориентация экрана — горизонтальная, как в десктопной версии
orientation = landscape

# Не полноэкранный (чтобы видеть системные кнопки)
fullscreen = 0

# Разрешения — доступ к интернету для подключения к PostgreSQL
android.permissions = INTERNET,ACCESS_NETWORK_STATE

# API уровни
android.minapi = 21
android.targetapi = 33
android.compileapi = 33

# Архитектуры
android.archs = arm64-v8a, armeabi-v7a

# Версия Android NDK
p4a.branch = master

# Логирование
log_level = 2
warn_on_root = 0

# Размер окна для десктопных тестов
# window.size = 1280,720

[buildozer]
build_dir = ./.buildozer
bin_dir = ./bin