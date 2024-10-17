@echo off

set path=d:\lib\FPC\3.2.2\bin\i386-win32;%path%
set path=d:\lib\fpcwasm\bin\i386-win32;%path%

fpc YASS.pas && YASS.exe -inline "    #####       " "    #   #       " "  ###  $###     " "  #  $    #     " "### # ##  ######" "#   # ##$ #  ..#" "# $   $   $  ..#" "##### ### #  ..#" "    #  @  ######" "    #######     "

if %ERRORLEVEL% NEQ 0 exit %ERRORLEVEL%

ppcrosswasm32.exe YASS.pas

if %ERRORLEVEL% NEQ 0 exit %ERRORLEVEL%

rem copy /y YASS_loader.js ..\..\js
copy /y YASS.wasm ..\..\js

rem call clean.cmd
