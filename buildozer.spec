[app]
title = Munchkin Helper
package.name = munchkinhelper
package.domain = org.munchkinhelper

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,ttf,md,txt,json
version = 1.0.0

entrypoint = android_entry.py

requirements = python3,kivy==2.3.0,sqlalchemy==2.0.29,pg8000==1.30.2,pydantic==2.6.2,pydantic-settings==2.2.1,passlib==1.7.4,bcrypt==4.1.2,typing-extensions

orientation = landscape
fullscreen = 0

android.permissions = INTERNET,ACCESS_NETWORK_STATE,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

android.minapi = 21
android.targetapi = 33
android.compileapi = 33
android.archs = arm64-v8a

# Используем master ветку p4a — там исправлены многие проблемы
p4a.branch = master
p4a.source_dir = 

log_level = 2
warn_on_root = 0

[buildozer]
build_dir = ./.buildozer
bin_dir = ./bin