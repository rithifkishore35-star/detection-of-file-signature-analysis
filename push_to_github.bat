@echo off
title FileGuard - Push to GitHub
echo =====================================================================
echo    FILEGUARD - PUSH TO GITHUB REPOSITORY
echo    Target: https://github.com/rithifkishore35-star/detection-of-file-signature-analysis.git
echo =====================================================================
echo.
cd /d "%~dp0"

echo [Step 1/3] Staging all files and committing...
git remote set-url origin https://github.com/rithifkishore35-star/detection-of-file-signature-analysis.git
git add -A
git commit -m "FileGuard - Premium Cybersecurity Dark Theme & Forensic Verification System"

echo.
echo [Step 2/3] Setting branch to main...
git branch -M main

echo.
echo [Step 3/3] Pushing to GitHub...
git push -u origin main

echo.
if %ERRORLEVEL% EQU 0 (
    echo [SUCCESS] Your project has been successfully pushed to GitHub!
    echo Repository: https://github.com/rithifkishore35-star/detection-of-file-signature-analysis
) else (
    echo [NOTICE] If authentication or Git setup is needed:
    echo 1. Install Git for Windows if not installed: https://git-scm.com/download/win
    echo 2. Login or use your GitHub Personal Access Token
    echo 3. Or run: git push -u origin main
)
echo.
pause
