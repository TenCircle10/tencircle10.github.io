document.addEventListener('DOMContentLoaded', function () {
  // 查找所有包含 [!type] 格式的引用块
  const blockquotes = document.querySelectorAll('blockquote');
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
    }
  });
});
