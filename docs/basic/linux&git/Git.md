# Git

## 为什么需要 Git ？

在大家日常开发的场景中，往往会遇到如下情景：

- 写了半天的代码最后发现跑不通，调来调去结果回不到一开始的版本了
- 自己一周之前写的代码没打注释，结果一周之后不知道当时是怎么想的了
- 和他人合作开发，结果使用微信/邮件传压缩包，不知道队友改动了哪些地方，合并起来极其麻烦

以上等等问题，都在 Git 下得到了很好的解决。通过 Git，你可以

- 跟踪每一次代码修改，方便回溯和恢复历史版本。
- 支持多人协作开发，解决代码合并和冲突问题。
- 便于分支管理，实验新功能不会影响主线代码。
- 提高项目的安全性和可靠性，防止数据丢失。

## Git 基本概念

### 分布式版本控制系统

Git 是一种分布式的版本控制系统，由 Linus Torvalds研制和开发，为了帮助管理Linux内核开发而开发的一个开源的版本控制软件，并逐渐成为行业标准。

所谓分布式，就是每个开发者的本地仓库都完整地保存了项目的所有版本历史，而不仅仅是服务器上的一个副本。这样即使没有网络连接，开发者也可以在本地进行提交、查看历史、分支等操作，等到有网络时再与远程仓库进行同步。

### 工作区 & 暂存区

在 Git 分布式版本控制中，我们一般把除 `.git` 文件夹外的所有文件（包括项目文件和其他资源文件）称为 **工作区（Working Directory）**。将在工作区中通过修改并完成添加（指 `git add`）的内容记录到 **暂存区（Staging Area）**中。

通过 `git commit`，可以将暂存区中的更改提交到本地仓库。通过 `git push`，可以将本地仓库的更改同步到远程仓库上。

<p align="center">
        <img src="/basic/linux&git/images/Repo.png" alt="Linux" width="800"/>
</p>

### 提交与分支

软件工程课程上的这页 PPT 很好展现了 Git 版本管理中的一些最常见的概念：

<p align="center">
        <img src="/basic/linux&git/images/branch.png" alt="Linux" width="800"/>
</p>

Git 的原理是存储 Diff，换言之，Git记录的是每一次提交相比较于上一次提交的修改。

以下内容摘自 Fuyuki 学长的 Linux Git 讲义：

> - Git 以 commit（提交）作为版本控制的节点，通过 commit 可以查询到这次提交相对上次提交的修改状况，以及提交者的信息。

> - Git 规定一个项目通常(*)只存在一个 Commit 不存在“上次提交”，这个 Commit 被称作 Init Commit。 

> - Branch（分支）是 指向树上某个 Commit 的指针。每个 Branch 都代表了一个独立版本，开发者可以在不同分支上独立修改提交。
>     - 因为 Branch 的指针特性，创建和删除 Branch 的过程非常迅速。
>     - 同时，对 Branch 进行的操作不会影响已有的 Commit。

> - Branch 的合并被用来综合不同分支上的工作，若无法自动综合则会出现名为“合并冲突”的错误。

<p align="center">
        <img src="/basic/linux&git/images/git_merge.png" alt="Linux" width="800"/>
</p>

## Git 基本操作

### 创建本地仓库

- 使用 `git init` 初始化当前目录为 Git 仓库。
- 使用 `git init <目录名>` 在指定目录创建仓库。

### 克隆远程仓库

- 使用 `git clone <仓库地址> [目录名]` 克隆远程仓库到本地。

### 暂存与撤销文件

- 使用 `git add <文件/目录>` 将更改添加到暂存区。
- 使用 `git restore <文件>` 或 `git checkout -- <文件>` 撤销工作区修改。

### 提交修改

- 使用 `git commit -m "提交说明"` 提交暂存区内容到本地仓库。
- 使用 `git log` 查看提交历史。

### 删除文件（rm）

- 使用 `git rm <文件>` 删除工作区和暂存区中的指定文件，并记录到下次提交。
- 若只想从暂存区移除文件但保留工作区文件，可用 `git rm --cached <文件>`。

### 远程仓库操作

- 使用 `git remote add <远程名> <仓库地址>` 添加远程仓库。
- 使用 `git push <远程名> <分支名>` 推送本地分支到远程仓库。
- 使用 `git pull <远程名> <分支名>` 拉取远程分支并合并到本地分支。

### 分支管理

- 使用 `git branch` 查看本地分支。
- 使用 `git branch <分支名>` 创建新分支。
- 使用 `git checkout <分支名>` 或 `git switch <分支名>` 切换分支。  
- 使用 `git merge <分支名>` 合并指定分支到当前分支。
- 使用 `git branch -d <分支名>` 删除本地分支。
> 从 Git 2.23 版本开始，推荐使用 `git switch` 命令来切换分支，替代传统的 `git checkout`。`git switch` 更加直观，专注于分支切换操作，使用体验更友好。

### 合并（merge）

- 使用 `git merge <分支名>` 将指定分支的更改合并到当前分支。合并时可能会遇到冲突，需要手动解决后再提交。
- 合并适用于将功能分支的开发成果整合到主分支。

### 变基（rebase）

- 使用 `git rebase <分支名>` 可以将当前分支的提交“移动”到目标分支之后，使提交历史更线性。
- 变基适合整理提交历史，但在多人协作时需谨慎使用，避免影响他人分支。

!!! 关于Merge和Rebase的区别与联系

    **Merge** 和 **Rebase** 都是用于整合分支的 Git 操作，但它们的原理和效果不同：

    - **Merge（合并）**：将目标分支的最新提交合并到当前分支，保留所有分支的历史轨迹。合并后会生成一个新的“合并提交”，历史记录呈现为分叉和汇合的结构，便于追踪分支的开发过程。
        - 优点：保留分支历史，适合多人协作。
        - 缺点：提交历史可能较为复杂。

    - **Rebase（变基）**：将当前分支的提交“移动”到目标分支的最新提交之后，使提交历史变得线性。不会生成合并提交，历史看起来更简洁。
        - 优点：提交历史清晰，便于回溯。
        - 缺点：可能会重写历史，不适合已推送到远程、多人协作的分支。

    假设你在 feature 分支上开发，有如下提交历史：

    ```
    main:     A --- B
                    \
    feature:             C --- D --- E
    ```

    现在 main 上有人新增了 F：

    ```
    main:     A --- B --- F
                    \
    feature:             C --- D --- E
    ```
    
    你执行：
    ```
    git merge：
            A --- B --- F
                    \    \
    feature:            C --- D --- E --- M  ← merge commit
    ```
    Git 要一次性合并 CDE 和 F 的差异，冲突可能集中爆发。

    若是 git rebase，Git 会执行下面的步骤：
    ```
    基于 F 依次应用：
    F + C → C'
    C' + D → D'
    D' + E → E'
    ```
    每次只有一个提交，冲突一旦发生，更容易知道是哪个改动引起的。

    冲突解决后继续，不影响其他提交。


### 其他常用操作

- 使用 `git status` 查看当前状态。
- 使用 `git diff` 查看未暂存的更改。
- 使用 `git stash` 临时保存当前修改。
- 使用 `git fetch` 获取远程更新但不合并。

## Git in IDE

现代集成开发环境（IDE）如 Visual Studio Code 和 JetBrains 系列（如 IntelliJ IDEA、PyCharm、WebStorm 等）都对 Git 提供了强大的原生支持，使得版本控制操作更加便捷和可视化。

### Visual Studio Code

- 内置 Git 支持，无需额外插件。
- 侧边栏可直接查看文件更改、提交历史、分支管理等。
- 支持通过图形界面进行 `add`、`commit`、`push`、`pull` 等操作。
- 可安装扩展（如 GitLens）获得更丰富的功能，如代码作者追踪、提交对比等。

<p align="center">
        <img src="/basic/linux&git/images/VSCode.png" alt="Git" width="800"/>
</p>

### JetBrains IDE

- 所有 JetBrains IDE 都集成了 Git 工具。
- 提供可视化的分支管理、合并、变基等高级操作。
- 支持冲突解决、历史回溯、变更对比等功能。
- 通过工具栏和右键菜单即可完成大部分 Git 操作，无需命令行。

<p align="center">
        <img src="/basic/linux&git/images/JetBrains_1.jpg" alt="Git" width="800"/>
</p>

<p align="center">
        <img src="/basic/linux&git/images/JetBrains_2.jpg" alt="Git" width="800"/>
</p>


## Git Config

关于 Git 的安装，你可以参考 [Git 官方网站](https://git-scm.com/downloads) 进行安装，此处不过多展开。

安装完成 Git 后，你需要通过 `git config` 指令进行 git 配置。

> Git 的配置分为三个等级：system 级，global 级、local 级。

> - system 级的配置影响这台电脑上的所有用户和所有仓库，使用 --system 参数。

> - global 级的配置影响当前用户的所有仓库，使用 --global 参数。

> - local 级的配置仅影响当前仓库，不添加以上参数时默认是此等级。

第一次使用 git 时，需要设置个人信息用于 commit：

- git config --global user.name "Your Name"

- git config --global user.email "email@example.com"

这部分信息将会显示在 Commit 中。


## 一些 Git 使用的常识与原则


### .gitignore & Git LFS

在绝大部分的 Git 仓库中，你并不需要上传程序编译运行的结果、训练模型的输出等等，请通过编写 `.gitignore` 文件保持远程仓库的整洁与干净。

另一方面，Git 记录 Diff，但是对于二进制大文件，尤其是图片、视频、模型等，Git 无法给出正确的 Diff，从而会倾向于把整个文件删掉重新上传。这会导致如果你有一个 100MB 的模型，你每次微调了一点，提交10次之后你的 Git 仓库就记录了10份不同的版本，也就是 1 GB，即使你并不需要前面的 9 个版本。特别对于规模更大的项目，如果每次 clone 都伴随着大量无用的文件，这是不太能接受的。

因此，你可以通过 Git LFS（Large File Storage）来解决这一问题。LFS 通过将仓库里的文件转换成一个指向 LFS 服务器的指针，使得用户能够在需要的时候再来下载这个文件。你可以通过在 Linux 下安装 `git-lfs` 包，随后通过 `git lsf init` 初始化 LFS。

更多信息可以参考 [Git LFS](https://git-lfs.com/)。

### Commit Message

你每次 `git commit` 的时候，可以通过 `-m` 参数指定 commit 信息，也可以不输入 `-m` 参数，此时 Git 会自动进入编辑器让用户填写 commit message。

在团队协作中，规范清晰的 commit message 有助于他人（也包括你自己）快速了解某条 commit 的用意与修改内容。

此处介绍 Commit Message 的 [Angular 规范](https://www.conventionalcommits.org/en/v1.0.0/)。

**Commit Message 格式**

推荐采用如下格式：

```
<type>[optional scope]: <description>

[optional body]

[optional footer(s)]
```

- `type`：本次提交的类型，如 feat（新功能）、fix（修复 bug）、docs（文档）、style（格式）、refactor（重构）、test（测试）、chore（杂项）。
- `scope`：本次提交影响的范围（可选），如模块名、文件名等。
- `description`：简要描述本次提交的内容，建议使用动词开头，简洁明了。

示例：

```
feat(login): 添加用户登录功能
fix(api): 修复数据接口返回错误
docs(readme): 更新项目说明文档
style: 调整代码缩进和格式
refactor(user): 重构用户模块逻辑
```

**编写建议**

- 使用中文或英文均可，但要保持团队一致性。
- 保持简洁，避免冗长描述。
- 一次 commit 只做一件事，避免混合多个不相关的修改。
- 必要时可在 subject 下方补充详细说明。

更多规范内容可参考 [Conventional Commits](https://www.conventionalcommits.org/zh-hans/v1.0.0/)。

### 分支管理

善用分支管理，在不同的分支上开发不同的功能，尽量做到互不干扰：

- `main` / `master` : 主分支，用于发布稳定版本。
- `dev` : 开发分支，用于发布新功能、测试不太稳定的版本。
- 其他分支用于开发特定功能：
    - `feature-xxx`: 功能开发分支
    - `test-xxx`: 测试分支
    - `bugfix-xxx`: bug 修复分支
    - ...

每次开发完一个完整的功能，可以通过 `merge request` 向 `dev` 或 `main` 分支提交修改，在经过团队他人审核通过后可以合并并删除功能分支。

**Note**：应养成保持清晰的开发历史和分支管理的习惯，不要一个项目只有一个 Commit （

### Fork & Pull Request

**Fork & Pull 模式** 是当今众多大型团队项目的重要工作模式，也是许多开源项目在 Github 上接受来自全世界开发者的贡献代码的方式。

一次 Fork & Pull 的流程大致为：

1. 项目的使用者或开发者提出 Issue 要求新功能或者找到 bug。

2. 某人看到 Issue 后，将原仓库 Fork 到自己的账户下进行修改。

3. 将修改好的新版本（分支）提出 Pull Request（合并请求，PR）给原项目。

4. 经过测试和原项目的维护者审核后，将该分支合并到原项目中。

