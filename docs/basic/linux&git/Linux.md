# Linux

## Linux 是什么？

### Linux 简介

**Linux** 是一种自由和开放源码的类 UNIX 操作系统，其内核由 Linus Torvalds 在 1991 年发布。

**Linux** 也是自由软件和开放源代码软件发展中最著名的例子，只要遵循 GNU，任何个人和机构都可以自由地使用 Linux 的所有底层源代码，这使得它得到来自全世界软件爱好者和组织的开发支持。

<p align="center">
    <img src="/basic/linux&git/images/Linux.png" alt="Linux" width="200"/>
</p>


!!! note

    Linux 严格来说是单指操作系统的内核，因操作系统中包含了许多用户图形界面和其他实用工具。如今Linux常用来指基于Linux的完整操作系统，内核则改以Linux内核称之。

    
### 接触 Linux 的场景

Linux 被广泛运用于各个领域：

- 服务器、主机、超级计算机
- 个人计算机
- 嵌入式系统（智能小车、树莓派、机顶盒、移动设备等）
- 基础设施（红绿灯、工业传感器）

对于个人的日常开发和使用，我们大概会从以下几个方面接触到 Linux：

- 安装 Linux 系统（单系统、Windows & Linux 双系统）
- WSL（英语：Windows Subsystem for Linux）
- 虚拟机（Virtualbox、Docker）
- 服务器远程连接（SSH、RDP）


### Linux 发行版

我们平时使用的“Linux”严格来说是 Linux 发行版本，而 Linux 狭义上单指操作系统的内核。

发行版本在内核的基础上还包括**安装工具、系统配置、图形桌面界面、各种 GNU 软件**等，使得这个系统能够适用于各种使用目的。

!!! note

    [DistroWatch](https://distrowatch.com/) 上面有很多发行版的排名，读者可以自行查阅选择。

以下是 Linux 一些发行版本的简介：

- **Ubuntu**: 可能是最多人在使用的一个 Linux 发行版。相当有名，用户群体大，提供长期支持，兼容性也较好。

- **Ubuntu Server**: 没有预装桌面环境的 Ubuntu，更常见于服务器。

- **Debian**: 据说是 Ubuntu 的上游，同样没有桌面环境，服务器上很常见，界面相当简陋（

- **Arch Linux**: 一个据说是高度可定制（什么都没预装）的版本，软件生态也比较新，不嫌麻烦和折腾的倒是可以试试，深度定制后还是蛮美观的。

- **Manjaro**: 似乎是一个基于 Arch 的版本，提供了几个初始可选的桌面，但是在易用性上仍然保留了许多 Arch 可定制的思想（不如 Ubuntu 易用）

- **Fedora**: Red Hat 的社区版, 听说是 "几乎所有的开发环境都能一键安装", 很省心的系统.

- **Linux Mint**: 来自 Ajax 学长推荐的一个发行版, 基于 Ubuntu, 更加注重用户体验 (好看).

- **Kali Linux**: 专用于渗透测试的系统, 预装了大量的渗透测试工具.

### 关于安装一个 Linux 系统

Linux 系统使用场景众多，安装流程根据发行版也各不相同，读者可以根据自己选择的发行版自行查阅对应的官方文档进行安装。此处给出 Linux & Windows 双系统、 WSL 和虚拟机几种主流场景的大致安装流程：

- **双系统**: 

    1. 制作启动盘：
        到对应发行版**官方**或**镜像源**下载对应的ISO文件，使用刻录工具刻录到U盘中
    2. 预留磁盘空间：
        你需要预留出一块**未分配**的磁盘空间，这个操作在 Windows 上可以通过**磁盘管理器**完成
    3. 进入安装：
        插入制作好的启动盘，重启电脑，长按 `f12` （不同型号的主板可能不一样）进入 **Boot Menu**，选择U盘作为启动盘，随后即可进入系统镜像源自带的安装程序

- **WSL**:

    适用于 Windows 系统，一点前置要求：在“程序”-“程序与功能”中，“启动或关闭Windows服务”，勾选“适用于Linux的Windows子系统”及“虚拟机”。
    随后读者只需要在 Windows 的终端输入 `wsl --install` 或者从 Microsoft Store 下载对应 Linux 发行版即可。
    
    !!! note

        `wsl --install` 没有指定发行版，默认会安装最新的 Ubuntu 系统，如果希望指定发行版本，可以通过 `wsl --list --online` 查询，随后通过 `wsl --install -d <Distro>` 安装。

- **虚拟机**:

    你需要一个类似 VMWare 或 Virtual Box 的虚拟机软件，随后可以自行查询相关教程，在虚拟机软件内进行虚拟机配置和镜像安装即可。

- **Mac**: 

    Mac 系统本身是类 Unix 的，有着跟 Linux 很相似的操作体验（除了包管理器和一些系统指令上的细微差别），个人认为 Mac 用户并不需要做额外的配置来学习 Linux。

## Shell

### 认识 CLI 

我们将“用户到内核之间的中介”称为 Shell，它接受并解析（Parse）用户输入命令行的指令，并调用内核所提供的对应服务。
    
Shell 分为图形界面和命令行界面两种，比如 Windows 的文件浏览器、程序管理器都可以算是 GUI Shell，但用 Linux 时我们一般说的都是 CLI Shell。

许多 Linux 发行版同样有着跟 Windows 和 Mac 一样直观易上手的图形界面（GUI, Graphical User Interface），但是通过 CLI （Command-Line Interface）可以更加直接和底层地接触到 Linux 系统。我们也将提供 CLI 的程序称为**终端（Terminal）**。
!!! note
    
    **Shell**：常见的 Shell 包括 sh、bash、zsh、fish 等。
    
    **Terminal**：终端的名字来源于它在用户和机器交互过程中所处的位置：用户在终端输入、机器通过终端输出，现在我们已经不再需要专门的硬件充当终端，而是利用一个程序来模拟其行为。当我们打开一个终端模拟器（如 Windows 的 cmd，Linux 的 Konsole、gnome-terminal）时，一个 Shell 随即被运行，我们就可以通过这个 Shell 所提供的 CLI 输入指令了。

<p align="center">
    <img src="/basic/linux&git/images/Shell.png" alt="Linux" width="400"/>
</p>

- 推荐大家课后阅读 [SAST skill docs](https://docs.net9.org/basic/linux/#how-does-shell-run-commands) 上关于 How Does Shell Run Commands 的介绍，会帮助大家加深对 Shell 的理解。

### Linux 文件系统

- **一切皆文件**

    在 Linux 的文件系统视角下，有一个非常重要的设计哲学：**「一切皆文件」**。

    不仅仅是我们提到的**常规文本文件、二进制文件**等，在 Linux 系统中，**目录**也是一个文件，与常规文件不同之处在于，常规文件存储的是用户所需要的文本等数据，而目录文件存储着其下的文件信息。

    除此之外，**块设备、FIFO（命名管道）和 Socket（网络套接字）**也被视作文件。因此，我们可以用访问常规文件的方式，去访问这些文件。（不过后者往往需要 `root` 权限）

- **文件层级**

    Windows 系统会将磁盘分为 C、D等不同的区域（Windows的磁盘管理下叫做“卷”），每个分区往往也有明确的作用（比如C会存放系统文件和用户）。

    不同于 Windows，Linux 系统的所有文件都被存放在了一个名叫 `/` 的根目录下，其他分区以挂载的形式挂在了这棵树上。

    用户登录 Linux 系统，默认会进入 `~` 目录，这里 `~` 指代的就是`home/<your_username>`，也就是你的用户所归属的目录，与你用户有关的所有文件（如下载的软件，配置的环境，ssh的密钥）也都将存放在这个目录下。

    <p align="center">
        <img src="/basic/linux&git/images/Tree.png" alt="Linux" width="800"/>
    </p>

    - `/`：根目录；
    - `/bin`：存放基础命令的**二进制文件**；
    - `/boot` ：存储在**启动系统**时需要的文件；
    - `/home`：存放**用户目录**的目录，默认情况每个用户主目录都设在该目录下；
    - `/lib`：存放标准程序设计库目录，又叫动态链接共享库目录，目录中文件类似windows里的后缀名为dll的文件；
    - `/etc`：系统配置文件所在目录；
    - `/root`：系统管理员的主目录；
    - `/mnt` ：**临时挂载文件系统**的地方，手动挂载磁盘时常挂载到这里
        - 如果你是 WSL2 系统，在这里应该能够看到 Windows 硬盘在此处的映射。（比如 `ls` 指令一下）
    - `/var`：可变数据，如日志（/var/log）、缓存、邮件、打印任务等；
    - `/run`：存放系统运行时的信息（临时挂载、pid 文件、服务状态），在开机时自动生成；
    - `/tmp`：存放公用临时文件目录。


### 熟悉 Shell  

有关 Linux 的基本操作，在[2023年暑培讲义](https://github.com/sast-summer-training-2023/sast2023-linux-git/blob/main/handout.pdf)和 [Docs9](https://docs.net9.org/basic/linux/) 中都有比较详细的讲解。这里不详细展开，读者可以自行学习或前往[拓展资料](/basic/linux&git/Extend)进行学习。

**需要说明的是**，学习 Shell 相关指令时，可以积极使用 `man` 和 `tldr` 指令进行查询，官方文档无法解决时，可以通过 StackOverflow 等论坛查询。当然你也可以询问 GPT，不失为一种高效的方法。

- [Shell Operations(Basic)](/basic/linux&git/ShellOperations)

## SSH

SSH（Secure Shell）是一种用于在不安全的网络上安全访问远程计算机的协议。SSH 采用加密等方法，提供了不安全网络上安全的远程登陆（ssh）和文件传输（scp/sftp）服务。

### SSH 基本使用方法

- 远程登陆

    ```bash
    # ssh {{username}}@{{remote_host}} -p {{2222}}
    ssh root@ics25.net9.org -p 22222
    ```

- 远程传输

    ```bash
    scp -P 22222 example.com:~/test.txt ./
    ```

有关 SSH 的更多用法（密钥生成与传输、SSH with Proxy / Jumping、SSH Tunneling），Ajax 学长的[2024年暑培Linux讲义](https://summer24.net9.org/basic/linux_git/Linux/#ssh)给出了更详细的介绍，读者可以自行阅读学习。

## Basic Tools

### Jobs Management

默认情况下，在 shell 中运行的命令都在前台运行，如果需要在后台运行程序，需要在最后加上 &。

如果希望把最近放在后台的程序恢复到前台，使用 `fg`。

```bash
❯ ping localhost &
[1] 74815
PING localhost (127.0.0.1) 56(84) bytes of data.
64 bytes from localhost (127.0.0.1): icmp_seq=1 ttl=64 time=0.135 ms

╭─ ~/TsingHua ········································································· ✔  ≡  base Py  16:49:51 ─╮
╰─ 64 bytes from localhost (127.0.0.1): icmp_seq=2 ttl=64 time=0.061 ms                                              ─╯
❯ fg
[1]  + 74815 running    ping localhost
64 bytes from localhost (127.0.0.1): icmp_seq=5 ttl=64 time=0.051 ms
64 bytes from localhost (127.0.0.1): icmp_seq=6 ttl=64 time=0.028 ms
64 bytes from localhost (127.0.0.1): icmp_seq=7 ttl=64 time=0.042 ms
# Ctrl + C
--- localhost ping statistics ---
7 packets transmitted, 7 received, 0% packet loss, time 6237ms
rtt min/avg/max/mdev = 0.028/0.054/0.135/0.034 ms

```

而如果需要将前台程序切换到后台，则需要按下 Ctrl + Z 发送 SIGTSTP 使进程挂起。

我们可以使用 jobs 命令，看到当前 shell 上所有相关的进程。

```bash
❯ ping localhost
PING localhost (127.0.0.1) 56(84) bytes of data.
64 bytes from localhost (127.0.0.1): icmp_seq=1 ttl=64 time=0.078 ms
64 bytes from localhost (127.0.0.1): icmp_seq=2 ttl=64 time=0.045 ms
64 bytes from localhost (127.0.0.1): icmp_seq=3 ttl=64 time=0.058 ms
64 bytes from localhost (127.0.0.1): icmp_seq=4 ttl=64 time=0.027 ms
^Z
[1]  + 75562 suspended  ping localhost
❯ jobs
[1]  + suspended  ping localhost
❯ fg %1
[1]  + 75562 continued  ping localhost
64 bytes from localhost (127.0.0.1): icmp_seq=5 ttl=64 time=0.037 ms
64 bytes from localhost (127.0.0.1): icmp_seq=6 ttl=64 time=0.037 ms
64 bytes from localhost (127.0.0.1): icmp_seq=7 ttl=64 time=0.037 ms
^C
--- localhost ping statistics ---
7 packets transmitted, 7 received, 0% packet loss, time 25128ms
rtt min
```

任务前的代号在 fg，bg，乃至 kill 命令中发挥作用。使用时需要在前面加 %，如将 2 号进程放入后台，则使用 bg %2 。

### tmux

`sudo apt install tmux`

对于一个运行中的程序，或是 SSH 远程登录创建的一个会话，此时窗口（或连接）是和它开启的进程（比如 Shell）绑定在一起。当我们关闭窗口或者断开连接时，对应的进程也随之终止了。

为了在会话结束后其开启的进程还能继续进行，我们需要先进行"解绑"，在后续需要时再重新进行绑定。tmux 完成的就是这样一个任务。

```bash
tmux new -s session_name           # 创建新的 tmux 会话
tmux detach     # 分离当前 tmux 会话，快捷键 Ctrl+B D
tmux ls         # tmux list-session
tmux attach -t <session-name> # Sessions are labeled by numbers by default
tmux kill-session -t <session-name>
```

<p align="center">
    <img src="/basic/linux&git/images/tmux.gif" alt="Linux" width="600"/>
</p>

tmux 由会话（session），窗口（window），面板（pane）组织起每个 shell 的输入框。会话用于区分不同的工作；窗口是会话中以显示屏为单位的不同的页；而面板则是一个窗口上被白线分割的不同区域。熟练掌握会话，窗口，面板之间的切换，可以极大提高使用效率。

- Ctrl + B 是 tmux 的全局前缀命令，按下该快捷键表示让 tmux 接收命令。
    
    
    | **快捷键（需先按下 Ctrl + B）** | **功能** |
    | --- | --- |
    | % | 左右分屏 |
    | " | 上下分屏 |
    | ↑ ↓ ← → | 焦点切换为上、下、左、右侧 pane，正在交互的 pane 被绿色框选中。 |
    | d (detach) | 从 tmux 中脱离，回到命令行界面 |
    | z (zoom) | 将 pane 暂时全屏，再按一次恢复原状 |
    | c | 新建窗口 |
    | , | 为窗口命名 |
    | s | 列出所有 session |
    | 1-9 | 切换到窗口 1-9 |

刚才提到如果不幸掉线，会话仍然被保存在后台，如果再次登录，可使用 `tmux attach [-t 窗口名称]` 重新连接窗口，不加 `-t` 参数将默认连接最后一次打开的窗口。

### sudo & su

- sudo


`sudo` 命令可以让你以另一个用户的身份执行指定的命令。当然，它最常见的用途，就是能让普通用户以 `root` 的身份执行命令：不加入其他参数，`sudo` 后面直接加命令，我们在前面的课程中也见到很多次了。

那么，如何以 `root` 之外的用户的身份执行命令呢？加上 `-u 用户名` 的参数即可。

```bash
$ sudo -u nobody id
uid=65534(nobody) gid=65534(nogroup) groups=65534(nogroup)
```

这里，我们就用 `nobody` 这个用户的身份，执行了 `id`，得到了 `nobody` 的 UID 等信息。


- su

`su` 命令用于直接切换用户，格式是 `su 用户名`。如果没有用户名这个参数，则切换到 `root` 用户。

在读完上面这句话之后，你可能会尝试切换到 `root`，但是却失败了：

```bash
$ su
Password:
（密码？什么密码？输我自己的密码试试？）
su: Authentication failure
$
```

这是因为，如 Ubuntu 等 Linux 发行版默认禁止了 `root` 用户的密码登录，只允许通过 `sudo` 提高权限。但是，我们可以用 `sudo` 运行 `su`，来得到一个为 `root` 用户权限的 shell。

```bash
$ sudo su
Password:
（没错，是我自己的密码）
# id
uid=0(root) gid=0(root) groups=0(root)
# exit
$
```

### chmod & chown

在 Linux 中，每个文件和目录都有自己的权限。可以使用 `ls -l` 查看当前目录中文件的详细信息。

```bash
$ ls -l
total 8
-rwxrw-r-- 1 ustc ustc   40 Feb  3 22:37 a_file
drwxrwxr-x 2 ustc ustc 4096 Feb  3 22:38 a_folder
```

第一列的字符串从左到右意义分别是：文件类型（一位）、文件所属用户的权限（三位）、文件所属用户组的权限（三位）、其他人的权限（三位）。对于每个权限，第一位 `r` 代表读取 (**R**ead)，第二位 `w` 代表写入 (**W**rite)，第三位 `x` 代表执行 (E**x**ecute)，`-` 代表没有对应的权限。

第三、四列为文件所属用户和用户组。

<p align="center">
    <img src="/basic/linux&git/images/privilege.jpg" alt="Linux" width="600"/>
</p>

例如，上面的文件 `a_file` 为普通文件 (`-`)，所属用户权限为 `rwx`，所属用户组权限为 `rw-`，其他人的权限为 `r--`，文件所属用户和用户组均为 `ustc`。

可以使用 `chmod` (**ch**ange file **mod**e bits) 修改权限，`chown` (**ch**ange file **own**er) 修改文件所有者。

```bash
$ # chmod命令
$ # 格式：chmod [who] [opt] [mode] 文件或目录名…
$ chmod u=rw,g=x test.txt
$ chmod 610 test1.txt # 9位权限转换成3个3位二进制码，获得一个3位8进制码

$ # chown命令
$ # 格式：chown [选项]… [用户][:[组]] 文件…
$ chown -R root /home/user/dest # 将目录/home/user/dest及其下所有文件和目录所有者改为root
```

## More

更多资料请参考 [拓展资料](/basic/linux&git/Extend)。