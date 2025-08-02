# Python

## 一、课程引入

### Python 的历史
Python 的历史可以追溯到1989年，由荷兰计算机科学家 Guido van Rossum 在圣诞节假期时开始开发一种新的编程语言。他最初的想法是创建一种易于阅读、易于学习的语言，同时具有与 C 语言一样的能力。在经过多年的发展和完善后，Python 成为了一种非常受欢迎的编程语言。2000年，Python 2.0 发布；Python 2.x 系列一直持续到 2020 年，发布了 Python 2.7.18 版本作为最终版本。

2008年，Python 3.0 发布，引入了一些不兼容的改变，如 print变成了 print() 、除法运算符 / 的行为改变等。这些改变是为了解决 Python 2.x 系列中存在的一些设计缺陷。Python 3.x 系列逐渐成为主流版本，目前最新的稳定版本是 Python 3.12。

大家可以看到，Python 2 和 Python 3 的开发周期是有重叠的，而且 **特别要强调** 这两个版本的 Python 是不兼容的，这个和大家之前学习的 C / C++ 向下兼容不太一样。

### Python 的特点
1. 简单易学：Python 语法简单，容易上手；代码可读性好，结构清晰，因此，Python 常常作为非计算机专业的人员所使用的编程语言，可以方便、快捷地协助完成其他领域的科研工作。如果已经学过 C / C++ 等语言，学习 Python 会变得更加容易，因为 Python 的语法更加简洁，不需要过多的花括号、分号等符号，代码更加简洁易读。

2. 解释型语言：Python 是一种解释型语言，可以直接运行代码，无需编译。这使得 Python 的开发和调试过程更加快速和方便。大家目前可能没有体会，但是当你遇到了一些比较大的项目的时候，编译就会是一个耗时极长的过程，而且如果出现了错误，很可能整个程序直接崩溃，也不方便于定位错误；解释形语言在这方面就好得多。

> 解释型语言每次执行程序都需要一边转换一边执行，用到哪些源代码就将哪些源代码转换成机器码，用不到的不进行任何处理。每次执行程序时可能使用不同的功能，这个时候需要转换的源代码也不一样。相比于编译型语言，解释型语言几乎都能跨平台，“**一次编写，到处运行**”是真实存在的。也就是说，可以轻松实现在 Windows 上编写 Python 源代码，然后丢到 Linux 上去运行，只要双方配置了相同的解释器环境即可。

> 下面是一个简单的错误定位的例子：
> ```arduino
> Traceback (most recent call last):
> File "example.py", line 12, in <module>
>     func_a()
> File "example.py", line 2, in func_a
>     func_b()
> File "example.py", line 5, in func_b
>     func_c()
> File "example.py", line 8, in func_c
>     1 / 0
> ZeroDivisionError: division by zero
> ```
> 可以看到，Python 会告诉你在哪个文件的哪一行出现了错误，并且递归地告诉你是哪个函数调用了哪个函数，这样就可以很方便地定位错误。

3. 强大的库：Python 自带了很多标准模块和库，如 re（正则表达式）、os（操作系统接口）等；同时，Python 社区庞大活跃，有很多优秀的第三方库和框架，如 NumPy、pandas、Django、Flask 等，这些库可以帮助程序员更快速、更方便地实现各种功能，提高开发效率。

这些因素的共同作用下，Python 有一个极大的优势：开发效率高，也就是节约我们，作为程序员，写代码的时间；但与之相对的，Python 还有一个极大的劣势：运行效率低，不过在一些场景下，这个劣势并不是很明显，比如数据处理等领域，Python 的运行效率还是可以接受的。

## 二、基础知识

### 运行 Python 程序

#### 交互式解释器
Python 提供了一个交互式解释器，可以直接在终端或命令行中输入 Python 代码并立即执行。在终端或命令行中输入 `python3` 或 `python` 后，会进入 Python 的交互式解释器，可以输入 Python 代码并立即执行。

退出交互式解释器的方法是输入 `exit()` 或按下 `Ctrl + D`。（在 Windows 中可能是 `Ctrl + Z`）

```bash
Python 3.13.5 | packaged by Anaconda, Inc. | (main, Jun 12 2025, 16:09:02) [GCC 11.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> print(1+2)
3
>>> #按下 Ctrl + D 或输入 exit() 退出
```
#### 脚本文件
交互式解释器适合用来测试一些小的代码片段，但是对于一些较长的代码，我们通常会将代码保存到一个文件中，然后通过解释器执行这个文件。这种文件称为 Python 脚本文件，通常以 `.py` 为后缀名。如果你之前学过 C / C++，那么你可能对 Python 脚本文件的执行方式看着更顺眼一些。

在终端或命令行中输入 `python3 文件名.py` 或 `python 文件名.py` 即可执行这个 Python 脚本文件。

一般而言，我们在日常的使用时会以 `.py` 文件进行编写和执行 Python 代码。

### 输出
Python 中的输出函数是 `print()`，可以将括号中的内容输出到终端或命令行中。`print()` 函数可以接受多个参数，用逗号 `,` 分隔，会在输出时自动添加一个空格，并且会在输出结束时自动换行。

```python
print("Hello, world!")
print("Hello", "world!")
```

如果想要设置输出的间隔符和结束符，可以使用 `sep` 和 `end` 参数。

```python
print("Hello", "world!", sep=", ", end="!\n")
```

> 在交互式解释器中，如果直接输入一个表达式，解释器会自动将这个表达式的值输出到终端或命令行中，不需要使用 `print()` 函数。

### 输入
Python 中的输入函数是 `input()`，可以从终端或命令行中获取用户输入的内容，可以在括号中添加提示信息，括号中的信息会在执行输入之前输出到终端中作为提示。
```python
question = input("Please input your question: ")
```

`input()` 函数返回的是一个**字符串类型**，如果需要将用户输入的内容转换为其他类型，需要显式地进行类型转换。

```python
number = int(input("Please input a number: "))
```

### 控制流
Python 中的代码是可以从头到尾一行一行执行的，但这样看上去不甚美观。因此可以使用"if \_\_name__ == '\_\_main__':"，起到一个类似于 C++ 中的 main 函数的作用，使得代码更加清晰。

#### 顺序执行
Python 中的代码默认是按照从上到下的顺序依次执行的，这种执行方式称为顺序执行。

默认情况下，Python 依靠**换行**来隔离语句，也就是说，一行代码就是一个语句，不需要写分号。当然，也可以写分号，并且可以用分号隔断一行为多个语句，不过这种写法不太推荐。另外，如果一行代码太长，可以使用反斜杠 `\` 来换行，或者使用括号 `()` 将一行代码括起来。

```python
a = 1; b = 2
c = a + \
    b
d = (a +
     b)
```

#### 分支结构
Python 中的分支结构使用 `if` 语句，可以根据条件的真假执行不同的代码块，注意 Python 中的嵌套使用**缩进**来表示，不需要使用花括号 `{}`。这里的缩进可以用空格或者制表符，但是不要混用，工程上推荐使用4个空格，不过实际写代码时，你可以使用 Tab 键，IDE 会自动将 Tab 转换为 4 个空格。

当涉及到多个条件时，可以使用 `elif` 来添加额外的条件分支，也可以使用 `else` 来添加默认的条件分支。注意 Python 中**没有 `switch` 语句**。


```python
if condition1 and condition2: # 注意别忘了冒号
    # do something
elif condition3 or condition4:
    # do something
    if condition5:
        # do something
    else:
        # do something
else:
    # do something
```
#### 循环结构
##### while 循环
Python 中的 `while` 循环和 C++ 中的 `while` 循环类似，只要条件为真，就会一直执行循环体中的代码块。

```python
while condition:
    # do something
```

注意 Python 中没有 `do-while` 循环。

##### for 循环
在 C++ 中，我们使用 `for` 循环的格式是形如 `for (int i = 0; i < n; ++i)`，但是在 Python 中，`for` 循环的格式并非如此。不过有一种对 C++ 格式的简单模拟： `for i in range(n)`，它还有一些变体，比如 `range(m, n)`、`range(m, n, step)`。

```python
a = [1, 2, 3, 4, 5] # list 列表，后面会讲到
for i in range(5):
    print(a[i]) # 1 2 3 4 5
for i in range(1, 5):
    print(a[i]) # 2 3 4 5
for i in range(0, 5, 2):
    print(a[i]) # 1 3 5
for i in range(4, 1, -1):
    print(a[i]) # 5 4 3
for i in range(4, -1, -2):
    print(a[i]) # 5 3 1
```

但是 Python 中的 `for` 循环更多地用于遍历容器类型，比如列表、元组、字典、字符串等，比如：
```python
s = "Hello"
for c in s:
    print(c) # H e l l o 
```

但这种遍历形式失去了元素的索引信息，如果需要索引信息，可以使用 `enumerate()` 函数。

```python
for i, c in enumerate(s):
    print(i, c) # 0 H 1 e 2 l 3 l 4 o 
```

另外，你仍然可以使用`continue` 和 `break` 语句来控制循环的执行，`continue` 用于跳过当前循环的剩余部分，直接进入下一次循环；`break` 用于终止循环，这里与c++ 中的用法是一样的。

## 三、数据类型
### 简单的数据类型
#### int
整数类型，如 `1`、`-1`、`0` 等。
> Python 中的整数类型没有大小限制，可以表示任意大小的整数。对于存储空间，Python 会根据整数的大小自动调整，对于较小的整数，Python 会使用 4 字节存储，如果整数超出了 4 字节的范围，Python 会自动调整存储空间。
> Python 中的整数默认是十进制的，也可以使用二进制、八进制、十六进制表示，比如 `0b10`、`0o10`、`0x10` 分别表示二进制、八进制、十六进制的 10，对应的十进制是 2、8、16。

#### float
浮点数类型，如 `1.0`、`-1.0`、`0.0` 等。
> Python 中的浮点数类型是双精度浮点数，遵循 IEEE 754 标准，可以表示的范围和精度都是有限的，不会自动变长，因此可能会出现精度丢失的情况，相当于 C++ 中的 `double` 类型。

#### bool
布尔类型，只有两个值：`True` 和 `False`。
> Python 中的布尔类型是整数类型的子类，`True` 对应的整数是 1，`False` 对应的整数是 0。
> 注意首字母大写，这一点与 C++ 不同。

#### NoneType
空类型，只有一个值：`None`。
> `None` 通常用来表示空值或者空对象，类似于 C++ 中的 `nullptr`。
> 与 C++ 不同的是，Python 中的 `None` 是一个对象，是一个特殊的单例对象，只有一个实例，可以使用 `is` 运算符来判断两个变量是否指向同一个 `None` 对象。

#### str
字符串类型，可以使用单引号 `'` 或双引号 `"` 来表示字符串，如 `'Hello, world!'`、`"Hello, world!"`，转义符的用法与 C++ 类似，并且当你知道字符串中有很多转义符但你并不希望转义符生效时，可以在字符串前加 `r` 来表示原始字符串，比如 `r"Hello\nworld!"`。

```python
print("Hello, world!")
print('Hello, world!')
print("Hello\nworld!")
print(r"Hello\nworld!")
```
格式化字符串指的是在字符串中插入变量，Python 中有多种格式化字符串的方法，比如 `%` 运算符、`str.format()` 方法、`f-string` 等，其中 `f-string` 是 Python 3.6 引入的一种新的字符串格式化方法，是最简单、最直观的一种方法，推荐使用。
```python
name = "Alice"
print(f"Hello, {name}!")
```
> 注意 Python 中没有像 C++ 中的 `char` 类型，单个字符也是字符串类型。

### 变量的定义
Python 是一种动态类型语言，不需要显式地声明变量的类型，Python 解释器会根据变量的值自动推断变量的类型，并且可以在程序运行时改变变量的类型。

```python
a = 1
a = "Hello, world!"
```
> 可以拿中文作为变量名，但是不建议这么做。

### 变量的类型转换
虽然 Python 是一种动态类型语言，但它同时是一个强类型语言，这意味着 Python 有时不会自动进行类型转换，需要程序员显式地进行类型转换。

```python
a = 1
b = 2.0
c = "3"
d = a + b # 3.0，int 和 float 相加，结果是 float
e = a + int(c) # 4，int 和 str 相加，需要将 str 转换为 int 进行整数加法
f = str(a) + c # "13"，int 和 str 相加，需要将 int 转换为 str 进行字符串拼接
```

当然强制类型转换不是万能的，有时候可能会出现异常，比如将一个字符串转换为整数时，如果字符串不是一个合法的整数，会抛出 `ValueError` 异常。

```python
a = "Hello, world!"
b = int(a) # ValueError: invalid literal for int() with base 10: 'Hello, world!'
```
### 变量的运算
Python 中的运算符和 C++ 中的运算符大致相同，但是有一些细微的差别，比如整数除法运算符 `/` 的行为不同，Python 中的除法运算符 `/` 会得到一个浮点数，而不是整数，如果想要得到整数部分，可以使用**整除运算符** `//` 。

另外，Python 中的**幂运算符**是 `**`，而不是 `^`，`^` 是按位异或运算符。比如 `2 ** 3` 表示 2 的 3 次方，结果是 8。

Python 中的逻辑运算符是 `and`、`or`、`not`，而不是 C++ 中的 `&&`、`||`、`!`。

Python 中的比较运算符和 C++ 中的比较运算符相同，但是 Python 中的比较运算符可以连续使用，比如 `a < b < c`，相当于 `a < b and b < c`。

Python 中还有些特殊的运算符，比如**身份运算符** `is` 和 `is not`，用来判断两个变量是否指向同一个对象；**成员运算符** `in` 和 `not in`，用来判断一个值是否在一个容器中。

```python
a = 1
b = 2
c = 3
d = "Hello, world!"
print(a < b < c) # True
print(a is b) # False
print(a is not b) # True
print("Hello" in d) # True
print("world" not in d) # False
```

> `is`比较常见的是用来判断一个变量是否是 `None`。趁这个机会，给大家介绍一下 Python 中的 `None`:
> 在Python中，`None`是一个【内置的常量】，表示值的缺失或对象的缺失。它是一个特殊值，通常用于指示变量或对象没有值或尚未初始化。
> `None`经常用作函数的默认返回值，这些函数不返回任何有意义的值；`None` 也可以指示变量或对象当前未初始化。
> 由于它是一个内置的常量，所有值是 None 类型的变量都指向同一个地址。因此，当我要确认一个变量是否是 `None` 时，可以并且推荐使用 `is` 运算符，而非 `==` 运算符。

> `is` 和 `==` 的区别在于，`is` 比较的是两个变量的地址，而 `==` 比较的是两个变量的值。对于 `None` 这种单例对象，使用 `is` 更加准确。而对于其他对象，使用 `==` 更加合适。
> ```python
> x = 3
> x is 3
> # 输出
> # <stdin>:1: SyntaxWarning: "is" with a literal. Did you mean "=="?
> # True
> ```
> ```python
> x = 666
> x is 666
> # 输出
> # <stdin>:1: SyntaxWarning: "is" with a literal. Did you mean "=="?
> # False
> ```
> 为什么呢？因为 Python 会存储所有的-5到 256 的整数，其他任何变量是这些值时，会被指向这个预先开好的内存，因此任何两个值为 3 的 int 变量都指向同一内存地址，而 666 不在这个范围内，所以不会指向同一内存地址。



## 四、数据类型进阶
### 列表`list`
#### 定义列表
Python 中的列表是一种有序的集合，可以存储任意数量的元素，元素之间用逗号 `,` 分隔，用方括号 `[]` 括起来。列表中的元素可以是不同类型的数据，也可以是列表。空列表可以用 `[]` 或 `list()` 来表示。
```python
a = [1, 2, 3, 4, 5]
b = ["Hello", "world"]
c = [1, "Hello", 2.0]
d = [1, 2, [3, 4]]
e = []
f = list()
```
下面我们来介绍一些常用的列表操作。
#### 查
```python
a = [1, 2, 3, 4, 5]
a[0] # 1
a[1:3] # [2, 3]
a[-1] # 5
a[-3:] # [3, 4, 5]
a[::2] # [1, 3, 5]
a[::-1] # [5, 4, 3, 2, 1]
a[::] # [1, 2, 3, 4, 5]

# a[start:stop:step] start 是起始索引，stop 是结束索引（不包含），step 是步长。
```
> `str` 类型也可以使用这种方式进行索引，但是 `str` 类型是不可变的，所以下面的增、删、改操作中大部分是不适用的。
```python
s = "Hello,world"
s.append("!") # AttributeError: 'str' object has no attribute 'append'
```

#### 增
```python
a = [1, 2, 3]
a.append(4) # [1, 2, 3, 4]
a.insert(1, 5) # [1, 5, 2, 3, 4]
a.extend([6, 7]) # [1, 5, 2, 3, 4, 6, 7]
a + [8, 9] # [1, 5, 2, 3, 4, 6, 7, 8, 9] str 也可以这样操作
a * 2 # [1, 5, 2, 3, 4, 6, 7, 1, 5, 2, 3, 4, 6, 7] str 也可以这样操作
# 这里其实是返回了一个新的字符串，原来的仍然没有被改变
```
#### 删
```python
a = [1, 2, 3, 4, 5]
a.pop() # [1, 2, 3, 4]
a.pop(1) # [1, 3, 4]
a.remove(3) # [1, 4]
del a[0] # [4]
a.clear() # []
```
#### 改
```python
a = [1, 2, 3]
a[0] = 4 # [4, 2, 3]
a[1:3] = [5, 6] # [4, 5, 6]
a[1:3] = [5, 6, 7] # [4, 5, 6, 7]
```

此外，列表还有一些其他的操作，比如 `index()`、`count()`、`sort()`、`reverse()` 等，大家可以自行查阅文档。

### 元组`tuple`
#### 定义元组
Python 中的元组与列表类似，是一种有序的集合，可以存储任意数量的元素，元素之间用逗号 `,` 分隔，用圆括号 `()` 括起来。空元组可以用 `()` 或 `tuple()` 来表示，单个元素的元组需要在元素后面加一个逗号 `,`。
```python
a = (1, 2, 3, 4, 5)
b = ("Hello", )
c = tuple()
d = ()
```
> 和字符串一样，元组也是不可变的，也就是说元组一旦创建，就不能再添加、删除或修改元素。因此元组的大部分操作和字符串相同，在这里不再赘述。
#### 元组的用处
有时元组的括号可以省略，比如在函数返回多个值时，可以直接返回一个元组，另外元组还可以用来进行多个变量的赋值与交换。
```python
a, b = 1, 2
a, b = b, a # 交换 a 和 b 的值
```

### 集合`set`
#### 定义集合
Python 中的集合是一种无序的集合，可以存储任意数量的元素，元素之间用逗号 `,` 分隔，用大括号 `{}` 括起来。空集合可以用 `set()` 来表示。
```python
a = {1, 2, 3, 4, 5}
b = {1, 1, 2, 3, 3, 4, 5} # {1, 2, 3, 4, 5}
print(f"b:{b}")
c = set()
```
> 集合中的元素是不重复的，重复的元素会被自动去重。
#### 集合的操作
```python
a = {1, 2, 3, 4, 5}
1 in a # True
6 not in a # True
a.add(6) # {1, 2, 3, 4, 5, 6}
a.remove(6) # {1, 2, 3, 4, 5}
a.clear() # {}
```
集合支持一些常见的集合操作，比如并集、交集、差集、对称差等。
```python
a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}
a | b # {1, 2, 3, 4, 5, 6, 7, 8} 并集
a & b # {4, 5} 交集
a - b # {1, 2, 3} 差集
a ^ b # {1, 2, 3, 6, 7, 8} 对称差
```

### 字典`dict`
#### 定义字典
Python 中的字典是一种无序的集合，可以存储任意数量的键值对，键值对之间用冒号 `:` 分隔，键值对之间用逗号 `,` 分隔，用大括号 `{}` 括起来。空字典可以用 `{}` 或 `dict()` 来表示。
```python
a = {"name": "Alice", "age": 18}
b = dict()
c = {}
```
#### 字典的操作
```python
a = {"name": "Alice", "age": 18}
a["name"] # "Alice"
a["age"] = 30
a["university"] = "THU"
a # {"name": "Alice", "age": 30, "university": "THU"}
a.get("name") # "Alice"
a.get("sex", "Unknown") # "Unknown"
a.pop("university") # "THU"
a # {"name": "Alice", "age": 30}
a[{1, 2}] = [3, 4] # TypeError: unhashable type: 'set'
a.clear() # {}
```

### 生成式
Python 中的生成式是一种非常强大的工具，可以用来生成列表、元组、集合和字典。生成式的语法是在一个中括号 `[]`、圆括号 `()`、大括号 `{}` 或者大括号 `{}` 后面加上一个表达式，然后在表达式前面加上一个 `for` 循环，可以有多个 `for` 循环，也可以有 `if` 条件判断。

```python
a = [i for i in range(5)] # [0, 1, 2, 3, 4]
b = [i for i in range(5) if i % 2 == 0] # [0, 2, 4]
c = {i: i ** 2 for i in range(5)} # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
d = {i for i in range(5)} # {0, 1, 2, 3, 4}
```

## 五、函数
### 定义函数
Python 中函数的定义十分简单：

```python
def myFunc(params):
  	# Your Code...
  	return 
```

和控制语句一样，也是通过缩进来区分代码块；如果没有显式的返回语句，或者没有返回值，则默认返回 None；由于元组的存在，我们可以同时返回多个值。

这里有一个有些滑稽，却又真实存在的问题：我希望定义一个空的函数怎么办呢？答案是这样：

```python
def doNothing():
  	pass
```

我们可以在函数定义行末尾添加上它的返回值，但这不会对代码运行造成任何影响与限制，只是给程序员自己看的而已。

```python
def needString() -> str:
    ret = 0
    return ret		# No Error
```

### 函数参数

Python 对于函数参数的支持是很灵活的。Python 中支持四类参数：位置参数，关键字参数，默认参数和可变参数。

#### 位置参数

位置参数是指函数调用时按照函数定义时的参数顺序传递的参数

```python
def greet(name, message1, message2):
    print(f"{message1}, {message2}, {name}!")

greet("Alice", "Hello", "How are you?")  # 输出 "Hello, Alice!"
```

#### 关键字参数

关键字参数是指在函数调用时使用参数名来指定参数的值。这样可以不按照函数定义时的参数顺序传递参数，而是根据参数名来确定参数值。

```python
greet(message1="Hi", message2="nice to meet you", name="Bob")  # 输出 "Hi, Bob!"
```

前两者可以混用，**位置参数一定要在关键字参数的前面**。
```python
greet("Alice", message1="Hello", message2="How are you?")# 输出 "Hello, How are you?, Alice!"
greet("Alice", message2="How are you?", message1="Hello") # 输出 "Hello, How are you?, Alice!"
greet(name="Alice", "Hello", "How are you?") # TypeError: greet() got multiple values for argument 'name'
```

#### 默认参数

这个还比较好理解，就是给一些参数默认值, 如果在调用时没有被传入，则使用默认值。

```python
def greet(name, message="Hello"):
    print(f"{message}, {name}!")

greet("Alice")  # 输出 "Hello, Alice!"
greet("Bob", "Hi")  # 输出 "Hi, Bob!"
```

#### 可变参数

在Python中，可变参数有两种：`*args` 和 `**kwargs`。我们先来看前者

`*args` 表示任意多个位置参数，它是一个元组类型：

```python
def add(*args):
    result = 0
    for num in args:
        result += num
    return result

print(add(1, 2, 3))  # 输出 6
print(add(1, 2, 3, 4, 5))  # 输出 15
```

再来看一下后者 `**kwargs`，它表示多个关键字参数，实际上是一个字典类型，不过在传入的时候我们也不需要显式写成字典。

```python
def greet(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

greet(name="Alice", message="Hello")  # 输出 "name: Alice" 和 "message: Hello"
greet(name="Bob", age=30, city="New York")  # 输出 "name: Bob"、"age: 30" 和 "city: New York"
```

## 六、面向对象
Python中的类基础用法比C/C++更简洁一些，下面我们通过例子来看一下。

```python
class myClass:
  	pass	# 定义了一个空类
  
myClass.b = 1		# 为 myClass 添加类公有成员变量 b

c = myClass()		# 实例化
print(c.b)			# Output: 1

c.b = 3

print(c.b)			# Output: 3
print(myClass.b) # Output: 1（访问类的属性）
print(c.__class__.b)	# Output: 1 （访问类的属性）
```

Python 中成员变量的定义不用像 C++ 那样在类中定义，可以随时在类外定义，但是这样的变量是类变量，而不是实例变量。在上面的例子中，我们先为 myClass 定义了类变量；当我们将类实例化的时候，会默认共享这一个变量，指向同一个地址；但是，如果在某个对象上修改了类变量的值，那么这个对象上的类变量会变成实例变量，即该对象会拥有自己的属性，而不再共享类变量；此时，我们仍然可以通过 `instance.__class__.var` 来访问共享变量。

我们再来看一下函数

```python
class A:
    def __init__(self, a, b):
		self.a = a
		self.__b = b #只要是以 __ 开头的成员变量，默认就是私有成员变量，无法在类外访问
        
    def print(self):
		print(self.a, self.__b)
        
a = A(1, 2)
print(a.a)		# Output: 1
print(a.__b)	# Output:	AttributeError: 'A' object has no attribute '__b'
a.print()			# Output: 1 2
        
```

`__init__` 是构造函数，这个学过 C++ 的同学应该还比较熟悉，但是要注意 Python 中只能有一个构造函数，同时大部分情况下我们不会用到析构函数；`print` 就是我们自己定义的一个成员函数。

所有成员函数第一个参数必须是 self，它起到和 C++ 中 this 类似的作用。不加 self 的变量、函数会被视作局部或全局的变量、函数，但是不会视作类成员，你需要显示地指出 self 。

注意到，我们为这个类添加了两个成员变量 `a` 和 `__b`，大家从下面的输出中也可以看出来，以 `__` 开头的默认就是私有成员变量，其他的都是公有成员变量，函数也是一样的。

继承的基础语法是 `class A(parent_class)`，默认是公有继承。由于篇幅关系这里就不展开了，请大家自学。

## 七、模块
Python 强大的地方之一就是有很多的模块，我们可以直接调用这些模块来实现我们的功能，而不用自己去实现。Python 的模块分为三种：内置模块、第三方模块和自定义模块。
### 引入模块
Python 中使用 `import` 关键字来引入模块，可以引入整个模块，也可以引入模块中的某个函数、类等。

```python
import math # 引入整个 math 模块     math.sqrt(4) # 2.0
import math as m # 引入整个 math 模块，并将其重命名为 m     m.sqrt(4) # 2.0
from math import sqrt # 从 math 模块中引入 sqrt 函数     sqrt(4) # 2.0
```

### 内置模块
Python 中有很多内置模块，比如 `math`、`random`、`os`、`sys` 等，我们可以直接使用这些模块来实现我们的功能。在这里我们列举出一些常用的内置模块及其功能：

1. `os`：提供了与操作系统交互的功能，如文件操作、目录操作、进程管理等。
2. `sys`：提供了一些与Python解释器和Python运行环境相关的功能，如命令行参数、标准输入输出、环境变量等。
3. `datetime`：提供了处理日期和时间的功能，如日期的计算、格式化、解析等。
4. `re`：提供了正则表达式的支持，可以用来进行文本匹配和替换等操作。
5. `math`：提供了数学运算的函数库，如三角函数、指数函数、常量等。
6. `random`：提供了生成随机数的函数，可以用来进行模拟和随机抽样等操作。
7. `json`：提供了JSON格式的编码和解码功能，可以进行数据的序列化和反序列化。
8. `sqlite3`：提供了SQLite数据库的支持，可以进行数据库的连接、查询、修改等操作。

### 第三方模块
Python 中有很多优秀的第三方模块，可以帮助我们更好地完成工作，比如 `numpy`、`pandas`、`matplotlib`、`scikit-learn` 等。这些模块通常需要使用 `pip` 来安装，安装命令为在终端输入 `pip install package_name`。（有时可能需要用 `pip3`）
> 如果你想要查看已经安装的模块，可以使用 `pip list` 命令。

> 如果你因为中国大陆的网络原因无法顺畅地安装第三方包，可以参照 [这个链接](https://mirrors.tuna.tsinghua.edu.cn/help/pypi/) 进行换源。
```bash
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple package_name #使用清华源进行安装
```
### 自定义模块
Python 中的模块就是一个 `.py` 文件，我们可以在一个 `.py` 文件中定义一些函数、类等，然后在其他文件中引入这个模块来使用这些函数、类等。比如我们可以定义一个 `my_module.py` 文件，然后在其他文件中引入这个模块来使用这个模块中的函数、类等。

对于文件的组织，每个文件夹都是一个包，每个包目录下都必须有一个 `__init__.py` 文件，否则，Python 就把这个目录当成普通目录，而不是一个包。这个文件可以为空，也可以包含一些初始化代码，比如导入一些模块、定义一些变量等。这样我们就可以通过 `import package_name` 来引入一个包。下面给出一个文件组织的示例：

```
my_package/
    __init__.py
    my_module.py
main.py
```

在 `my_module.py` 文件中定义了一个函数 `my_func`：

```python
def my_func():
    print("Hello, world!")
```

在 `main.py` 文件中引入了 `my_module` 模块，并调用了 `my_func` 函数：

```python
import my_package.my_module

my_package.my_module.my_func()
```

### 我该怎么学习使用一个库

1. 阅读文档
2. 尝试样例、经典项目
3. 根据 IDE / 编辑器的提示阅读接口文档
4. **问 ChatGPT**

## 八、其他常见操作

### 异常处理
有的时候我们的代码设计得并不精巧，一些没有考虑到的特殊情况可能会导致程序崩溃，但很多时候我们希望程序能够继续运行下去，这时候我们就需要用到异常处理。

Python 中的异常处理使用 `try`、`except`、`else` 和 `finally` 关键字来实现，`try` 代码块中放置可能会出现异常的代码，`except` 代码块中放置异常处理的代码，`else` 代码块中放置没有异常时执行的代码，`finally` 代码块中放置无论是否有异常都会执行的代码。

```python
try:
    a = 1 / 0
except ZeroDivisionError:
    print("Division by zero!")
else:
    print("No exception!")
finally:
    print("Finally!")
```
### 断点调试
有些时候，我们的从程序可能会在中间出现bug，而仅仅命令行提供的报错信息有无法满足我们的需求，这时候我们就需要用到断点调试。

这里为大家推荐一个简单的调试工具`breakpoint()`，它可以在代码中设置断点，运行到断点时会暂停程序的执行，并进入一个交互式的调试环境。你可以在这个环境中查看变量的值、执行代码等。

进入调试后，输入`continue`或者`c`可以继续执行程序，输入`quit`或者`q`可以退出调试环境。
```python
def my_func():
    a = 1
    b = 2
    breakpoint()  # 设置断点,
    c = a + b
    print(c)
my_func()
```

你也可以使用其他的调试工具，比如 `pdb`、`ipdb` 等，这里不再逐一介绍。

### 文件操作
Python 中的文件操作十分简单，主要有三个步骤：打开文件、读写文件和关闭文件。

#### 打开文件
Python 中使用 `open()` 函数来打开文件，`open()` 函数的第一个参数是文件名，第二个参数是打开文件的模式，常用的模式有 `r`（只读）、`w`（只写）、`a`（追加）、`r+`（读写）、`w+`（读写）、`a+`（读写追加）等。

```python
f = open("test.txt", "r") # 不推荐，需要手动关闭文件
f.close()

with open("test.txt", "r") as f: # 推荐，自动关闭文件
    pass #这里缩进部分表示在文件打开后可以进行的操作，结束缩进会自动关闭文件
```

#### 读写文件
打开文件后，可以使用 `read()`、`readline()`、`readlines()` 来读取文件内容，使用 `write()` 来写入文件内容。

```python
with open("test.txt", "r") as f:
    content = f.read() # 读取整个文件
    line = f.readline() # 读取一行
    lines = f.readlines() # 读取所有行，返回一个列表

with open("test.txt", "w") as f:
    f.write("Hello, world!") # 写入字符串
```

## 九、环境配置进阶
我们刚刚介绍了 Python 有很多现成的包，这些包被广泛应用。事实上，任何大型的 Python 项目或多或少都引入了第三方的包。然而，这些包的不同版本之间有可能是不互相兼容的。如果我们同时开发 A 项目和 B 项目，A 项目要求 x 包的 4.0 版本， B 项目却只能在 x 包的 5.0 版本下运行，这就会给我们带来极大的困扰。

Conda 的一大作用就是创建独立的虚拟环境，每个环境都可以拥有自己的 Python 解释器、库和依赖项。这使得在不同的项目或应用程序之间隔离依赖项变得容易。我们可以为每一个项目创建专属的虚拟环境，在切换项目的同时也切换虚拟环境，避免依赖上的冲突。

Conda 的安装相对简单，请大家自行去 [Tuna](https://mirrors.tuna.tsinghua.edu.cn/anaconda/miniconda/) 下载系统对应版本的 miniconda 并安装（请安装较新版本的 Conda）。下面有一些笔者常用的操作供参考：

1. `conda create -n <env_name> python=3.9` 创建一个 Python 3.9 版本的新虚拟环境，注意最好不要在一个虚拟环境启动时创建另一个虚拟环境，否则可能会出现问题。
2. `conda activate <env_name>` 激活这一虚拟环境。激活后，你可以正常使用 `pip` 安装包，所安装的包会且只会作用于当前的虚拟环境。
3. `pip freeze > requirements.txt` 将当前环境中 pip 安装的包的列表存储到 requirements.txt 当中。
4. `pip install -r requirements.txt` 按照 requirements.txt 中的要求在当前环境中安装对应的包。(下载缓慢时可以选择清华源加速)
   - `pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt` 使用清华源加速安装。
5. `conda deactivate` 退出当前的虚拟环境。

当一个项目需要多人协作的时候，流程往往是这样的：

- 一个人：创建新的虚拟环境并激活 -> 安装必要的包 -> 导出到 requirements.txt 中，一并上传至项目仓库
- 其他人：把仓库拉下来 -> 创建新的虚拟环境并激活 -> 根据 requirements.txt 安装需要的包

## 十、附录
下面列出了一些 Python 的学习资源，供大家参考：

- 2024年sjx学长的 Python 教程：[链接](https://summer24.net9.org/basic/python/)
- 2023年lyf学长的 Python 教程：[链接](https://summer23.net9.org/basic/python/)
- 2022年zcy学长的 Python 教程：[链接](https://zhaochen20.notion.site/a5a8fc071a0c42b188cf2bec1be5149d)
- 2021年ayf学长的 Python 教程：[链接](https://cloud.tsinghua.edu.cn/d/1f222c2869964fc99f33/?p=%2F07-19%20Python&mode=list)
- 清华大学计算机系科协技能引导文档：[链接](https://docs.net9.org/languages/python/)
- Python 官方文档：[链接](https://docs.python.org/3/)
