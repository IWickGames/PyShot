@echo off
echo Uninstalling PyShot...

echo Stopping Process...
taskkill /im PyShot.exe /f >nul

echo Removing PyShot from startup...
del /q /f "C:\Users\%username%\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\PyShot.exe"

echo PyShot was uninstalled successfully!
pause