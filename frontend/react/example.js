/*
## 2. JSX 语法基础

JSX 是 JavaScript XML 的缩写，是一种在 JavaScript 中编写 HTML 风格代码的语法。

### 基本语法





### JSX 规则

1. 必须有一个根元素
2. 标签必须正确闭合
3. 使用 camelCase 命名属性（如 onClick 而非 onclick）
4. 使用 {} 嵌入 JavaScript 表达式
5. 注释写法：`{/* 这是 JSX 注释 */





// JSX 示例
const element = (
  <div>
    <h1>Hello, React!</h1>
    <p>This is a JSX example</p>
  </div>
);

// 在 JavaScript 中使用表达式
const name = "React Developer";
const elementWithExpression = <h1>Hello, {name}</h1>;

// 条件渲染
const isLoggedIn = true;
const loginMessage = (
  <div>
    {isLoggedIn ? (
      <p>Welcome back!</p>
    ) : (
      <p>Please sign in.</p>
    )}
  </div>
);

// 属性定义
const imageUrl = "https://picsum.photos/200/300";
const imageElement = <img src={imageUrl} alt="Example" className="my-image" />;
// 注意：使用 className 而不是 class，htmlFor 而不是 for
