@prompt $G
@cd /d "%~dp0"
del /s /q dist
pyinstaller --onefile --windowed --icon=fnfo.ico -y -n FNFOriginizer gui.py
copy logo.gif dist\
@pause