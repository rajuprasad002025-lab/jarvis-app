<html>
<style>
   div{min-height:1em;}
</style>
<body>[app]<br/><br/># (str) Title of your application<br/>title = Jarvis<br/><br/># (str) Package name<br/>package.name = jarvis<br/><br/># (str) Package domain (needed for android packaging)<br/>package.domain = org.jarvis<br/><br/># (list) Source files to include (let it empty to include all files)<br/>source.include_exts = py,png,jpg,kv,atlas<br/><br/># (list) Application requirements<br/># comma separated e.g. requirements = python3,kivy<br/>requirements = python3,kivy,gtts,pyjnius<br/><br/># (str) Supported orientations<br/>orientation = portrait<br/><br/># (list) Permissions<br/># Give internet access and audio recording for voice features<br/>android.permissions = INTERNET,RECORD_AUDIO<br/><br/>[buildozer]<br/><br/># (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))<br/>log_level = 2<br/></body>
</html>