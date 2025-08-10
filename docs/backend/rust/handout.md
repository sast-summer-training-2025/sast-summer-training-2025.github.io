# Rust 语言基础

!!! note 
    
    本课程讲义假定读者具有一定的 C/C++ 语言基础，并具备了面向对象程序设计的基本概念。

## Rust 简介

Rust 是一门注重安全、并发和性能的系统级编程语言。软件开发人员 Graydon Hoare 于 2006 年在 Mozilla Research 工作时创建了 Rust 作为个人项目。Mozilla 于 2009 年正式赞助了该项目。Rust 的第一个稳定版本 Rust 1.0 于 2015 年 5 月发布。继 2020 年 8 月大规模裁员 Mozilla 员工后，其他多家公司与 Mozilla 一起通过 2021 年 2 月创建 Rust 基金会来赞助 Rust。2022 年 12 月，Rust 成为 Linux 内核开发中除 C 和汇编之外第一个支持的语言。

Rust 旨在提供与 C/C++ 相媲美的运行速度，同时通过所有权（Ownership）、借用（Borrowing）和生命周期（Lifetimes）等机制，最大程度地避免内存安全问题。Rust 支持函数式和面向对象编程范式，广泛应用于操作系统、嵌入式开发、Web 后端等领域。其包管理工具 Cargo 也极大地方便了项目的构建与依赖管理。Rust 因其在许多软件项目中的采用而闻名，尤其是 Web 服务和系统软件。它已经在学术上进行了研究，并拥有不断壮大的开发人员社区。

## Rust 文档

**Rust Documentation**

- [Rust Documentation](https://doc.rust-lang.org/stable/)
- [Learn Rust](https://www.rust-lang.org/learn)

**The Book**

- [The Rust Programming Language](https://doc.rust-lang.org/book/)
- [Rust 程序设计语言 中文版](https://rustwiki.org/zh-CN/book/)

**Rust Wiki**

- [Rust 官方文档中文教程](https://rustwiki.org)

**Rust By Example**

- [Rust By Example](https://doc.rust-lang.org/rust-by-example/)
- [通过例子学 Rust 中文版](https://rustwiki.org/zh-CN/rust-by-example/)

**Exercises**

- [Rustlings](https://rustlings.rust-lang.org)

**Cargo**

- [The Cargo Book](https://doc.rust-lang.org/stable/cargo/index.html)

**Crates**

- [DOCS.RS](https://docs.rs)
- [Crate std](https://doc.rust-lang.org/stable/std/)
- [The Rust community’s crate registry](https://crates.io)

**Advanced**

- [Effective Rust](https://www.lurklurk.org/effective-rust/)
- [The Rust Unstable Book](https://doc.rust-lang.org/stable/unstable-book/index.html)
- [The Embedded Rust Book](https://doc.rust-lang.org/stable/embedded-book/index.html)

**Others**

- [The Rustc Book](https://doc.rust-lang.org/rustc/index.html)
- [The Rustdoc Book](https://doc.rust-lang.org/rustdoc/index.html)
- [The Rust Edition Guide](https://doc.rust-lang.org/edition-guide/index.html)

## Rust 环境

该部分可参考

- [Rust 快速入门](https://docs.net9.org/languages/rust/start/)
 
或者 

- [The Rust Programming Language：Getting Started](https://doc.rust-lang.org/book/ch01-00-getting-started.html)
- [Rust 程序设计语言 中文版:入门指南](https://rustwiki.org/zh-CN/book/ch01-00-getting-started.html)

进行安装。

推荐先安装 Cargo 包管理器，并成功使用 Cargo 创建项目并编译运行得到 `Hello World!` 结果。

或者，你也可以使用 Rust 官方提供的 [Rust Playground](https://play.rust-lang.org/?version=stable&mode=debug&edition=2024&gist=05f1a8e53b8b732bf60b7466ceff5699) 线上环境。

## Rust 的所有权

为了兼顾内存使用的**安全**和**性能**，Rust 在设计之初就采用了与 C++ 完全不同的内存管理。

Rust 引入了**所有权（ownership）**的概念：

- Rust 中的每个值都有所有者 (owner)。
- 同一时刻每个值只有一个所有者。
- 当所有者失效，值也将被丢弃。

### 变量绑定

变量通过绑定的方式，获得对数据的所有权。如果一个绑定超出作用域，其绑定的数据将被自动释放。

```rust
let a = 1;
```

变量之间的**赋值**行为，将会直接导致绑定关系的变化，这一语义被称为**移动所有权**，亦即**掩盖 (shadowing)**。

```rust
let s1 = String::from("hello");
let s2 = s1; // 字符串 "hello" 已经被 s2 绑定，s1 悬置。

println!("{s1}, world!");
// 此时将发生编译错误 error: borrow of moved value: `s1`
```

!!! note "移动所有权"
    - 移动所有权是编译时的语义，不涉及程序运行时的数据移动，数据对应的内存区域并没有改变，只是更改了对应的变量名（类似C++的指针）。
    - 移动是默认行为(通过绑定或赋值)，不需要像 C++ 那样用 std::move 来显式指定。

### 借用

但并非所有语境下的变量赋值都希望移交所有权，这个时候应该采用 Rust 中的**借用（borrow）**概念。

#### 借用规则

```rust
let v = vec![1, 2, 3];
let v_ref = &v; // v_ref is a reference to v.
```

!!! note "借用规则"

    - 可以通过对变量取引用来借用变量中的数据的所有权，此时所有权本身并没有发生变化。
        - 当引用超过作用域，借用也随之结束。
        - 原来的变量依然拥有对数据的所有权。

    ```rust
    let v = vec![1, 2, 3];
    // v_ref is a reference to v.
    let v_ref = &v;
    // use v_ref to access the data in the vector v.
    assert_eq!(v[1], v_ref[1]);
    ```

    - 当借用发生时，会对原来的变量增加限制：
        - 当一个变量有引用存在时，不能移交它所绑定的数据的所有权。

    ```rust
    let v = vec![1, 2, 3];
    let v_ref = &v; 
    let v_new = v;
    // Moving ownership to v_new would invalidate v_ref.
    // error: cannot move out of `v` because it is borrowed 
    ```

#### 可变借用与不可变借用

Rust 类型系统中，变量被分为**可变**与**不可变**。在借用中，同理可分为**可变借用** `&mut` 和**不可变借用** `&`。
```rust
fn main() {
    let mut vector: Vec<i32> = vec![];
    let vector_ref: &mut Vec<i32> = &mut vector; 
    push(vector_ref, 4);
}
```

!!! note "借用规则"
    - 不能在某个对象不存在后继续保留对它的引用。一个对象可以
        - 同时存在**多个不可变**引用(&T)。
        - 或者**仅有一个可变引用**(&mut T)。 
    - 以上两者不能同时存在。

#### 函数参数中的借用

需要注意的是，**函数**的**参数传递**时，采用的是与变量赋值和借用相同的语法规则。如果不指定 `&` 或 `&mut`,变量会直接发生移动。
```rust
fn hello_move(s: String) {
    println!("Message by moving: {}", S);
}

fn hello_borrow(s: &String) {
    println!("Message by borrowing: {}", S);
}

fn main() {
    let x: String  = String::from("hello");
    let y: String  = String::from("hello");
    
    hello_move(x);
    hello_borrow(&y);
    
    println!("x:{}",x); // error[E0382]: borrow of moved value: `x`
    println!("y:{}",y); // This runs normally. 
}

```

!!! note "变量的拷贝"
    如果想要直接获得一份变量的副本，可以使用 Rust 的 Copy 特型。

    - 大多数基本类型是 Copy 类型(i32、f64、char、bool 等等)。
        - 基本类型发生赋值时，会发生拷贝而非移动。
  
    
    ```rust
    let x: i32 = 12;
    let y = x; // `i32` is `Copy`, so it's not moved :D 
    println!("x still works: {}, and so does y: {}", x, y);
    ```
    
    - 可以通过 `impl Copy for ...` 或 `#[derive(Copy)]` 宏为变量实现 Copy 特型。
        - 非基本类型在实现了 Copy 特型后，可以通过 `clone()` 等方法进行拷贝。
    
    ```rust
    let x: String  = String::from("hello");
    let y = x.clone(); // here copy an 'x' to y
    println!("x still works: {}, and so does y: {}", x, y);
    ```
所有权的思想贯穿了 Rust 编程的全过程，在后续的 **变量**、**函数**、**结构体** 等章节中，你还会多次遇到所有权的**转移**与**借用**问题。

## Rust 类型系统

### 变量声明

Rust 语言中通过 `let` 关键字来声明变量。Rust 是一门静态强类型语言，因此任何一个变量都有一个确定、不可变的类型。如果在声明同时初始化，则可以依靠编译器的类型推断来得到变量类型，不一定需要显式指定类型。

```rust
let a: i32 = 1; // 完整的变量声明和初始化
let b: i32; // 显式声明类型，未初始化
let c = 1; // 声明同时初始化，类型由编译器推断为 i32
// let d; // 既没有初始化又没有标注类型，编译器无从得知类型，编译无法通过
```

!!! note "与 C++ 的对照"

    Rust 的 `let` 关键字与 C++11 中引入的 `auto` 关键字有一些类似之处，例如在声明时初始化的变量可以自行推断类型。

#### 可变性与不可变性

Rust 语言与许多其他语言不同的一点在于变量的**默认不可变性**，即变量的值默认是不可修改的。

```rust
let a = 1;
// a = 2; // 变量 a 默认不可变，编译无法通过
```

要声明一个可变的变量，需要加上 `mut` 关键字。

```rust
let mut a = 1;
a = 2; // 变量 a 可变，OK 
```

!!! note "与 C++ 的对照"

    简单地看，`let` 声明的变量更类似于 C++ 中用 `const` 声明的常量，而 `let mut` 声明的变量更类似于“普通”的 C++ 变量。

    这种说法是不严格的，但是这样思考可以快速上手。

Rust 的这种设计看似奇怪，其实也有其用意。一般大部分变量的值实际上都不需要修改，默认不可变可以强制程序员思考变量是否需要修改，从而避免了一些潜在的错误。而在 C++ 中想达到相同的效果，则需要主动使用大量 `const` 关键字，其繁琐会让大部分程序员不愿意这么做。

!!! note "如何打印一个变量"

    ```rust
    let a: i32 = 1;
    println!("{}", a);
    ```

    这里的 `println!` 是一个宏，但使用起来与函数很相似。

#### 常量

Rust 中的常量使用 `const` 关键字声明，常量的值必须在编译期间确定。常量的类型必须显式指定。

```rust
const SECONDS_PER_DAY: i32 = 24 * 60 * 60; // 常量的值必须在编译期间确定. 能够通过编译
// const B = 1; // 常量必须显式指定类型，编译无法通过
const c: i32 = 1; // 能够通过编译，但会被编译器警告，因为常量名的规范是 大写字母+下划线
```

!!! note "与 C++ 的对照"

    Rust 的 `const` 在定位上和 C++ 的 `constexpr` 基本是一致的。

    C++ 中，一般把 `const` 与 `constexpr` 所定义的量都笼统地称为“常量”。但从 Rust 的视角看，只有编译期常量才是真正的“常量”，而 C++ 中用 `const` 声明的所谓“常量”在语义上只是一个“不可变量”（readonly，只读），其实反而更接近 变量 而不是 常量。

    也许可以这样理解：常量是一个「值」；而变量是一个「对象」、其值可能要在运行时才能确定，而这个变量是否可变则是另一个回事。

    例如，定义数组要求数组的长度必须是常量表达式。但 C++ 中 `const` 声明的所谓“常量”并不一定能满足这点；而 C++ 中的 `constexpr` 与 Rust 中的 `const` 则都能满足。

#### 变量遮蔽

其英文为 `shadowing`，可被译为“遮蔽”、“重影”，是 Rust 的一种特殊语法，允许在同一作用域中声明一个与之前变量同名的新变量，从而遮蔽之前的变量。

这相当于把变量名绑定到了一个新的值上，而不是修改了原来的值。这种特性在一些场景下很有用，可以减少变量的数量、减轻给变量取名字的负担。

```rust
let spaces = "   "; // spaces 是一个字符串
let spaces = spaces.len(); // spaces 变成了一个数字

let mut spaces = "   "; // spaces 是一个字符串
// spaces = spaces.len(); // 编译无法通过，因为 spaces 已经是一个字符串，不能再赋值为数字，类型不匹配

let mut num = 1;
num *= 2; // OK
```

!!! note "变量遮蔽的原理"

    Rust 中变量遮蔽的本质其实是 Rust 的所有权系统。Rust 的变量更接近于 C++ 的指针，表示对内存的引用。

### 变量类型

#### 基本类型

**整数**

Rust 中的整数有许多种，按照长度不同、有无符号进行区分。

Rust的多数整数命名遵循“**字母 + 数字**”这一结构。其中，以字母 `i` 开头的类型表示它是**有符号整数**，而以字母 `u` 开头的类型表示它是**无符号整数**，字母后面的数字则表示这一类型的长度，从最短的 8 字节到最长的 128 字节，有 `i8, u8, i16, u16, i32, u32, i64, u64, i128, u128` 这一系列类型。

编译器将整形字面量默认类型推导为 `i32`。

```rust
let a = 1; // a 的类型为（隐式推导为）i32
let b: u32 = 1; // b 的类型（显式声明为）u32
```

!!! note "与 C++ 的对照"

    [C/C++ 数据模型](https://zh.cppreference.com/w/cpp/language/types) 并没有给整形规定具体长度，只规定了不同整形之间长度的比较关系和最小长度。在常见的 64 位机器上，`char, short, int, long long` 分别表示 8、16、32 和 64 位带符号整数，分别可以对应 Rust 的 `i8, i16, i32, i64`，无符号整数类似。

    在实际使用中，如果需要确定长度的整数，可以使用 `cstdlib` 中的 `int32_t` 等类型，它们在不同平台上有不同的 `typedef`，对应不同的具体类型。

    C/C++ 没有统一的 128 位整数标准。

同时，Rust 还提供了两个特殊的类型 `isize` 和 `usize`，这两个类型的长度由平台决定，在 32 位平台上是 32 位，在 64 位平台上是 64 位。这一设计方便了内存中的寻址，如数组下标就接受 `usize` 而不是 `u32` 类型。

**浮点数**

类似整形，Rust 中的浮点型以字母 `f` 开头，后面是对应的长度，但只有 `f32` 和 `f64` 两种类型。

编译器将浮点字面量默认类型推导为 `f64`。

```rust
let f: f32 = 1.0;
let g = 2.0; // 类型默认推导为 f64
```

**布尔值**

Rust 中的布尔型为 `bool`，有且仅有两个值 `true` 和 `false`。

**字符类型**

Rust 中一个字符由单引号包裹，表示一个 **Unicode 字符**而非一个 **ASCII 字符或字节**。

```rust
let ascii_char_z = 'z';
let heart_eyed_cat = '😻';
```

!!! note "与 C++ 的对照"

    Rust 在设计时就考虑到了多语言支持，因此采取了这样的设计。如果希望与 C/C++ 中的 `unsigned char` 对应，即表示**一个字节**，应当使用 Rust 中的 `u8` 类型。

#### 复合类型

**元组**

元组将几个相同或不同的类型组合为一个复合类型。

```rust
let tuple_1: (i32, f64, bool) = (1, 2.0, false); // 显式声明类型
let tuple_2 = (3, 1.0, true); // 隐式推断类型
```

元组支持通过模式匹配来解构，也可以通过点 `.` 来访问其元素。

```rust
let tuple = (1, 2.0, false);
let (x, y, z) = tuple;
// 上面的 let 语句创建了 i32 类型的变量 x、f64 类型的变量 y 和 bool 类型的变量 z
let xx = tuple.0;
let yy = tuple.1;
let zz = tuple.2;
// xx, yy, zz 分别对应 x, y, z
```

!!! note "与 C++ 的对照"

    C++ 语言标准中并没有元组类型，但标准库中提供了功能和语义都相同的 `std::tuple`。但总的来说，C++ 的元组使用较为繁琐，不如 Rust 中作为基本类型的元组方便。

**数组**

Rust的数组将**固定数目**的**同类型**变量储存在一起。

```rust
let arr_1: [i32; 5] = [1, 2, 3, 4, 5];
// [i32; 5] 表示包含5个 i32 的数组
let arr_2 = [1.0, 2.0, 3.0, 4.0];
// arr_2 的类型被隐式推断为 [f64; 4]
let arr_long: [i32; 100] = [0; 100];
// arr_long 的类型为 [i32; 100]，而且这 100 个元素都是 0
```

如果需要一个可变长的数组，那么可以使用 `Vec`。

```rust
let arr_vec: Vec<i32> = Vec::new();
// Vec::new() 返回一个新的 Vec<i32> 结构体
```

!!! note "与 C++ 的对照"

    Rust 的数组可以直接作为参数传递，这一点与 C/C++ 不同（C++ 中的 `std::tuple` 与 Rust 的数组更加类似）。这是因为 Rust 的数组是在栈上分配的。与 C/C++ 类似的是，数组的长度都是不可变的，变长的线性容器在两门语言中分别叫做 `std::Vec` 和 `std::vector`。 

Rust 的下标访问自带越界检查。

下面的代码将会在编译时报错：

```rust
let arr = [1, 2, 3];
let element = arr[3]; // 编译器报错：index out of bounds: the length is 3 but the index is 3
```

下面的代码能够通过编译，但当输入的下标超出数组长度时，程序会立即退出而不允许访问越界的内存：

```rust
use std::io;

let arr = [1, 2, 3];
let mut index = String::new();
io::stdin().read_line(&mut index).expect("Failed to read line"); // 若输入10...
let index: usize = index.trim().parse().expect("Index must be a number");
let element = arr[index]; // ...程序产生运行时错误并退出
println!("The value of element is: {}", element); // 该行不会被执行
```

#### 单元类型

Rust 中有一个特殊的**单元类型 （Unit Type）**，亦称 **单位元**，它的类型是 `()`，而且它唯一的值也是 `()`。例如，当一个表达式或函数什么也不返回时，它的返回类型和返回值就都是 `()`。

```rust
fn some_func() {
    return 0;
}
```

尝试编译上面的函数，编译器将报告类型不匹配，期望得到 `()` 而得到了整数。这表明无返回值的函数实质上返回了 `()`。

!!! note "与 C++ 的对照"

    Rust 的 `()` 类似 C/C++ 的 `void`，但与之不完全相同。在开始理解时，可以这样对照；但请在认真探究 `()` 类型的设计时毫不留情地将有关 C/C++ 中的 `void` 的印象全部抛弃。

!!! caution "关于 Unit Type"

    在这里，我们不解释 Unit Type 为何设计成如此，也不深究它在 Rust 的其他地方有哪些用处。如果对 Unit Type 的细节感兴趣，可以参考 Rust 官方文档或者查看 [这个 StackOverFlow 问题](https://stackoverflow.com/questions/24842271/what-is-the-purpose-of-the-unit-type-in-rust)。

## Rust 中的流程控制

### 条件表达式

Rust 中的条件语句类似 C/C++，都是通过 `if` 和 `else` 来控制。

`if` 后面的条件可以省略括号，编译器也推荐这样做。

```rust
let age = 17;
if age < 18 {
    println!("您未成年");
} else {
    println!("您成年了");
}
```

注意，`if` 实际上是表达式而非语句，因此可以拥有值。

```rust
let age = 17;
let adulthood = if age < 18 {
    false
} else {
    true
};
```

Rust 是一门基于表达式的语言，这仅仅是冰山一角。读者在实际采用 Rust 编程时将会对这一设计有更深刻的理解。

!!! note "与 C++ 的对照"

    Rust 中没有 C/C++ 中常见的三元表达式，但是可以用 `if-else` 表达式来实现相同的功能。

### 循环语句

#### `for` 循环

`for` 循环用于遍历容器中的每一个元素，这与 C 风格的 `for` 循环大为不同，而与 Python 更加类似。

```rust
let mut sum = 0;
for i in (1 .. 10) { // (a .. b) 创建了一个数字序列 Range，表示半开半闭区间 [a, b) 中的所有整数。
    sum += i;
}
// 实际上这里的求和可以通过迭代器用更优雅和快速的方法重写，此处仅仅作为演示。
let word: &str = "World";
    for letter in word.chars() { // 将 &str 类型转化为迭代器
        println!("{}", letter);
}
// 迭代器的简单示例
```

#### `while` 循环

`while` 循环与 C/C++ 较为类似，仅仅给出代码样例。

```rust
let mut sum = 0;
let mut a = 1;
while a < 10 {
    sum += a;
    a += 1;
}
```

#### `loop` 循环

`loop` 循环是显式的死循环，会一直重复执行直到显式 `break` 为止。

```rust
let mut sum = 0;
let mut a = 1;
loop {
    sum += a;
    a += 1;
    if a == 10 {
        break;
    }
}
```

实际上，以上的三种循环也都是表达式，而且 `loop` 中的 `break` 可以返回这个表达式的值。这里提供一个 `3n + 1` 问题的代码来展示它的表达式本质：

```rust
let mut a = 19112021; // 可以是要验证的任意大整数，只要不越界即可
let must_be_one = loop {
    if a == 1 {
        break a;
    } else if a % 2 == 1 {
        a = 3 * a + 1;
    } else {
        a = a / 2;
    }
}; // must_be_one 的值应当为 1
// 如果你发现程序没有结束，请多等一会
```

#### 循环标签

如果存在嵌套循环，`break`、`continue` 都只作用于此时最内层的循环。在Rust中，你可以为特定循环指定 循环标签（loop label），然后将标签与 break 或 continue 一起使用，使这些关键字作用于所标记的循环，实现跳出多重循环的目的。

在有这个特性之前，「跳出多重循环」其实颇为棘手——因为最优雅的方式是声名狼藉的"goto"。虽然「把循环封装在一个函数内用return跳出」是个好办法，但并不总适合这样做。

```rust
let matrix = vec![
    vec![1, 2, 3],
    vec![4, 5, 6],
    vec![7, 8, 9]
];

let target = 5;
let mut found = false;

'outer: for row in &matrix { // 将循环标签放在循环前面. 格式为 'label
    for &num in row {
        if num == target {
            found = true;
            break 'outer;  // 使用循环标签直接跳出外层循环
        }
    }
}

if found {
    println!("找到了目标元素！");
} else {
    println!("未找到目标元素。");
}
```

## Rust 中的函数

### 函数声明

Rust 中通过 `fn` 关键字声明函数，在函数名后的括号内声明参数（必须指定类型），在 `->` 后面指定返回类型（如果没有，可以不加）。

```rust
fn func_1() {
    println!("Hello");
} // 无参数，无返回值的函数
// 无返回值的函数，会默认返回 单位元 ()

fn func_with_param(i: u32, j: u32) {
    println!("I love you {} times", i + j);
} // 有参数的函数

fn func_with_return_value(i: i32, j: i32) -> i32 {
    return i + j;
} // 有返回值的函数

fn func_with_return_value_mod(i: i32, j: i32) -> i32 {
    i + j
}
// 在有返回值的函数中，return 语句并不是必需的。在这里
// 由大括号包裹的代码块是一个表达式，i + j 就是表达式的值，
// 同样也就是函数的返回值。
```

!!! note "与 C++ 的对照"

    在 C/C++ 中，函数的声明的类型在前，没有额外关键字。读者可能需要一些时间来适应 Rust 的语法。

!!! caution "函数返回值"

    无返回值的函数会默认返回 **单位元** `()`，并非真实语义下的“无返回值”。

    Rust 编译器具有严格的类型检查，如果函数指定了返回值类型，但没有给出返回值或 return 语句，编译器将给出 `mismatched types` 报错。
    
    类似的，如果没给定返回值类型，但返回了 **非单位元** 类型的值，编译器也会给出 `mismatched types` 报错。

### 函数调用

Rust 的函数调用语法与 C/C++ 没有太大区别。

```rust
let a = 1;
let b = 2;
let c = func_with_return_value(a, b);
```

## Rust 的枚举和匹配

### 枚举类型

Rust 的枚举通过关键字 `enum` 定义。

```rust
enum CoinType {
    Dime, // 一角
    Half, // 五角
    Yuan, // 一元
} // 这个枚举量仅仅标定了硬币的类型

struct Coin {
    kind: CoinType,
    value: u32
} // 这个结构体记录了硬币的类型和对应的面值

let coin = Coin {
    kind: CoinType::Dime,
    value: 10
};
```

枚举的每种变体 (variant) 可以:

- 没有数据(单位元变体)
- 有命名的数据域(结构体变体)
- 有不命名的有序数据域(元组变体)

```rust
enum Resultish { 
    Ok,
    Warning { code: i32, message: String },
    Err(String)
}
```

!!! note "与 C++ 的对照"

    C/C++ 的枚举类型底层是整数，不能拥有数据成员。这是 Rust 和 C/C++ 的一个很大的区别。
    枚举类型是 Rust 提供给我们的有力武器。善用枚举类，可以便捷地传递很多数据。

### 匹配

#### `match` 表达式

`match` 表达式可以对枚举量进行匹配。

```rust
enum Operator {
    Add(i32, i32),
    Sub(i32, i32),
    Mul(i32, i32),
    Div(i32, i32),
    Rem(i32, i32)
}

let op = Operator::Add(10, 5);

let value = match op {
    Operator::Add(a, b) => a + b,
    Operator::Sub(a, b) => a - b,
    Operator::Mul(a, b) => a * b,
    Operator::Div(a, b) => a / b,
    _ => a % b // _ 匹配任意值，类似 default
};
```

!!! note "与 C++ 的对照"

    `match` 表达式与 C/C++ 的 `switch-case` 有类似之处，但远比后者强大。读者可能需要花一点时间来适应 Rust 的 `enum` 和 `match` 表达式，然后就可以享受它美妙的模式匹配语法了。

#### `if-let` 表达式

`if-let` 提供了一种简化的模式匹配机制。

```rust
let op = Operator::Add(10, 5);

let value = if let Operator::Add(a, b) = op {
    a + b
} else {
    -1
};
```

## Rust 的结构体

### 结构体类型
!!! note "与 C++ 的对照"

    C++ 的 `struct` 本质上是默认 `public` 的 `class`，因此我们接下来仅讨论 Rust `struct` 和 C++ `class` 的区别。

Rust 中没有“类”的概念，但是保留了结构体。

```rust
struct Person {
    age: u32,
    name: String
}

let alice = Person {
    age: 20,
    name: String::from("Alice")
}
```

### 结构体方法
结构体可以有方法和关联函数，在 `impl` 块中实现。包含 `self`、`&self` 或 `&mut self` 的函数为方法，由 `结构体.方法名()` 调用；不包含的为关联函数，用 `结构体名::关联函数名()` 的方式调用。

```rust
impl Person {
    fn new(age: u32, name: String) -> Self {
        Self {
            age: age,
            name: name
        }
    }
    fn hello(&self) {
        println!("Hello! My name is {}.", name);
    }
}

let bob = Person::new(19, String::from("Bob"));
bob.hello();
```

执行以上代码将输出：

```text
Hello! My name is Bob.
```

!!! note "与 C++ 的对照"

    上文所述的方法和关联函数分别类似 C++ 中的方法和类方法（即在类中由 `static` 修饰的函数，不关联实例对象而关联类本身）。

    在构造和析构方面，由于 C++ 采用 [RAII](https://zh.wikipedia.org/wiki/RAII) 进行内存管理，每一个类都包含一个或多个构造函数以及一个析构函数。Rust 没有构造函数，但我们常用一个关联函数来进行结构体对象的构建（如上文的 `Person::new`）。Rust 采用 `Drop` trait 来管理对象的销毁，关于 trait 的讨论将在后续展开。 

## Rust 的特型

Rust 具有与 C++ 完全不同的面向对象，Rust 中没有继承的机制，对于“不同类共享相同的行为”这样的要求，Rust 使用一个叫做 `trait` 的机制来实现。

!!! note "组合优先于继承"
    Rust 特型机制的核心思想在于**“组合优先于继承”**，这种设计理念使得相比较于 C++ 更关注于抽象的类的继承关系，Rust 更关注每个对象的特性，通过特性的组合来定义一个完整的对象。
    
    比如，我们想要定义一个鸟类，我们在鸟类中实现了非常多的特性。这个时候我们想把企鹅也加入到我们的系统中，企鹅也是鸟，但是企鹅不会飞。那这怎么解决呢？我们不得不重构我们的代码，比如再重新定义一个会飞的鸟和不会飞的鸟，然后共同继承自抽象鸟。然后我们还得把要求输入参数为鸟的函数都给按照实际情况改成抽象鸟或者会飞的鸟。过了一会，蝙蝠又要加入。蝙蝠在飞行方面和鸟很像，但确是哺乳动物，继续重构。不知不觉中我们的代码也越来越抽象了。
    
    那如果用组合该如何解决这个问题呢？我们不必把所有鸟类共性都放到鸟类里面，而是可以把每一个共性单独定义成一个Trait，然后我想要能飞能吃饭且生物学上是鸟类的生物的时候可以把参数约束成Fly+Eat+BiologicallyBird ，只想要飞而不关心是不是鸟的时候可以约束成Fly。这样我们就可以很方便地组合出我们想要的生物了。
    
    （参考自[zhc7](bjhansen2012@outlook.com)的2024暑培讲义）

Rust 的 `trait` 机制通过如下代码实现：

```rust
struct Cat {}

struct Dog {}

trait CanMakeSound {
    fn make_sound(&self) -> String;
}
```

上文定义了一个叫做 `CanMakeSound` 的 `trait`，在其中声明了 `make_sound` 方法而没有实现。如果要为一个类型实现 `trait`，则需要实现该 `trait` 的所有方法。实现 `trait` 的语法形如 `impl 特性名 for 类型名`。

```rust
impl CanMakeSound for Cat {
    fn make_sound(&self) -> String {
        String::from("Meow")
    }
}

impl CanMakeSound for Dog {
    fn make_sound(&self) -> String {
        String::from("Woof")
    }
}
```

在一个类型实现该 `trait` 后，这个类型的变量就可以使用其方法。

```rust
let cat = Cat {};
let dog = Dog {};

println!("{}\n{}", cat.make_sound(), dog.make_sound());
```
`trait` 可以拥有默认实现。

```rust
pub trait Fly {
    fn fly(&self) {
        println!("Taking off!");
    }
}
```

也可以实现多重 `trait`。

```rust
pub trait HaveWings() {
    fn flap(&self);
}

pub trait HaveLegs() {
    fn walk(&self);
}

pub trait CanFly(): HaveWings + HaveLegs {
    fn fly(&self);
    fn land(&self);
}
```

!!! note "与 C++ 的对照"

    在 C++ 中，不同类要想共享行为，则需要声明一个基类，将希望共享的行为声明为基类中的虚函数，然后分别继承该基类并重载希望共享的函数。例如，对上文的 `Cat` 和 `Dog`，在 C++ 中会这样实现：

    ```C++
    class CanMakeSound {
        virtual std::string make_sound() = 0;
    };
    class Cat : public CanMakeSound {
        std::string make_sound() override {
            return "Meow";
        }
    };
    class Dog : public CanMakeSound {
        std::string make_sound() override {
            return "Woof";
        }
    };
    ```

如果仅仅是直接进行方法调用，那么使用或不使用 `trait` 看起来并无太大区别。但 `trait` 还可以用于函数参数的声明，这样就可以对参数类型加以限定而不需要完全确定类型：

```rust
fn animal_make_sound(animal: impl CanMakeSound) -> String {
    animal.make_sound()
}
```

事实上，这是 `Trait Bound` 语法的一个语法糖。如果展开写则形式如下：

```rust
fn animal_make_sound<T: CanMakeSound>(animal: T) -> String {
    animal.make_sound()
}
```

`Trait Bound` 也可以不仅包含一个 `trait`。

```rust
fn some_function<T: Display + Clone, U: Clone + Debug>(t: T, u: U) -> i32;
// 此处的 Display、Clone 和 Debug 都是 rust 语言提供的 trait
```

也可以采用 `where` 从句来简化过长的 `Trait Bound`。

```rust
fn some_function<T, U>(t: T, u: U) -> i32
    where T: Display + Clone, U: Clone + Debug;
```

!!! note "Rust 提供的 traits"
    事实上，Rust 的标准库 `std` 提供了非常多好用的 `trait`，你可以直接通过 `#[derive()]` 的方式，快捷地为你的结构体实现指定 `trait`。
    这里给出一些常用的 trait：
    
    `Debug`: 可以用 `println!("{:?}", my_struct)` 来打印结构体的调试信息。

    `Clone`: 可以使用 `my_struct.clone()` 创建结构体的副本。

    `PartialEq`: 可以使用 `==` 和 `!=` 进行结构体对象之间的部分相等性比较。如果要实现完全相等性比较，可以使用 `Eq`。

    `PartialOrd`: 可以使用 `<`、`<=`、`>`、`>=` 进行比较。

    更多 `trait` 可以参考 [Rust std 官方文档](https://doc.rust-lang.org/std/index.html)

## Rust 的泛型

Rust 中的泛型通过如下方式实现：

### 泛型函数
```rust
fn foo<T, U>(x: T, y: U) {
}
```

### 泛型枚举
```rust
enum Result<T, E> {
    Ok(T),
    Err(E), 
}
```

### 泛型结构体
```rust
struct Point<T> {
    x: T,
    y: T, 
}

impl<T> Point<T> // 在 impl 代码段开头声明泛型
where
    T: std::ops::Add<Output = T> + std::ops::Mul<Output = T> + Copy,
{
    fn distance_from_origin(&self) -> T {
        self.x * self.x + self.y * self.y
    }
}
```

### Option 和 Result 类型
Rust 提供了两个非常方便的枚举类型：`Option` 和 `Result`。
```rust
enum Option<T> { 
    None,
    Some(T), 
}

enum Result<T,E> {
    Ok(T),
    Err(E),
}
```
合理地运用这两个枚举类型，可以便捷地传递参数、捕获错误。

```rust
fn eat(food: Option<String>) {
    match food {
        Some(c) => println!("Nice {}! I'm full.",c),
        None => println!("Nothing to eat. I'm hungry!"),
    }
}

fn divide(a: i32, b: i32) -> Result<i32, String>{
    if b == 0 {
        return Err(String::from("Division by zero"));
    }

    Ok(a / b)
}
```

!!! note "Option 与 Result 的数据获取"
    Rust 为 `Option` 和 `Result` 类型提供了 `unwrap()` 和 `expect()` 等方法进行快速的数据获取，可以绕开冗余的模式匹配。但程序员需要自己确保 `Option` 对应的类型为 `Some(_)`（`Result` 为 `Ok(_)`），否则会导致程序`panic`退出。

    ```rust
    fn main() {
        let a:Option<String> = Some("hello".to_string());
        let b: Result<_,&str> = Err("world");
        let content = a.unwrap() + " " + b.expect("Empty content"); // If a is None or b is Err, this will panic.
        // a is None: thread 'main' panicked at ...:
        // called `Option::unwrap()` on a `None` value
        // b is Err:thread 'main' panicked at ...:
        // Empty content: "world"
        println!("{}",content);
    }
    ```

