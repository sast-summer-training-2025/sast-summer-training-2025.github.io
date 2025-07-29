## **目录相关**

| Command | Description | Parameter | Usage | Example |
| --- | --- | --- | --- | --- |
| `pwd` | 当前目录 |  | `pwd` |  |
| `cd` | 切换目录 |  | `cd DEST` | <ul><li>`cd ..`</li><li>`cd ~/`</li><li>`cd ./test/`</li></ul> |
| `ls` | 查看目录列表 | <ul><li>`-l` ：列出详细信息</li><li>`-a` ：列出隐藏文件</li><li>`-la` ：同时列出隐藏文件和详细信息</li></ul> | `ls -la` |  |
| `mkdir` | 新建目录 |  | `mkdir <dir_name>` | `mkdir tests` |
| `find` | 在层级目录下搜索文件 | <ul><li>`-name` ：按文件名查询</li><li>`-path` ：按路径查询</li></ul> | `find DIR <param>` | `find ./ -name '*.txt'` |

## **文件相关**

| Command | Description | Parameter | Usage | Example |
| --- | --- | --- | --- | --- |
| `touch` | 新建文件 | `-c` , `-a` , `-m`  | `touch <param> FILE` | `touch hello.c` |
| `mv` | 移动（可用于重命名） | `-f` , `-i` , `-n`, `-v` | `mv <param> FILE PATH` | <ul><li>`mv hello.c ./tools/`</li><li>`mv hello.c goodbye.c`</li></ul> |
| `cp` | 拷贝 | `-r` , `-i` | `cp <param> SOURCE DESTINATION` | `cp hello.c ../` |
| `rm` | 删除 | `-i` , `-r` , `-f`  | `rm <param> FILE/DIR` | <ul><li>`rm hello.c`</li><li>`rm -rf ./src`</li></ul> |
| `chmod`  | 更改文件权限 |  | `chmod [OPTION]... MODE[,MODE]... FILE...` |  |
| `chown` | 更改文件所属 |  | `chown [OPTION]... [OWNER][:[GROUP]] FILE...` |  |
| `echo` | 输出提供的文本 | `-e` , `-n`  | `echo [SHORT-OPTION]... [STRING]...` | `echo 'hello world!'` |
| `file` | 查看文件类型 |  |  |  |
| `cat` | 将文件内容输出到标准输出 | `-z`  | `cat <param> FILE` | `cat hello.c` |

## **用户相关**

| Command | Description |
| --- | --- |
| `useradd` | 创建用户 |
| `groupadd` | 创建组 |
| `passwd` | 更改密码 |
| `chpasswd` | 批量更改密码 |
| `su` | 一般用于切换用户 |
| `sudo` | 一般用于执行 root 权限指令 |

## **其他命令**

| Command | Description | Example |
| --- | --- | --- |
| `clear` | 清屏 | `clear` |
| `history` | 查看历史命令 | `history` |
| `alias` | 创建命令别名 | <ul><li>`alias ll='ls -la'`</li><li>`alias gs='git status'`</li></ul> |
| `tar` / `gzip` / `gunzip` / `zip` / `unzip` | 文件打包与压缩/解压 | <ul><li>`tar -cvf archive.tar files/`</li><li>`tar -xvf archive.tar`</li><li>`gzip file.txt`</li><li>`gunzip file.txt.gz`</li><li>`zip archive.zip file.txt`</li><li>`unzip archive.zip`</li></ul> |
| `shutdown` / `halt` / `reboot` | 关机/重启相关 | <ul><li>`shutdown -h now`</li><li>`halt`</li><li>`reboot`</li></ul> |
| `uname` | 显示系统信息 | `uname -a` |
| `grep` | 使用正则表达式查找文件中的模式 | <ul><li>`grep -i 'fn' src/main.rs`</li><li>`cat src/main.rs \| grep -c 'fn'`</li></ul> |
| `ps` | 查看进程 | `ps` |
| `systemctl` | 控制 systemd 系统和服务管理器 | <ul><li>`systemctl status`</li><li>`systemctl start|stop|restart|reload|status <service>`</li></ul> |
| `ip` | 查看路由，设备等信息 | `ip address` |

## **Shell Operations**

| Operator | Description | Example |
| --- | --- | --- |
| `&` | 允许命令在后台执行 | `cp -r ./here ./there &` |
| `&&` | 执行多条指令，逻辑和 C++ 类似 | `wget someurl/install.sh . && ./install.sh` |
| `>` | 重定向输出 | `echo "Hello" > hello.txt` |
| `<` | 重定向输入 | `./main < in.txt` |
| `>>` | 重定向输出并采取“追加”模式 | `echo cirno >> visitors.txt` |
| `|` | 管道符，将前者的输出作为后者的输入 | `ls ~/Documents | grep note.txt` |

## **网络相关**

| Command | Description | Example |
| --- | --- | --- |
| `ping` | 测试网络连通性 | `ping www.baidu.com` |
| `curl` | 发送网络请求 | `curl https://www.example.com` |
| `wget` | 下载文件 | `wget https://www.example.com/file.txt` |
| `ifconfig` | 查看和配置网络接口 | `ifconfig` |
| `netstat` | 查看网络连接和端口 | `netstat -tuln` |

## **进程查询相关**

| Command | Description | Example |
| --- | --- | --- |
| `top` | 实时显示进程信息 | `top` |
| `htop` | 更友好的进程查看工具 | `htop` |
| `ps aux` | 显示所有进程详细信息 | `ps aux` |
| `kill` | 终止进程 | `kill <PID>` |
| `pkill` | 按名称终止进程 | `pkill firefox` |

## **Shell 变量相关**

| Operator/Command | Description | Example |
| --- | --- | --- |
| `VAR=value` | 定义变量 | `NAME=cirno` |
| `$VAR` | 访问变量 | `echo $NAME` |
| `export VAR=value` | 导出为环境变量 | `export PATH=$PATH:/new/path` |
| `unset VAR` | 删除变量 | `unset NAME` |