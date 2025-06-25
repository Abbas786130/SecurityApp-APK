[app]
# (str) Title of your application
title = SecurityApp
# (str) Package name (must be unique! use your domain reversed)
package.name = securityapp
package.domain = org.abas

# (list) Source file extensions to include
source.include_exts = py,tflite

# (list) Application requirements
requirements = python3,kivy,opencv-python,numpy,tensorflow

# (str) Permissions
android.permissions = INTERNET,CAMERA,READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE

# (int) Android API to use
android.api = 31
android.minapi = 21
android.ndk = 23b

# (bool) Copy libraries instead of linking
copy_libraries = 1
