document.addEventListener('DOMContentLoaded', function () {
  // 查找所有包含 [!type] 格式的引用块
  const blockquotes = document.querySelectorAll('blockquote');
  const replacedNodes = []; // 替换出来的 callout 内容节点，稍后交给 MathJax 重排
  blockquotes.forEach(bq => {
    const firstLine = bq.innerHTML.trim().split('\n')[0];
    const calloutMatch = firstLine.match(/^\[!(\w+)\]([+-])?\s*(.*)$/);
    if (calloutMatch) {
      const type = calloutMatch[1].toLowerCase();
      const foldType = calloutMatch[2]; // '+' 或 '-'
      const title = calloutMatch[3] || type.charAt(0).toUpperCase() + type.slice(1);
      // 构建 Callout HTML
      const callout = document.createElement('div');
      callout.className = 'callout';
      callout.dataset.callout = type;
      callout.innerHTML = `<div class="callout-title">${title}</div><div class="callout-content"></div>`;
      // 将引用块中的其余内容移入 Callout
      const contentDiv = callout.querySelector('.callout-content');
      const remainingHTML = bq.innerHTML.substring(firstLine.length).trim();
      if (remainingHTML) contentDiv.innerHTML = remainingHTML;
      // 替换原始引用块
      bq.parentNode.replaceChild(callout, bq);
      // 记录替换出来的节点，等 MathJax 就绪后重新排版
      replacedNodes.push(contentDiv);
    }
  });

  // MathJax 是 async 加载的，此刻可能尚未就绪；而 callout 又是在 MathJax 首次排版
  // 之后才替换节点的，所以这里显式等 MathJax.startup.promise 完成后，
  // 对替换出来的节点再做一次排版，避免其中的公式丢失或不刷新。
  retypesetMath(replacedNodes);
});

// 对指定节点重新执行 MathJax 排版（节点里没有公式时是空操作）
function retypesetMath(targets) {
  if (!targets.length) return;
  const run = () => MathJax.typesetPromise(targets)
    .catch(err => console.error('MathJax typeset failed:', err));
  if (window.MathJax && MathJax.startup && MathJax.startup.promise) {
    MathJax.startup.promise.then(run);
    return;
  }
  // MathJax 脚本还没加载完，轮询等待（最多约 10 秒）
  let attempts = 0;
  const timer = setInterval(function () {
    if (window.MathJax && MathJax.startup && MathJax.startup.promise) {
      clearInterval(timer);
      MathJax.startup.promise.then(run);
    } else if (++attempts >= 100) {
      clearInterval(timer);
    }
  }, 100);
}
