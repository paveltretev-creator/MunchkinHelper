[app]
title = Munchkin Helper
package.name = munchkinhelper
package.domain = org.munchkinhelper

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,ttf,md,txt,json
version = 1.0.0
entrypoint = android_entry.py

# ОСТАВЛЯЕМ ТОЛЬКО KIVY И REQUESTS (без pydantic, cryptography, sqlalchemy)
requirements = python3,kivy==2.3.0,requests

orientation = landscape
fullscreen = 0
log_level = 2

android.permissions = INTERNET,ACCESS_NETWORK_STATE
android.api = 33
android.minapi = 21
android.ndk = 25b
p4a.android_api = 33
p4a.ndk = 25b
android.archs = arm64-v8a
p4a.branch = master

[buildozer]
build_dir = ./.buildozer
bin_dir = ./bin
log_level = 2