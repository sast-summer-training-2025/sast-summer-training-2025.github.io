# 课前准备：Python配置
## 验证 Python 是否已安装
由于 Python 是一门热门的语言，很多操作系统都会默认安装 Python，你可能也会因为一些千奇百怪的原因在你的设备中安装过 Python 但后来又忘掉了。为了验证 Python 是否已经安装在你的设备上，你可以在终端或命令行中输入以下指令：
```bash
python3 --version	# for macOS and Linux
python --version	# for windows
```

如果你看到了类似 `Python 3.8.5` 的输出，那么恭喜你，你的设备上已经安装了 Python。如果你看到了类似 `Python 2.7.18` 的输出，那么你的设备上安装的是 Python 2，我们建议你安装 Python 3。如果你看到了 `command not found: python` 的输出或者没有输出，那么你的设备上没有安装 Python，你需要安装 Python。

## 安装 Python
### macOS

访问 https://www.python.org/downloads/macos/ 下载对应版本的包并安装。

### Windows

访问 https://www.python.org/downloads/windows/ 并安装对应版本。在安装时记得勾选 Add To Path，将安装路径保存为系统环境变量。

### Linux

使用包管理器安装。例如在 Debian/Ubuntu 上，你可以使用以下指令来安装 Python3。
```bash
sudo apt-get update
sudo apt-get install python3
```

## 线上操作平台
如果你想在没有安装Python的情况下进行一些简单的python编程，可以使用[菜鸟工具](https://c.runoob.com/compile/9/)或者 [pythontutor](https://pythontutor.com/)，线上编写 Python 代码并运行。
