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

# 2. 检查 Git 是否有改动（有改动才提交，没改动不要直接退出）
$gitStatus = git status --porcelain
if ([string]::IsNullOrWhiteSpace($gitStatus)) {
    Write-Host "✨ 没有新的改动，跳过提交。" -ForegroundColor Yellow
} else {
    Write-Host "📦 正在提交到本地仓库..." -ForegroundColor Cyan
    # 2>&1 | Write-Host 是为了把 git 的 warning / 进度信息转成普通文本输出，
    # 否则 PowerShell 会把 stderr 当成红色错误抛出来（其实并不是失败）
    git add . 2>&1 | Write-Host
    $commitMsg = "auto: sync notes and deploy $(Get-Date -Format 'yyyy-MM-dd HH:mm')"
    git commit -m $commitMsg 2>&1 | Write-Host
}

# 3. 推送：不管本次有没有新改动都推一次，
#    这样之前因网络失败积压在本地、还没推上去的 commit 也能补推上去
Write-Host "☁️ 正在推送到线上..." -ForegroundColor Cyan
$pendingCommits = @(git log --oneline origin/main..HEAD 2>$null)
if ($pendingCommits.Count -gt 0) {
    Write-Host ("  检测到本地还有 {0} 个 commit 未推送，正在一并推送..." -f $pendingCommits.Count) -ForegroundColor Yellow
}
git push origin main 2>&1 | Write-Host

if ($LASTEXITCODE -eq 0) {
    Write-Host "🎉 发布成功！请稍等 1 分钟去网页查看。" -ForegroundColor Green
} else {
    Write-Host "⚠️ 推送失败！大概率是网络问题，请开启代理或切换手机热点后，直接执行 'git push origin main' 重试。" -ForegroundColor Red
}
