@echo off 

set path_script=D:\Dougall\Work\STC\Dissem\WFH_COVID\DAT\scripts\ui
set path_view=D:\Dougall\Work\STC\Dissem\WFH_COVID\DAT\app\view


for %%f in (%path_view%\*.ui) do (
%path_script%\pyuic5.bat -x %%f -o %%~df%%~pf%%~nf.py
)


