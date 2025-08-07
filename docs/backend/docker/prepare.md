# 课前准备

## 前置知识

- 了解Linux命令行的基本操作；
- 对文件目录有基本的认识。

## 环境配置

### Windows和MacOS

可以直接从官网下载[Docker Desktop](https://www.docker.com/)并安装。

### Linux

以Ubuntu为例，常见的安装方式包括：

- 从官网下载[Docker Desktop](https://www.docker.com/) Linux版并安装。
- 按照[官方文档](https://docs.docker.com/desktop/setup/install/linux/ubuntu/)的指引安装Docker Desktop。
- 按照[官方文档](https://docs.docker.com/engine/install/ubuntu/)的指引安装Docker Engine。

> Docker Engine是Docker Desktop的组成部分之一，也是Docker的核心组件，而Docker Desktop还另外提供了图形界面、Kubernetes集群管理等其他特性。事实上，对于初学者来说，二者的区别几乎只体现在图形界面的有无。Docker Engine足以应对本次课程的内容。

若使用其他Linux发行版，可以参考[官方文档](https://docs.docker.com/desktop/setup/install/linux/)中提供的其他Linux发行版的安装方式。

## 测试环境

安装完成后，可以启动Docker Desktop并在命令行中运行`docker run --rm hello-world`，若输出的内容中含有
```shell
Hello from Docker!
This message shows that your installation appears to be working correctly.
```
证明安装成功。

## 提醒

互联网上很多旧的Docker安装教程会提倡在安装Docker后进行换源，但是近来国内Docker镜像站陆续下架，现在依旧可用的镜像源十分罕见，因此不再建议换源。

解决办法是在科学上网（笑）后直接使用默认源，至于如何配置科学上网，就不是（也不能是）课程的内容了，可以自行研究。
