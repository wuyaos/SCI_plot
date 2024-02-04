@echo off
chcp 65001

title sci_plot包安装

@REM 执行 activate.bat 会打开一个新的 cmd 窗口，所以这里使用 call 命令
@REM call C:\virtualenv\xxx\Scripts\activate.bat

echo ****进入目录****
echo %~dp0
cd /d %~dp0

echo ****获取当前用户文件夹****
for /f "delims=" %%i in ('echo %USERPROFILE%') do set "user_profile=%%i"
echo %user_profile%

echo ****复制文件到用户文件夹****
set "source_folder=%~dp0sci_plot\.matplotlib"
set "destination_folder=%user_profile%\.matplotlib\"

if not exist "%destination_folder%\*" (
    xcopy "%source_folder%" "%destination_folder%" /s /i
) else (
    choice /M "目标文件夹已存在。是否要覆盖？"
    if errorlevel 2 goto end
    xcopy "%source_folder%" "%destination_folder%" /s /i /y
)
:end

echo ****安装字体****
echo A^|copy "%~dp0sci_plot\fonts\TimesSong.ttf" "%windir%\Fonts\TimesSong.ttf"

echo ****安装sci_plot包****
pip install .

@REM @REM 复制文件到用户文件夹
@REM copy "C:\virtualenv\xxx\Lib\site-packages\pymysql\cursors.py" "%user_profile%\.pymysql\cursors.py"

pause