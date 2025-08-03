# 课前准备：Django

本节将帮助你完成 Django 开发环境的搭建与测试工具 Postman 的安装和基础配置。

---

## 一、安装 Django 环境

确保你已正确安装 Python，并了解如何使用包管理工具（如 pip）安装第三方包。例如，通过pip安装django的指令如下：

```bash
pip install django
```

### 检查 Django 是否安装成功

安装完成后，在命令行输入以下命令，检查 Django 版本：

```bash
python -m django --version
```

如果能正确输出版本号（如 `5.1.6`），说明安装成功。

### 创建并运行第一个 Django 项目（可选）

你可以通过以下命令快速体验 Django 项目：

```bash
django-admin startproject proj
cd proj
python manage.py runserver
```

浏览器访问 http://localhost:8000/，看到 Django 欢迎页面即说明环境配置无误。

---

## 二、安装与配置 Postman

Postman 是常用的 API 测试工具，可以帮助你快速测试和调试接口。
访问 [Postman 官方网站](https://www.postman.com/) 以下载并安装对应操作系统的客户端。