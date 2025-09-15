function EventExamples() {
  // 基本事件处理
  const handleClick = () => {
    alert('Button clicked!');
  };

  // 带参数的事件处理
  const handleGreeting = (name) => {
    alert(`Hello, ${name}!`);
  };

  // 处理表单输入
  const [inputValue, setInputValue] = useState('');
  
  const handleInputChange = (e) => {
    setInputValue(e.target.value);
  };

  // 阻止默认行为
  const handleFormSubmit = (e) => {
    e.preventDefault();
    alert(`Form submitted: ${inputValue}`);
  };

  return (
    <div>
      {/* 基本点击事件 */}
      <button onClick={handleClick}>Click me</button>
      
      {/* 带参数的事件 */}
      <button onClick={() => handleGreeting('React')}>
        Greet
      </button>
      
      {/* 表单事件 */}
      <form onSubmit={handleFormSubmit}>
        <input
          type="text"
          value={inputValue}
          onChange={handleInputChange}
        />
        <button type="submit">Submit</button>
      </form>
    </div>
  );
}
