[app]

# (str) Title of your application
title = Jarvis

# (str) Package name
package.name = jarvis

# (str) Package domain (needed for android packaging)
package.domain = org.jarvis

# (str) Source directory where your application source files are stored
source.dir = .

# (str) Version of your application
version = 0.1

# (list) Source files to include (let it empty to include all files)
source.include_exts = py,png,jpg,kv,atlas

# (list) Source files to exclude (let it empty to exclude nothing)
source.exclude_exts = spec

# (list) List of inclusion patterns
source.include_patterns = assets/*,images/*.png

# (list) Application requirements
requirements = python3,kivy

# (str) Supported orientations
orientation = portrait

# (list) Permissions
android.permissions = INTERNET

# (int) Target Android API, should be as high as possible
android.api = 33

# (bool) Automatically accept SDK licenses
android.accept_sdk_license = True

[buildozer]
log_level = 2
