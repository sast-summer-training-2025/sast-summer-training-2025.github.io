/*### 组件生命周期

类组件有生命周期方法，但现代 React 更推荐使用 Hooks。主要生命周期阶段：

1. 挂载（Mounting）：组件被创建并插入 DOM
2. 更新（Updating）：组件 props 或 state 变化
3. 卸载（Unmounting）：组件从 DOM 中移除

### Hooks 基础

Hooks 允许在函数组件中使用状态和其他 React 特性。*/

import { useState, useEffect } from 'react';

// useState: 管理状态
function CounterWithHooks() {
  const [count, setCount] = useState(0);
  
  return (
    <div>
      <p>Count: {count}</p>
      <button onClick={() => setCount(count + 1)}>Increment</button>
    </div>
  );
}

// useEffect: 处理副作用（相当于生命周期方法）
function DataFetcher() {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);
  
  // 相当于 componentDidMount 和 componentDidUpdate
  useEffect(() => {
    // 模拟 API 请求
    fetch('https://api.example.com/data')
      .then(response => response.json())
      .then(data => {
        setData(data);
        setLoading(false);
      });
      
    // 清理函数，相当于 componentWillUnmount
    return () => {
      // 取消请求或清理资源
    };
  }, []); // 空依赖数组表示只在挂载和卸载时执行
  
  if (loading) return <p>Loading...</p>;
  
  return (
    <div>
      <h2>Fetched Data</h2>
      <pre>{JSON.stringify(data, null, 2)}</pre>
    </div>
  );
}

// 使用多个 useEffect
function WindowSizeTracker() {
  const [windowSize, setWindowSize] = useState({
    width: window.innerWidth,
    height: window.innerHeight
  });
  
  useEffect(() => {
    const handleResize = () => {
      setWindowSize({
        width: window.innerWidth,
        height: window.innerHeight
      });
    };
    
    window.addEventListener('resize', handleResize);
    
    // 清理函数
    return () => {
      window.removeEventListener('resize', handleResize);
    };
  }, []); // 只在挂载时添加事件监听
  
  return (
    <div>
      <p>Window size: {windowSize.width} x {windowSize.height}</p>
    </div>
  );
}
