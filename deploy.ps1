# 让 Python 的中文输出不乱码（Windows 控制台默认是 GBK）
$env:PYTHONIOENCODING = 'utf-8'
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8

# 1. 运行 Python 转换脚本
Write-Host "🚀 正在转换 Obsidian 笔记..." -ForegroundColor Cyan
python sync_notes.py

# 检查上一步是否成功
if ($LASTEXITCODE -ne 0) {
    Write-Host "❌ 转换失败，请检查上面的报错信息。" -ForegroundColor Red
    exit 1
}

# 2. 检查 Git 是否有改动
$gitStatus = git status --porcelain
if ([string]::IsNullOrWhiteSpace($gitStatus)) {
    Write-Host "✨ 没有新的改动，无需提交。" -ForegroundColor Yellow
    exit 0
}

# 3. 提交并推送
Write-Host "📦 正在提交并推送到 GitHub..." -ForegroundColor Cyan
# 2>&1 | Out-Host 让 git 的 warning / 进度以普通文本显示，
# 而不是被 PowerShell 当成红色错误信息抛出来
git add . 2>&1 | Out-Host
$commitMsg = "auto: sync notes and deploy $(Get-Date -Format 'yyyy-MM-dd HH:mm')"
git commit -m $commitMsg 2>&1 | Out-Host

# 4. 处理 Push（考虑网络问题）
Write-Host "☁️ 正在推送到线上..." -ForegroundColor Cyan
git push origin main 2>&1 | Out-Host

if ($LASTEXITCODE -eq 0) {
    Write-Host "🎉 发布成功！请稍等 1 分钟去网页查看。" -ForegroundColor Green
} else {
    Write-Host "⚠️ 推送失败！大概率是网络问题，请开启代理或切换手机热点后，直接执行 'git push origin main' 重试。" -ForegroundColor Red
}
