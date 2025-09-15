

### 什么是 React？
React 是由 Facebook 开发的开源 JavaScript 库，用于构建用户界面，特别适合构建单页应用和交互式 UI。

React 的核心特点：
- 组件化开发
- 虚拟 DOM 提高性能
- 单向数据流
- JSX 语法

### 环境搭建

我们使用 Create React App 快速创建 React 应用：

```bash
# 安装 Create React App
npm install -g create-react-app

# 创建新应用
npx create-react-app my-first-react-app

# 进入项目目录
cd my-first-react-app

# 启动开发服务器
npm start
```

应用启动后，访问 http://localhost:3000 即可看到默认页面。

项目结构说明：
- `public/`：静态资源
- `src/`：源代码
  - `App.js`：根组件
  - `index.js`：入口文件
