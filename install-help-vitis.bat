@echo off & cls
if not "%minimized%"=="" goto :minimized
set minimized=true
start /min cmd /C "%~dpnx0"
goto :EOF
:minimized
mode 75,40
powershell (New-Object -ComObject Wscript.Shell).Popup("""This utility copies the webhelp files to the recommended location so that you can access the help from within the Vitis IDE.`n`nClick OK to continue.""",0,"""Accessing Vitis Environment Help Content""",0x0)
powershell (New-Object -ComObject Wscript.Shell).Popup("""Click OK to copy the help files to %UserProfile%\.Xilinx\Vitis\2024.1\helpdocs\vitis""",0,"""Accessing Vitis Environment Help Content""",0x0)
XCOPY /E/Y *.* "%UserProfile%\.Xilinx\Vitis\2024.1\helpdocs\vitis"
cd "%UserProfile%\.Xilinx\Vitis\2024.1\helpdocs\vitis"
DEL *.bat
powershell (New-Object -ComObject Wscript.Shell).Popup("""Operation Completed!`n`nYou can now access the Vitis Environment Help from within the Vitis IDE. `n`nLaunch the SDx IDE and select Help `> Vitis Help `> Vitis Help to view the help files.""",0,"""Accessing Vitis Environment Help Content""",0x0)