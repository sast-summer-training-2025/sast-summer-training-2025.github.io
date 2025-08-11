## Java简介

Java 是一种**面向对象、跨平台、功能强大**的编程语言，由Sun Microsystems（后被Oracle公司收购）于1995年发布。  其设计理念是**一次编写，到处运行 (Write Once, Run Anywhere)**，通过 Java 虚拟机 (JVM) 实现跨平台运行。

## 主要特点

- 跨平台性 
  只要安装了JVM，Java 程序就能在Windows、macOS、Linux等不同操作系统上运行。

- 面向对象 
  Java 完全支持面向对象编程 (OOP)，包括封装、继承、多态三大特性。

- 安全性与稳定性 
  Java 有严格的语法规范和内存管理机制（自动垃圾回收），程序更加安全稳定。

- 丰富的类库 
  Java 提供了庞大的标准类库 (Java API)，支持网络编程、数据库开发、多线程等。

- 多线程支持 
  内置多线程机制，方便编写高并发程序。

## 基本语法

### 注释

Java提供了三种主要的注释方式：

```
// 这是一个单行注释

/*
  这是一个多行注释
  可以用于注释一段代码
*/

/**
 * 这是文档注释
 * @author Alice
 * @version 1.0
 * 可以后续用javadoc工具提取
 */
```

### main方法结构

Java 应用程序的入口是 `main()` 方法。其标准定义格式如下：

```
public class Hello { // public属性
    public static void main(String[] args) {  // static：无需创建对象即可调用；返回值为void
        System.out.println("Hello, world!");
    }
}
```

每个Java应用都必须有一个包含 `main` 方法的类作为程序起点。

### 包与导入

package语句用于声明类所在的包路径，通常对应于文件系统中的目录结构。如以下包定义：

```
package com.example.myapp;

public class Example{
	public static void main(String[] args) {  
    	...
    }
}
// 对应目录的组织结构：com/example/myapp/Example.java
```

注意包语句必须是源文件的第一条语句；

import语句用于导入其他包中的类或接口，可导入标准库或自定义包；若使用的是当前包内的类或 `java.lang` 包（如 `String`、`Math`）或使用类的完整类名（如 `java.util.Scanner`）时，可省略 import。

```
import java.util.Scanner;  // 导入 util 包中的Scanner类
import java.util.*;  // *是通配符，导入整个 util 包中的所有类
```

### 基本数据类型

| 类型    | 位数 | 示例值       | 说明                              |
| ------- | ---- | ------------ | --------------------------------- |
| byte    | 8    | 127          | 有符号整数，范围 -128 ~ 127       |
| short   | 16   | 32000        | 有符号整数，范围 -65536 ~ 65535   |
| int     | 32   | 100000       | 默认整数类型                      |
| long    | 64   | 9999999999L  | 后缀L与int区分                    |
| float   | 32   | 3.14f        | 后缀f与double区分                 |
| double  | 64   | 3.14159      | 默认浮点数                        |
| boolean | 1    | true / false | 逻辑类型，与C语言中的"bool"区分   |
| char    | 16   | 'A'          | 表示单个 Unicode 字符，注意有16位 |

### 引用数据类型

引用类型的变量不直接存储数据本身，而是存储一个地址（引用），指向堆内存中的对象实例。

#### 数组

java推荐将`[]`放在数据类型和数组名之间，参考以下定义：

```
int[] scores = {90, 85, 100};
char[] charArray = {'a', 'b', 'c', 'd', 'e'};
```

#### 类

自定义或标准库中定义的类都是引用类型，如：

```
String name = "Alice";  
Scanner sc = new Scanner(System.in);  // Scanner是标准库类
Myclass myclass = new Myclass();  // Myclass是自定义类
```

#### 接口与枚举

### 字符串

#### 不可变字符串：String

Java 中的字符串是不可变对象。一旦字符串对象被创建，其值就不能被更改。

```
String s = "Hello";
s = s + " World";
System.out.println(s);
```

虽然输出的是 `"Hello World"`，但其实 `"Hello"` 并没有被改变，而是创建了一个新的字符串对象。

#### 可变字符串类：StringBuilder 与 StringBuffer

当你需要频繁修改字符串内容时，比如在循环中拼接大量字符串，使用 `String` 会频繁创建新对象，效率低下。这时可以使用`String Builder`和`StringBuffer`：

```
StringBuilder sb = new StringBuilder();
sb.append("Java");
sb.append("is fun");
System.out.println(sb.toString()); // 非线程安全，适用于单线程环境

StringBuffer sb = new StringBuffer("Hello");
sb.append(" World");
System.out.println(sb.toString());  // 比StringBulider慢，但使用了synchronized，适用于多线程环境
```

### 运算符

Java中算术运算符和逻辑运算符与C语言中基本相同，这里不做赘述；特别需要注意的是逻辑右移 `>>>`和等于`==`。

- 区分`>>` 与 `>>>`：


| 运算符 | 含义         | 高位补什么         |
| ------ | ------------ | ------------------ |
| `>>`   | 算术右移     | 补符号位（保符号） |
| `>>>`  | **逻辑右移** | 始终补 0（无符号） |

```
int x = -4;  // 二进制补码表示：11111111 11111111 11111111 11111100
System.out.println(x >> 1);   // 算术右移，保留负数符号，高位补 1，输出 -2
System.out.println(x >>> 1);  // 逻辑右移，高位补 0， 输出 2147483646
```

- 使用 `.equals()` 比较内容：

  在 **Java 中 `==` 比较的是引用（对象地址）**，不是对象内容；
  而 C 语言中 `==` 用来比较值。

  ```
  String a = new String("Java");
  String b = new String("Java");
  System.out.println(a == b);       // false（不同对象）
  System.out.println(a.equals(b));  // true（内容相同）
  ```

### 输入输出

#### 输出语句

```
System.out.println("This is the first line");
System.out.print("This is a new line.");
System.out.print("No new line here.");
System.out.printf("圆周率保留两位小数：%.2f\n", 3.14159); 
```

`System.out` 是标准输出流，默认指向控制台；`println()` 输出完毕后会自动换行；

`print()` 输出完毕后不换行；`printf()` 可用于格式化输出（类似C语言）：

#### 输入语句

```
import java.util.Scanner;  // 先导入标准库

Scanner sc = new Scanner(System.in);  // 创建 Scanner 对象
System.out.print("Enter your name：");
String name = sc.nextLine();          // 接收字符串
System.out.print("Enter your age：");
int age = sc.nextInt();               // 接收整数

sc.close(); // 关闭输入流
```

附常用的`scanner`方法

| 方法名        | 示例输入            | 说明         |
| ------------- | ------------------- | ------------ |
| next()        | hello world → hello | 读取一个单词 |
| nextLine()    | hello world         | 读取一整行   |
| nextInt()     | 42                  | 读取int      |
| nextDouble()  | 3.14                | 读取double   |
| nextBoolean() | true/false          | 读取boolean  |

### 控制语句

`if-else`, `switch`, `while`, `for`等语法和C语言基本相同，大家可以结合示例代码进行学习。

```
// 这段代码用于演示控制流语句

package examples;

import java.util.Scanner;

public class ControlFlow {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // if-else 条件判断
        System.out.print("Enter an integer: ");
        int number = scanner.nextInt();

        if (number > 0) {
            System.out.println("The number is positive.");
        } else if (number < 0) {
            System.out.println("The number is negative.");
        } else {
            System.out.println("The number is zero.");
        }

        // switch 多分支结构
        System.out.print("Enter a number for day of week (1-7): ");
        int day = scanner.nextInt();

        switch (day) {
            case 1:
                System.out.println("Today is Monday.");
                break;
            case 2:
                System.out.println("Today is Tuesday.");
                break;
            case 3:
                System.out.println("Today is Wednesday.");
                break;
            default:
                System.out.println("Today is another day.");
        }

        // for 循环：输出 1~5
        for (int i = 1; i <= 5; i++) {
            System.out.print(i + " ");
        }
        System.out.println();

        // while 循环：输出 5~1
        int count = 5;
        while (count > 0) {
            System.out.print(count + " ");
            count--;
        }
        System.out.println();

        // break 和 continue
        for (int i = 0; i < 10; i++) {
            if (i == 3) {
                continue;
            }
            if (i == 7) {
                break;
            }
            System.out.print(i + " ");
        }

        scanner.close();
    }
}
```

## 面向对象编程

### 类（Class）

Java 最初的设计目标之一就是成为一种纯粹的面向对象语言。所有的代码都必须包含在类（Class）中，几乎所有元素都是对象（除了8种基本数据类型）。它支持封装、继承和多态等面向对象的核心概念，程序的组织结构高度模块化。具体地说，**所有的 Java 代码都需要封装在类里，每一个 `.java` 文件恰有一个与其同名的 `public` 类**。

> 面向对象编程的基本流程为：
>
> 1. 设计类 `class Car { /* ... */ }`
> 2. 创建/实例化对象 `Car myCar = new Car();`
> 3. 向对象发送消息 `myCar.move();`

Java 使用垃圾回收（Garbage Collection，GC）机制进行内存管理。开发者不需要显式地分配和释放内存，这减轻了开发负担并减少了内存泄漏和悬挂指针等常见的错误。也就是说，**Java 没有指针的概念**。函数传参**只有传值没有传引用**。Java 程序员只需要关心何时 `new` 一个对象，而不需要考虑何时 `delete` 它。

java类修饰符的访问规则如下：

| 修饰符    | 类内 | 同包 | 子类 | 外部类 |
| --------- | ---- | ---- | ---- | ------ |
| public    | Yes  | Yes  | Yes  | Yes    |
| protected | Yes  | Yes  | Yes  | No     |
| private   | Yes  | No   | No   | No     |

#### 构造函数

和C语言类似，构造函数用于创建对象并初始化状态。若无显式构造函数，Java 会提供默认无参构造函数。

```
public class Book {
    String title;
    String author;

    public Book(String title, string writer) {
        this.title = title;
        author = writer;
    }
}
```

析构函数（C++ 中的 `~ClassName()`）在 Java 中不存在，Java 采用自动垃圾回收（Garbage Collection）来释放对象内存。虽然 Java 提供了 `finalize()` 方法，但它已被废弃，不推荐使用。

#### static关键字

在 Java 中，`static`是一个非常重要的关键字，用于修饰类的成员（变量/方法），表示该成员属于类本身，而不是某个具体的实例。所以使用static修饰的成员可以不实例化对象而通过类直接访问使用。

```
public class Counter {
    static int count = 0; // 所有实例共享

    public Counter() {  // 构造函数
        count++;
    }

    public static void printCount() {
        System.out.println("Total: " + count);
    }
}

public class Main {
    public static void main(String[] args) {
        new Counter();
        new Counter();
        new Counter();
        Counter.printCount(); // 通过类名直接调用静态方法
    }
}
```

在这段代码中，`count`是一个静态变量，属于Counter类，所有创建的 `Counter` 实例共享这一个变量。不管创建多少个对象，`count` 变量在内存中只有**一份**。

`printCount()`是一个**静态方法**。它不能访问非静态成员（即不能使用 this），但可以访问静态变量 `count`。它的调用不依赖于对象实例，可以直接通过类名调用，如`Counter.printCount(); `

#### 实例初始化块

实例初始化块（在类中用大括号括起来 `{ ... }`） 会在构造函数前自动执行，常用于多个构造函数中共享逻辑。

```
public class InitBlock {
    {
        System.out.println("Instance initializer runs");  // 实例初始化块
    }

    public InitBlock() {
        System.out.println("Constructor runs");
    }
}
```

#### final关键字

`final` 变量一旦赋值就不能再修改，用来定义常量。通常与 `static` 搭配用于定义全局常量，变量的命名采用 `SCREAMING_SNAKE_CASE`（字母大写，用下划线分割）：

```
public class MathConstants {
    public static final double PI = 3.14159;
    public static final int MAX_SIZE = 1000;
}
```

`final`定义的方法不能被子类重写，这是为了防止继承关系中对方法行为的修改，确保方法的实现在整个继承体系中保持一致性和安全性。

```
// Parent.java
public class Parent {
    public final void display() {
        System.out.println("Final method in Parent");
    }
}

// Child.java
public class Child extends Parent {
    // ❌ 编译错误：不能重写 final 方法
//    @Override
//    public void display() {
//        System.out.println("Trying to override");
//    }
}
```

#### 组合

组合是类的一种“拥有”(has-a)关系，即一个类将另一个类的对象作为**成员变量**使用。

```
class Engine {
    void start() {
        System.out.println("Engine starts");
    }
}

class Car {  // a car has an engine
    private Engine engine = new Engine(); 

    void drive() {
        engine.start();  // 通过组合来使用 Engine 的功能
        System.out.println("Car is moving");
    }
}
```

#### 继承

```
static class Animal {
    int age, weight;

    public Animal(int age, int weight) {
        this.age = age;
        this.weight = weight;
    }

    void makeSound() {
        System.out.println("Make sound");
    }
}

static class Dog extends Animal {
    String color;

    Dog(int age, int weight, String color) {
        super(age, weight);
        this.color = color;
    }

    @Override
    void makeSound() {
        System.out.println("Bark.");
    }
}

static class Cat extends Animal {
    String name;

    Cat(int age, int weight, String name) {
        super(age, weight);
        this.name = name;
    }

    @Override
    void makeSound() {
        System.out.println("Meow.");
    }
}

public class Main{
    public static void main(String[] args) {
        Dog dog = new Dog(3, 25, "White");
        Cat cat = new Cat(4, 4, "Kitty");
        dog.makeSound();
        cat.makeSound();
    }
}
```

`Animal` 是一个父类，`Dog` 和 `Cat` 是 `Animal` 的子类，使用了 `extends` 关键字建立**继承关系**，`Dog` 和 `Cat` 都继承了 Animal 的属性和方法，包括：

- `int age, weight`（变量）
- `void makeSound()` （方法）

**子类的构造函数**

使用 `super(age, weight)` 明确调用父类构造方法初始化 `age` 和 `weight`，子类自己负责初始化自己的新字段：`color`、`name`

**方法重写（Override）**

`@Override` 表示子类重写了父类的 `makeSound()` 方法：`Dog` 输出 “Bark.”，`Cat` 输出 “Meow.”，而不是父类默认的 “Make sound”

#### 抽象类

在刚才继承的代码示例中，我们会发现，`Animal` 类的 `makeSound()` 方法并没有被调用；这个方法被所有继承 `Animal` 类的子类都重写了。我们可以将 `Animal` 类实现为一个抽象类。抽象类是一种**不能被实例化**的类，它通常被用作其他类的基类。抽象类可以包含抽象方法，这些方法没有具体的实现，就像 C++ 中的纯虚函数一样。

```
public abstract class Animal{}
    int age, weight;

    public Animal(int age, int weight) {
        this.age = age;
        this.weight = weight;
    }

    // 抽象方法：没有方法体，必须被子类实现
    public abstract void makeSound();

    // 普通方法：可以被继承
    public void sleep() {
        System.out.println("Sleeping zzz...");
    }
}
```

#### 接口

在 Java 中，接口（interface）是一种特殊的抽象类型，它规定了一组类必须实现的方法。接口只包含方法的声明（默认为 `public abstract`）和常量（默认为 `public static final`），而实现接口的类必须实现接口中声明的所有方法。

接口的定义方式如下：

```
interface 接口名 {
    // 常量
    类型 常量名 = 值;

    // 抽象方法
    返回类型 方法名(参数列表);
}
```

可以结合以下代码理解：

```
interface Animal {
    void makeSound(); // 抽象方法
    void eat();
}

// 接口的实现类
class Dog implements Animal {
    @Override
    public void makeSound() {
        System.out.println("Bark");
    }

    @Override
    public void eat() {
        System.out.println("Dog is eating");
    }
}

class Cat implements Animal { // 不同类实现同一接口
    @Override
    public void makeSound() {
        System.out.println("Meow");
    }

    @Override
    public void eat() {
        System.out.println("Cat is eating");
    }
}

public class Main {
    public static void main(String[] args) {
        Animal myDog = new Dog();
        Animal myCat = new Cat();

        myDog.makeSound(); 
        myCat.makeSound(); 

        myDog.eat();      
        myCat.eat();      
    }
}
```

在以上代码中，Dog和Cat类用关键字`implements`实现了接口`Animal`。对比之前的抽象类，可能有同学会好奇为什么还要再定义接口。最主要的原因就是 Java 中**类只能单继承**，一个类不能同时继承多个抽象类（“菱形问题”），但接口可以多实现，也就是一个类可以实现多个接口，让 Java 类可以获得多种行为。

## 异常处理

在 Java 程序运行过程中，如果出现了 非正常的情况（如除零、文件找不到、网络中断等），程序会抛出一个异常对象，导致当前方法中断执行。

Java 中所有异常类都继承自 `java.lang.Throwable`，可分为两大类：

- **Error**：表示严重错误，程序无法处理，如内存溢出（OutOfMemoryError）等
- **Exception**：表示程序可以处理的异常

其中 `Exception` 又分为：

| 类型                | 描述                                                         |
| ------------------- | ------------------------------------------------------------ |
| Checked Exception   | 编译器检查，必须处理，例如：`IOException`、`SQLException`    |
| Unchecked Exception | 运行时异常，不强制处理，例如：`NullPointerException`、`ArithmeticException` |

Java 提供以下关键词（"try-catch-finally"）进行异常处理：

```
try {
    // 可能发生异常的代码
} catch (ExceptionType name) {
    // 捕获异常后的处理代码
} finally {
    // 无论是否发生异常，都会执行
}
```

以下是示例代码：

```
public class ExceptionDemo {
    public static void main(String[] args) {
        try {
            int result = 10 / 0;  // 除零错，会抛出 ArithmeticException
        } catch (ArithmeticException e) {
            System.out.println("Caught an exception: " + e.getMessage());
        } finally {
            System.out.println("This always executes.");
        }
    }
}
```

java中还可以手动抛出异常对象和自定义异常类，代码如下：

```
class InvalidAgeException extends Exception {  // 自定义异常类，继承自Exception类
    public InvalidAgeException(String message) {
        super(message);
    }
}

public class ExceptionDemo {
    public static void main(String[] args) {
        try {
            processUser("Alice", 17);  // 年龄小于18，触发自定义异常
            processUser("Bob", 25);    // 正常流程
            int[] nums = new int[3];
            System.out.println(nums[5]); // 数组越界异常
        } catch (InvalidAgeException e) {
            System.out.println("Custom Exception: " + e.getMessage());
        } catch (ArrayIndexOutOfBoundsException e) {
            System.out.println("Array Exception: " + e.getMessage());
        } catch (Exception e) {
            System.out.println("General Exception: " + e.getMessage());
        } finally {
            System.out.println("Resource cleanup in finally block.");
        }
    }

    // 声明可能抛出自定义异常
    public static void processUser(String name, int age) throws InvalidAgeException {
        if (age < 18) {
            throw new InvalidAgeException("User " + name + " is underaged!");
        } else {
            System.out.println("User " + name + " is allowed.");
        }
    }
}
```

`InvalidAgeException` 是一个用户自定义的异常类，它通过 `extends Exception` 继承了 Java 的标准异常体系，是一个 Checked 异常。构造方法中调用 `super(message)`，把错误信息传递给父类的 `Exception`，从而可以通过 `getMessage()` 获取异常原因。

`throw` 是一个 Java 关键字，用于手动抛出一个异常对象。后面必须跟一个 `Throwable` 类型的实例（可以是 `Exception` 或 `Error` 的子类）。抛出异常后，该方法的后续代码不会再执行，控制权转移到上层的 `catch` 块或调用者。

区分`throw` 和 `throws` ：

- `throw` 是语句，用于“抛出”一个具体的异常对象；
- `throws` 是方法签名的一部分，声明这个方法可能“抛出某种类型的异常”。

## Java 标准库

正如C++中的STL一样，Java 也提供了功能强大的标准类库，包含丰富的工具类和数据结构。

#### Math 类

用于执行基本数学运算，如三角函数、对数、平方根等。

```
System.out.println(Math.sqrt(16));      // 输出 4.0
System.out.println(Math.pow(2, 3));     // 输出 8.0
System.out.println(Math.random());      // 输出 [0.0, 1.0) 范围的随机数
```

#### BigInteger / BigDecimal

`BigInteger` 和 `BigDecimal` 是 Java 中用于处理大数和高精度计算的两个类。它们属于 `java.math` 包。

- **`BigInteger`** 类用于表示整数值，它不受 Java 内置的 `int` 和 `long` 类型所受的固定大小限制。`BigInteger` 可以处理任意精度的整数，包括非常大的数值，
- **`BigDecimal`** 类用于表示具有精确小数位的小数值，它提供了对小数点后任意位数的精确控制。`BigDecimal` 常用于需要高精度计算的金融领域。

```
import java.math.BigInteger;
import java.math.BigDecimal;

BigInteger big1 = new BigInteger("12345678901234567890");
BigInteger big2 = new BigInteger("98765432109876543210");
System.out.println(big2.add(big1));

BigDecimal d1 = new BigDecimal("3.1415926535");
BigDecimal d2 = new BigDecimal("2.7182818284");
System.out.println(d1.multiply(d2));
```

#### Arrays 与 ArrayList

数组（Arrays）是 Java 中最基本的数据结构，与C语言中的数组基本相同，定义在`java.util`包中。

```
import java.util.Arrays;

public class ArrayExample {
    public static void main(String[] args) {
        // 创建并初始化数组
        int[] numbers = {10, 20, 30, 40, 50};

        // 遍历数组
        for (int i = 0; i < numbers.length; i++) {
            System.out.println("Element at index " + i + ": " + numbers[i]);
        }

        // 使用 Arrays 工具类
        java.util.Arrays.sort(numbers); // 排序
        System.out.println("Sorted: " + .Arrays.toString(numbers));  // 转化为string
    }
}
```

`ArrayList` 属于集合框架，提供了动态数组的功能，也定义在 `java.util` 包中。

```
import java.util.ArrayList;

public class ArrayListExample {
    public static void main(String[] args) {
        // 创建 ArrayList，存储字符串
        ArrayList<String> names = new ArrayList<>();

        // 添加元素
        names.add("Alice");
        names.add("Bob");
        names.add("Charlie");

        // 插入元素
        names.add(1, "David");  

        // 获取元素
        String name = names.get(2);
        System.out.println("Element at index 2: " + name);

        // 删除元素
        names.remove("Alice");      // 按值删除
        names.remove(0);            // 按索引删除

        // 遍历列表
        for (String n : names) {
            System.out.println("Name: " + n);
        }

        // 获取大小
        System.out.println("Total: " + names.size());
    }
}
```

#### LinkedList

`LinkedList` 是 Java 集合框架中的一个双向链表实现，位于 `java.util` 包下。它是 `List` 接口的一个具体实现类，与 `ArrayList` 相比，在插入、删除元素时性能更优。

```
import java.util.LinkedList;

public class LinkedListExample {
    public static void main(String[] args) {
        // 创建 LinkedList，存储字符串
        LinkedList<String> fruits = new LinkedList<>();

        // 添加元素
        fruits.add("Apple");
        fruits.add("Banana");
        fruits.add("Cherry");

        // 在头部和尾部添加
        fruits.addFirst("Mango");
        fruits.addLast("Orange");

        // 获取元素
        System.out.println("First: " + fruits.getFirst()); // Mango
        System.out.println("Last: " + fruits.getLast());   // Orange

        // 遍历链表
        for (String fruit : fruits) {
            System.out.println("Fruit: " + fruit);
        }

        // 删除元素
        fruits.removeFirst();   // 删除头部
        fruits.removeLast();    // 删除尾部
        fruits.remove("Banana");

        System.out.println("After deletion: " + fruits);
    }
}
```

##### java中的栈和队列

由于 `LinkedList` 同时实现了 `Deque` 接口，可以用来模拟：

-  栈（Stack）

```
LinkedList<Integer> stack = new LinkedList<>();
stack.push(10);  // 入栈
stack.push(20);
System.out.println(stack.pop()); // 出栈
System.out.println(stack.peek()); // 查看栈顶
```

- 队列（Queue）

```
LinkedList<String> queue = new LinkedList<>();
queue.offer("A");  // 入队
queue.offer("B");
System.out.println(queue.poll()); // 出队
System.out.println(queue.peek()); // 查看队头
```

#### HashMap

`HashMap` 用于存储键值对（key-value）映射，位于 `java.util` 包中。每个键（Key）只能出现一次，重复插入会覆盖旧值，而值可以重复，即多个键可以映射到同一个值

```
import java.util.HashMap;

public class HashMapExample {
    public static void main(String[] args) {
        // 创建 HashMap，键为 String，值为 Integer
        HashMap<String, Integer> scores = new HashMap<>();

        // 添加键值对
        scores.put("Alice", 90);
        scores.put("Bob", 85);
        scores.put("Charlie", 95);

        // 更新键对应的值（Bob 原本为 85）
        scores.put("Bob", 88);

        // 获取值
        int aliceScore = scores.get("Alice");
        System.out.println("Alice's score: " + aliceScore);

        // 判断键或值是否存在
        System.out.println(scores.containsKey("Charlie"));
        System.out.println(scores.containsValue(100));

        // 遍历 HashMap
        for (String name : scores.keySet()) {
            int score = scores.get(name);
            System.out.println(name + ": " + score);
        }

        // 删除键值对
        scores.remove("Alice");
        System.out.println("After removal: " + scores);
    }
}
```

#### HashSet

`HashSet` 是存储**不重复元素**的集合类，位于 `java.util` 包中。

```
import java.util.HashSet;

public class HashSetExample {
    public static void main(String[] args) {
        HashSet<String> names = new HashSet<>();

        // 添加元素
        names.add("Alice");
        names.add("Bob");
        names.add("Charlie");

        // 尝试添加重复元素
        boolean added = names.add("Alice");  // 返回 false，不会添加
        System.out.println("Was 'Alice' added again? " + added);

        // 判断是否包含元素
        System.out.println("Contains Bob? " + names.contains("Bob"));

        // 删除元素
        names.remove("Charlie");

        // 遍历集合（无序）
        for (String name : names) {
            System.out.println("Name: " + name);
        }

        System.out.println("Total size: " + names.size());
    }
}
```

利用HashSet的性质可以进行去重：

```
        // ArrayList 去重
        ArrayList<String> list = new ArrayList<>(Arrays.asList("Tom", "Jerry", "Tom", "Anna", "Jerry"));
        System.out.println("\nOriginal list with duplicates: " + list);

        HashSet<String> uniqueSet = new HashSet<>(list);  // 自动去重
        System.out.println("Set after removing duplicates: " + uniqueSet);
```

## Object 类

在 Java 中，`Object` 类是所有类的基类，也就是说，每一个类（无论是标准库的还是用户自定义的）都直接或间接继承自 `java.lang.Object`。`Object` 类提供了一些基本方法，这些方法必须在子类中正确实现。

以下介绍几种`object`类提供的方法：

#### toString() 

默认实现：返回对象的类名 + “@” + 哈希码的十六进制形式。

通常我们会重写 `toString()` 方法，让它返回更具可读性的内容：

```
public class Person {
    String name;
    int age;

    public Person(String name, int age) {
        this.name = name;
        this.age = age;
    }

    @Override
    public String toString() {
        return "Person[name=" + name + ", age=" + age + "]";
    }
}

public class Main {
    public static void main(String[] args) {
        Person p = new Person("Alice", 25);
        System.out.println(p);  // 自动调用 p.toString()
    }
}
```

#### equals() 

用于比较对象的内容是否相同，通常应当根据对象的内容进行重写：

```
@Override
public boolean equals(Object obj) {
    if (this == obj) return true;
    if (obj == null || getClass() != obj.getClass()) return false;
    Person other = (Person) obj; // 转化成Person类对象
    return age == other.age && name.equals(other.name);  // 依次比较各个成员
}
```

#### hashCode() 

哈希码是用于哈希表（如 `HashMap` 和 `HashSet`）中快速查找对象的关键。正确实现哈希码对于这些数据结构的性能至关重要。如果两个对象通过 `equals()` 方法比较相等，则它们的哈希码也必须相等。同样的，不同对象的哈希码应尽可能不同，这有助于减少哈希冲突。

```
@Override
public int hashCode() {
    return Objects.hash(name, age);  // 使用objects提供的哈希函数
}
```

## 包装类

在 Java 中，基本数据类型是预定义的，它们是原始类型，直接存储在内存中，而不是对象。而包装类则用于将基本数据类型包装为对象。以下是一些基本数据类型和对应的包装类对象：

Java 为每种基本数据类型提供了对应的包装类：

| 基本数据类型 | 包装类    |
| ------------ | --------- |
| byte         | Byte      |
| short        | Short     |
| int          | Integer   |
| long         | Long      |
| float        | Float     |
| double       | Double    |
| char         | Character |
| boolean      | Boolean   |

这些类都定义在 `java.lang` 包中，默认可以直接使用，无需导入。

包装类提供了一些常用的静态方法：

- `valueOf()`：将字符串转换为包装类对象

```
Integer intObj = Integer.valueOf("123");
Double doubleObj = Double.valueOf("3.14");
```

- `parseXxx(String)`：将字符串解析为基本类型

```
int i = Integer.parseInt("456");
double d = Double.parseDouble("6.28");
```

- `toString()`：将包装类对象转换为字符串

```
String s = Integer.valueOf("789").toString(); 
```

包装类对象的**比较**要注意以下几点：

- 使用 `.equals()` 比较数值是否相等；
- 使用 `==` 会比较**引用地址**是否相同（[-128, 127]以内的整数会被缓存）：

```
Integer a = 127;
Integer b = 127;
Integer c = 128;
Integer d = 128;

System.out.println(a == b); // true
System.out.println(c == d); // false, 超出缓存范围
System.out.println(c.equals(d)); // true
```

由于Java 的泛型编程不支持基本类型，所以在使用集合类的时候应该使用包装类，例如：

```
ArrayList<int> list; // 编译错误
ArrayList<Integer> list = new ArrayList<>();
```

#### 自动装箱和自动拆箱

自动装箱和拆箱的本质是类型转换，对应的转换如下：

**自动装箱**：基本类型 → 包装类对象

**自动拆箱**：包装类对象 → 基本类型

```
public class WrapperExample {
    public static void main(String[] args) {
        int x = 10;
        Integer obj = x;  // 自动装箱：int → Integer
        int y = obj;      // 自动拆箱：Integer → int

        System.out.println("x = " + x);
        System.out.println("obj = " + obj);
        System.out.println("y = " + y);
    }
}
```

## 线程入门

**线程（Thread）是程序执行的最小单位**，是程序内部的一个独立执行流程。一个程序运行时至少有一个线程，称为主线程（`main()`）。Java 中每个线程由 `java.lang.Thread` 类的对象表示。

> 线程也被称为“轻量级进程”，相比进程，它们之间的切换和通信成本更低。

------

#### 创建线程的方式

1. 继承 `Thread` 类

   ```
   class MyThread extends Thread {
       public MyThread(String name) {
           super(name); // 设置线程名
       }
   
       @Override
       public void run() {
           for (int i = 0; i < 5; i++) {
               System.out.println(i + " " + getName());
               try {
                   Thread.sleep((int)(Math.random() * 1000)); // 模拟延迟
               } catch (InterruptedException e) {}
           }
       }
   }
   
   public class ThreadDemo {
       public static void main(String[] args) {
           new MyThread("First").start();
           new MyThread("Second").start();
       }
   }
   ```

2. 实现`Runnable`接口：

   ```
   class MyRunnable implements Runnable {
       public void run() {
           for (int i = 0; i < 5; i++) {
               System.out.println("Running " + i);
               try {
                   Thread.sleep(500);
               } catch (InterruptedException e) {}
           }
       }
   }
   
   public class RunnableDemo {
       public static void main(String[] args) {
           Thread thread = new Thread(new MyRunnable());
           thread.start();
       }
   }
   ```

#### 线程的生命周期

Java 中的线程有五种主要状态：

1. **新建**：用 `new` 创建线程对象，但未启动。
2. **就绪**：调用 `.start()` 后，等待 CPU 分配时间片。
3. **运行**：获得 CPU，开始执行 `run()` 方法。
4. **阻塞**：例如 `sleep()`、`wait()`、等待 I/O 等。
5. **死亡**：`run()` 方法执行完毕，或被异常终止。

以下是线程调度的一些常见方法：

| 方法                      | 说明                                                         |
| ------------------------- | ------------------------------------------------------------ |
| `start()`                 | 启动线程（进入就绪状态，等待 CPU 调度）                      |
| `run()`                   | 线程执行的任务逻辑（通常不直接调用，而是由 `start()` 内部调用） |
| `sleep(ms)`               | 让当前线程休眠指定毫秒时间                                   |
| `join()`                  | 等待指定线程执行完毕后再继续当前线程                         |
| `yield()`                 | 暂时让出 CPU 执行权，让其他线程有机会运行（不保证立即切换）  |
| `interrupt()`             | 中断线程（设置中断标志，具体响应需在线程逻辑中检查）         |
| `isAlive()`               | 判断线程是否还在运行                                         |
| `getName()` / `setName()` | 获取 / 设置线程名字                                          |
| `currentThread()`         | 获取当前正在执行的线程对象                                   |

```
public class ThreadControlExample {
    public static void main(String[] args) {
        Thread t1 = new Thread(new MyTask(), "Worker1");
        Thread t2 = new Thread(new MyTask(), "Worker2");

        // 启动线程，进入就绪状态
        t1.start();
        t2.start();

        // 判断线程是否还在运行
        while (t1.isAlive() || t2.isAlive()) {
            System.out.println("Main thread: Waiting for workers to finish...");
            try {
                Thread.sleep(500);  // 主线程睡眠一段时间
            } catch (InterruptedException e) {
                System.out.println("Main thread interrupted");
            }
        }
        System.out.println("Main thread: All workers finished.");
    }

    static class MyTask implements Runnable {  // 采用实现接口的方式创建
        @Override
        public void run() {
            String name = Thread.currentThread().getName();
            for (int i = 1; i <= 5; i++) {
                System.out.println(name + " - Step " + i);

                if (i == 3) {
                    // 第3步让出CPU资源
                    System.out.println(name + " yields the CPU.");
                    Thread.yield();  // 主动让出CPU
                }

                try {
                    Thread.sleep(300);  // 每步之间休眠300ms
                } catch (InterruptedException e) {
                    System.out.println(name + " was interrupted.");
                }
            }
        }
    }
}
```

## 参考资料

- 感谢 [Clever_Jimmy](https://github.com/leverimmy) 在 2024 年暑期培训中的 Java 部分的讲义。
- 感谢许斌老师在2024年暑期小学期java课程中详尽的PPT。
- 由于示例代码大部分都是用ChatGPT写的，~~所以顺手感谢一下造福人类的OpenAI公司吧。~~