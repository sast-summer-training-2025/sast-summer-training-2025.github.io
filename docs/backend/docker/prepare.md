# 课前准备

## 前置知识

- 了解 Linux 命令行的基本操作；
- 对文件目录有基本的认识。

## 环境配置

### Windows 和 MacOS

可以直接从官网下载[Docker Desktop](https://www.docker.com/)并安装。

### Linux

以 Ubuntu 为例，常见的安装方式包括：

- 从官网下载 [Docker Desktop](https://www.docker.com/) Linux 版并安装。
- 按照[官方文档](https://docs.docker.com/desktop/setup/install/linux/ubuntu/)的指引安装Docker Desktop。
- 按照[官方文档](https://docs.docker.com/engine/install/ubuntu/)的指引安装 Docker Engine。

> Docker Engine 是 Docker Desktop 的组成部分之一，也是 Docker 的核心组件，而 Docker Desktop 还另外提供了图形界面、Kubernetes 集群管理等其他特性。事实上，对于初学者来说，二者的区别几乎只体现在图形界面的有无。Docker Engine 足以应对本次课程的内容。

若使用其他 Linux 发行版，可以参考[官方文档](https://docs.docker.com/desktop/setup/install/linux/)中提供的其他 Linux 发行版的安装方式。

## 测试环境

安装完成后，可以启动 Docker Desktop 并在命令行中运行 `docker run --rm hello-world`，若输出的内容中含有

```shell
Hello from Docker!
This message shows that your installation appears to be working correctly.
```

证明安装成功。

## 提醒

互联网上很多旧的 Docker 安装教程会提倡在安装 Docker 后进行换源，但是近来国内 Docker 镜像站陆续下架，现在依旧可用的镜像源十分罕见，因此不再建议换源。

解决办法是在科学上网（笑）后直接使用默认源，至于如何配置科学上网，就不是（也不能是）课程的内容了，可以自行研究。
