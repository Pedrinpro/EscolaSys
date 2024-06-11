@echo off
color 1
echo SETUP
echo Contato para erros e sugestoes [+55 21-99885-7949]
color 0
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python não encontrado. Instalando Python...
    set /p P="Deseja instalar o Python? [S/N]: "
    if /i "%P%"=="S" (
        winget install --id=Python.Python -e
        python --version >nul 2>&1
        if %errorlevel% neq 0 (
            echo Falha ao instalar o Python. Certifique-se de ter o winget instalado e tente instalar manualmente.
            pause
            exit /b
        )
    ) else (
        exit
    )
)

echo Python encontrado. Continuando com o script...

set /p O="Deseja prosseguir? [S/N]: "

if /i "%O%"=="S" (
    pip install colorama -q -U
    pip install tabulate -q -U
    pip install sqlite3 -q -U 
    echo Finalizado
    pause
) else (
    exit
)
