// ===== 1. 获取 DOM 元素 =====
// document.querySelector('CSS选择器') 返回第一个匹配元素
const btn = document.getElementById('sayHiBtn');
const input = document.getElementById('nameInput');

// ===== 2. 事件监听 =====
// 语法：元素.addEventListener('事件名', 回调函数)
btn.addEventListener('click', function () {
  // 2-1 读取输入框的值
  const name = input.value.trim(); // trim() 去掉首尾空格
  
  // 2-2 空值判断（逻辑或运算符）
  const who = name || '朋友';      // 如果 name 为假（空串）则默认 '朋友'
  
  // 2-3 弹出对话框
  alert(`Hello, ${who}!`);         // 模板字符串，反引号 + ${变量}
  
  // 2-4 彩蛋：改变标题
  document.title = `你好，${who}`;
});

// ===== 3. 进阶：按回车也能触发 =====
input.addEventListener('keydown', function (event) {
  // 当按键码为 13（Enter）时触发按钮点击
  if (event.keyCode === 13) {
    btn.click();
  }
});
