# Docker 课程作业

现在有一个简单的 [C++ 项目](https://github.com/sast-summer-training-2025/docker-hw)，已提供 Makefile 文件，请基于 `ubuntu:24.04` 构建镜像，运行这个项目。

## 项目介绍

这是一个用于计算多边形、圆形的周长、面积与圆柱体、圆锥体的表面积、体积的 C++ 项目，输入几何图形的参数，即可获得计算结果。

### 输入

输入为 5 个浮点数，分别为多边形边数、多边形边长、圆的半径、圆柱和圆锥的底面半径、圆柱和圆锥的高度。

### 输出

输出为计算得到的周长、面积、表面积、体积结果。

### 样例

输入

```
4 3.5 3.0 2.0 3.0
```

应当得到如下输出

```
Polygon Perimeter: 14.0000
Polygon Area: 12.2500
Circle Perimeter: 18.8495
Circle Area: 28.2743
Cone Surface Area: 35.2207
Cone Volume: 12.5664
Cylinder Surface Area: 62.8318
Cylinder Volume: 37.6991
```

## 要求（可循序渐进完成）

1. 基于 `ubuntu:24.04` 构建镜像，使用 Makefile 来编译项目并运行。
2. 分阶段构建镜像，使最终得到的镜像中只含有可执行文件，不含源代码和依赖工具。
3. 将构建最后阶段的基础镜像改为 `scratch`，从而减小镜像的大小。

此外，也可以尝试使用完成的 Dockerfile 运行自己手中其他的 C++ 项目，有余力的同学还可以自行尝试完成 Dockerfile 来运行一个 Django 项目。

## 提示

为了避免 C++ 编译工具安装过程中的交互性时区选择导致镜像构造过程卡住，可以在 Dockerfile 中增加一行

```dockerfile
ENV DEBIAN_FRONTEND=noninteractive
```

由于 `scratch` 镜像不含有 C++ 的动态链接库，因此需要在编译时增加 `-static` 选项静态链接标准库。
