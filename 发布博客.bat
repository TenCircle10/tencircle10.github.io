@echo off
chcp 65001 >nul
title Publish Website

echo =======================================
echo    Starting auto publish...
echo =======================================
echo.

:: Call deploy.ps1 in the same folder, bypassing the execution policy
powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0deploy.ps1"

echo.
echo =======================================
echo    Done. Check above for any errors.
echo =======================================
echo.
pause
