@echo off
echo Installing PyShot...

echo Copying to startup...
copy /-y "PyShot.exe" "C:\Users\%username%\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup"

echo Starting...
start "" "C:\Users\%username%\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\PyShot.exe"

echo PyShot should now be installed and running. If not your system may be incompatable
pause