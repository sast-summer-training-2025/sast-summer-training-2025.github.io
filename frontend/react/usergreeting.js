/*## 3. 组件与 Props

### 函数组件

函数组件是最简单的组件形式，就是一个返回 React 元素的 JavaScript 函数。





### Props

Props 是组件的输入，允许我们将数据从父组件传递到子组件。





注意：Props 是只读的，子组件不能修改接收到的 props。*/


// UserGreeting.js
function UserGreeting(props) {
  return <h1>Hello, {props.name}!</h1>;
}

// 使用示例
function App() {
  return (
    <div>
      <UserGreeting name="Alice" />
      <UserGreeting name="Bob" />
      <UserGreeting name="Charlie" />
    </div>
  );
}

// Props 可以是任何类型
function Product(props) {
  return (
    <div className="product">
      <h3>{props.name}</h3>
      <p>Price: ${props.price}</p>
      <p>In stock: {props.inStock ? 'Yes' : 'No'}</p>
    </div>
  );
}

// 使用 Product 组件
function ProductList() {
  return (
    <div>
      <Product name="Laptop" price={999.99} inStock={true} />
      <Product name="Mouse" price={25.50} inStock={false} />
    </div>
  );
}
