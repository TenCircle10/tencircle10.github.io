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
git add .
$commitMsg = "auto: sync notes and deploy $(Get-Date -Format 'yyyy-MM-dd HH:mm')"
git commit -m $commitMsg

# 4. 处理 Push（考虑网络问题）
Write-Host "☁️ 正在推送到线上..." -ForegroundColor Cyan
git push origin main

if ($LASTEXITCODE -eq 0) {
    Write-Host "🎉 发布成功！请稍等 1 分钟去网页查看。" -ForegroundColor Green
} else {
    Write-Host "⚠️ 推送失败！大概率是网络问题，请开启代理或切换手机热点后，直接执行 'git push origin main' 重试。" -ForegroundColor Red
}
