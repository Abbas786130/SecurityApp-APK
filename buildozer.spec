[app]

# (str) Title of your application
title = SecurityApp

# (str) Package name
package.name = securityapp

# (str) Package domain (used for Android package name)
package.domain = org.abbas.security

# (str) Source code where the main.py lives
source.dir = .

# (str) Application version
version = 1.0

# (str) Application entry point
entrypoint = main.py

# (list) Permissions
android.permissions = CAMERA, INTERNET

# (str) Supported orientation (portrait, landscape, all, sensor)
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (list) List of inclusions using pattern matching
source.include_exts = py,png,jpg,kv,tflite

# (str) Presplash of the application
presplash.filename = %(source.dir)s/data/presplash.png

# (list) Application requirements
requirements = python3, kivy, numpy, opencv-python, tensorflow

# (str) Custom source folders for requirements
# (list) Garden requirements
#garden_requirements = 

# (str) Android NDK API level
android.ndk_api = 21

# (int) Target API
android.api = 31

# (str) Bootstrap to use (sdl2 or webview)
bootstrap = sdl2

# (str) Android archs
android.archs = arm64-v8a, armeabi-v7a

# (bool) Copy library instead of making a libpymodules.so
copy_libs = 1

# (bool) Use --private data storage (True) or --dir public storage (False)
android.private_storage = True

# (bool) Package as an APK file
android.packaging = apk

# (str) Android logcat filters to use
android.logcat_filters = *:S python:D

# (str) Path to icon
icon.filename = %(source.dir)s/icon.png

# (str) Supported screens
android.supported_screens = small, normal, large, xlarge

# (bool) Enable Android x86 builds (not needed for most apps)
# android.archs = armeabi-v7a, x86

# (bool) Include Android native libraries (*.so)
# android.add_libs_armeabi-v7a = libs/android/*.so

# (str) Key alias to use for signing
# android.keyalias = mykey

# (str) Keyalias password
# android.keyalias_password = password

# (str) Key password
# android.keypassword = password

# (str) Path to keystore
# android.keystore = debug.keystore

# (list) Java .jar files to add to the libs dir for inclusion in the APK
# android.add_jars = customjar.jar

# (list) Python files to include (in addition to all from source.dir)
# include_exts = py

# (list) Assets to be included in apk
# android.add_assets = assets/

# (str) Custom source folders for requirements
# (list) Extra dependencies for requirements
# requirements.source = path/to/lib

# (str) Custom Java class path
# android.add_src = src

# (bool) Whether to include test apps
# test = 0

