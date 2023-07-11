[app]

# (required) Title of your application
title = StationsApp

# (optional) Package name
package.name = StationsApp

# (optional) Package domain (needed for android/ios packaging)
package.domain = com.mycompany.StationsApp

# (optional) Source code where the main.py live
source.dir = .

# (optional) Icon of the application
icon.filename = free-icon-subway-entrance-3720614.png

# (optional) Supported orientation (one of landscape, sensorLandscape,
# portrait or all)
orientation = portrait

# (optional) Version code of your application
# A custom version code is useful when updating the application with new
# features. You can define any string value, as long as it is unique across
# your application history. It's not recommended to use a date-based version
# code (YYMMDDHH), because version codes can't be downgraded and you may want
# to publish a bugfix update to users of an older version.
version.code = 1

# (optional) Version name of your application
version.name = 0.1
version.filename = myapp-{version.name}-debug.apk

# (optional) Version regex of your application
# This is used to extract the version information from the filename.
version.regex = myapp-(\\d+\\.\\d+)-debug.apk
# (optional) Application description
description = My Awesome App

# (optional) Application author (could be multiple)
author = GalkinAndTyulyaev

# (optional) Application author email (for multiple authors, separate them by comma)
author.email = nikson6911@mail.ru

# (optional) Application author website (for multiple authors, separate them by comma)
author.website = https://www.example.com

# (optional) Permissions
android.permissions = INTERNET

# (optional) Services
android.services =

# (optional) Receivers
android.receivers =

# (optional) Application meta-data
# android.meta_data = key=value

# (optional) Data files (no need to list .kv files or images already listed
# in `source`)
# Add as many as you want, one per line. You can use your local file system
# or urls.
# data_files =

# (optional) Presplash of the application
# presplash.filename = %(source.dir)s/data/presplash.png

# (optional) Splash image of the application
# (place it in the same directory as the .spec file, or specify full path)
# splash.filename = %(source.dir)s/data/splash.png

# (optional) The hash sum of the source python package
# (default to md5, can be 'sha1' or 'sha512')
source.hash_method = md5

# (optional) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = kivy

# (optional) List of additional pypi dependencies to install (let empty to
# install nothing)
# pypi.whitelist =

# (optional) Application build directory (default is .buildozer)
build.dir = .buildozer

# (optional) Set the target device to install app, default armeabi-v7a
#target = armeabi-v7a

# (optional) Python for android distribution to use, defaults to latest
# available stable if not set, you can set it to "sdk" to use the android SDK
# standalone distribution instead
#python-for-android =

# (optional) Space-separated list of Java classes to add as activities to the
# manifest.
#android.add_activites = com.example.ExampleActivity

# (optional) Space-separated list of Java classes to add as services to the
# manifest.
#android.add_services = com.example.ExampleService

# (optional) Application needs to be fullscreen
#fullscreen = 1

[buildozer]

# (optional) Path to build artifact storage, absolute or relative to spec file
# build_dir = /path/to/build/dir

# (optional) Path to build output (i.e. .apk, .ipa) storage
# bin_dir = /path/to/bin/dir

#    * android
#
# (required) Path to the android ndk
# android.ndk_path = /path/to/android/ndk

# (required) Path to the android sdk
# android.sdk_path = /path/to/android/sdk

# (optional) Android app armeabi-v7a architecture
android.arch = armeabi-v7a

# (optional) Android app x86 architecture
android.x86 = False

# (optional) Android app ARM64-v8a architecture
android.arm64-v8a = False

# (optional) Android app x86_64 architecture
android.x86_64 = False

# (optional) Python interpreter to use for building the application
# defaults to the first one found in the PATH if not set
# python_version = 3.8.6

# (optional) The name of the python-for-android dist to use, defaults to the
# latest stable version available
# dist_name = mydist

# (optional) If set, it will be used to specify custom source folders
# source.include_exts = py,png,jpg,kv,atlas

# (optional) If set, it will be used to specify custom source folders
# source.include_patterns = assets/*,images/*.png

# (optional) If set, it will be used to exclude patterns from the source folder
# source.exclude_patterns = license,images/*/*.jpg

# (optional) Application configuration to build
# settings =

# (optional) List of source files to include in the .apk, for native builds only
# (the default includes everything in the app/ directory)
#android.app_source_dirs =

# (optional) List of Java classes to include in the .apk alongside the compiled
# python bytecode, for native builds only
#android.add_javaclass_dir =

# (optional) List of Java .jar files to include in the .apk alongside the
# compiled python bytecode, for native builds only
#android.add_jars = foo.jar,bar.jar,path/to/more/*.jar

# (optional) Obfuscate Python bytecode (experimental)
#obfuscate = False

# (optional) Sign the built .apk
# False (default) means don't sign
# True means sign with the default key (recommended)
# Or specify a custom keystore to use
#sign = False
#keystore = /path/to/keystore
#alias = myalias
#storepass = mykeypass
#keypass = mykeypass

# (optional) Android logcat filters to use
#android.logcat_filters = *:S python:D

# (optional) Android additional libraries to include
#android.library_references = com.android.support:appcompat_v7:27.1.1

# (optional) Android build flags to use when compiling the pyjnius module
#android.pyjnius.build_flags =

# (optional) Android AAR archives to include, supports jnius, plyer and any
# library that includes an AAR file in its package.
#android.aars =

# (optional) Gradle dependencies to add (currently for android only)
#gradle_dependencies =

# (optional) Compile python files to bytecode using python compileall module
#python_compile = true

# (optional) Enables Android's hidden API access
# Warning: this capability is in beta mode and may cause crashes or other issues
# when used. Use at your own risk.
#android.experimental_hidden_api = false