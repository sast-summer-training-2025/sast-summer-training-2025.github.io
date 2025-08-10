# Docker 作业答案

讲义中已经给出了一个构建能够编译 C++ 代码的镜像的 Dockerfile：

```dockerfile
# build
FROM ubuntu AS builder

WORKDIR /usr/src/cpp

ENV DEBIAN_FRONTEND=noninteractive

RUN apt update && apt install -y build-essential

COPY main.cpp .

RUN g++ main.cpp -o main -static

# runtime
FROM scratch

COPY --from=builder /usr/src/cpp/main .

CMD ["./main"]
```

得到这个 Dockerfile 的过程可以参考讲义，此处不再赘述。

现在我们在这个 Dockerfile 上进行修改。

题目已经提供了 Makefile，那么我们可以用 make 来编译项目，因此在安装编译工具时增加 `make`，即

```dockerfile
RUN apt update && apt install -y build-essential make
```

后面的 `COPY` 现在需要复制所有的项目文件，因此改为

```dockerfile
COPY . .
```

编译不再使用 `g++` 命令，而是使用 `make` 命令，即

```dockerfile
RUN make
```

现在，我们得到了满足条件的 Dockerfile：

```dockerfile
FROM ubuntu:24.04 AS builder

ENV DEBIAN_FRONTEND=nointeractive

RUN apt update && apt install -y build-essential make

WORKDIR /usr/src/cpp

COPY . .

RUN make

FROM scratch

COPY --from=builder /usr/src/cpp/main .

CMD ["./main"]
```

别忘了，`scratch` 镜像中不含静态链接库，因此我们还需要修改 `Makefile`，增加编译选项 `-static`，即

```makefile
all:
    g++ main.cpp circle.cpp polygon.cpp cone.cpp cylinder.cpp \
        -o main --std=c++11 -Wall -static
```

现在我们可以使用如下命令构建镜像并运行容器了

```shell
docker build -t cpp:5.0 .
docker run -it --rm cpp:5.0
```

提供一组输入，即可看到程序的计算结果。

此外，还可以使用手中其他的 C++ 项目，将项目文件拿过来，构建镜像并运行容器，也可以正常运行项目代码。

