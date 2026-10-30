[app]
title = Munchkin Helper
package.name = munchkinhelper
package.domain = org.munchkinhelper

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,ttf,md,txt,json
version = 1.0.0

entrypoint = android_entry.py

requirements = python3,kivy==2.3.0,sqlalchemy==2.0.29,pg8000==1.30.2,pydantic==2.6.2,pydantic-settings==2.2.1,cryptography==42.0.5,passlib==1.7.4,bcrypt==4.1.2,typing-extensions

orientation = landscape
fullscreen = 0
log_level = 2
warn_on_root = 0

# ЖЕСТКАЯ ФИКСАЦИЯ ВЕРСИЙ (Критически важно для обхода ошибки)
android.api = 33
android.minapi = 21
android.ndk = 25b
p4a.android_api = 33
p4a.ndk = 25b

android.permissions = INTERNET,ACCESS_NETWORK_STATE,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE
android.archs = arm64-v8a, armeabi-v7a
p4a.branch = master

[buildozer]
build_dir = ./.buildozer
bin_dir = ./bin
log_level = 2