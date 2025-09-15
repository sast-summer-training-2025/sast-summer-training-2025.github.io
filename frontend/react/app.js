import { useState } from 'react';

function TodoApp() {
  // 状态管理
  const [todos, setTodos] = useState([]);
  const [inputValue, setInputValue] = useState('');
  
  // 处理输入变化
  const handleInputChange = (e) => {
    setInputValue(e.target.value);
  };
  
  // 添加新待办
  const handleAddTodo = (e) => {
    e.preventDefault();
    if (inputValue.trim()) {
      setTodos([
        ...todos,
        {
          id: Date.now(),
          text: inputValue,
          completed: false
        }
      ]);
      setInputValue('');
    }
  };
  
  // 切换待办状态
  const handleToggleTodo = (id) => {
    setTodos(
      todos.map(todo =>
        todo.id === id ? { ...todo, completed: !todo.completed } : todo
      )
    );
  };
  
  // 删除待办
  const handleDeleteTodo = (id) => {
    setTodos(todos.filter(todo => todo.id !== id));
  };
  
  // 清除已完成待办
  const handleClearCompleted = () => {
    setTodos(todos.filter(todo => !todo.completed));
  };
  
  return (
    <div className="todo-app">
      <h1>Todo List</h1>
      
      {/* 添加待办表单 */}
      <form onSubmit={handleAddTodo}>
        <input
          type="text"
          value={inputValue}
          onChange={handleInputChange}
          placeholder="Add a new todo..."
        />
        <button type="submit">Add</button>
      </form>
      
      {/* 待办列表 */}
      <ul>
        {todos.map(todo => (
          <li 
            key={todo.id}
            style={{ textDecoration: todo.completed ? 'line-through' : 'none' }}
          >
            <span onClick={() => handleToggleTodo(todo.id)}>
              {todo.text}
            </span>
            <button onClick={() => handleDeleteTodo(todo.id)}>
              Delete
            </button>
          </li>
        ))}
      </ul>
      
      {/* 操作按钮 */}
      {todos.some(todo => todo.completed) && (
        <button onClick={handleClearCompleted}>
          Clear Completed
        </button>
      )}
      
      {/* 统计信息 */}
      <p>
        {todos.filter(todo => !todo.completed).length} items left
      </p>
    </div>
  );
}

export default TodoApp;
