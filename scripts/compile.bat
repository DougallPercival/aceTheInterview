@echo off 
setlocal

set path_script=%~dp0
set path_view=%~dp0..\ui


for %%f in (%path_view%\*.ui) do (
%path_script%\pyuic5.bat -x %%f -o %%~df%%~pf%%~nf.py
)


