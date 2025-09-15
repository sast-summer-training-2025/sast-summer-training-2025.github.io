/*### State（状态）

State 是组件内部管理的数据，当 state 发生变化时，组件会重新渲染。*/

import { useState } from 'react';

function Counter() {
  // 声明一个 count 状态变量，初始值为 0
  // setCount 是更新 count 的函数
  const [count, setCount] = useState(0);

  return (
    <div>
      <p>You clicked {count} times</p>
      <button onClick={() => setCount(count + 1)}>
        Click me
      </button>
    </div>
  );
}

// 复杂状态示例
function UserForm() {
  const [user, setUser] = useState({
    name: '',
    email: ''
  });

  // 更新对象状态的正确方式
  const handleNameChange = (e) => {
    setUser(prevState => ({
      ...prevState,
      name: e.target.value
    }));
  };

  const handleEmailChange = (e) => {
    setUser(prevState => ({
      ...prevState,
      email: e.target.value
    }));
  };

  return (
    <form>
      <input
        type="text"
        value={user.name}
        onChange={handleNameChange}
        placeholder="Name"
      />
      <input
        type="email"
        value={user.email}
        onChange={handleEmailChange}
        placeholder="Email"
      />
      <p>Name: {user.name}</p>
      <p>Email: {user.email}</p>
    </form>
  );
}
