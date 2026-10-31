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
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,kivy

# (str) Supported orientations
orientation = portrait

# (list) Permissions
android.permissions = INTERNET

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2
