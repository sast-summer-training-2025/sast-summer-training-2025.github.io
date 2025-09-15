// Welcome.js
function Welcome() {
  return <h1>Hello, React!</h1>;
}

export default Welcome;

// 在其他组件中使用
import Welcome from '/* Path to welcome.js */';

function App() {
  return (
    <div>
      <Welcome />
    </div>
  );
}
