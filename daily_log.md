# 每日学习记录

## Day 1 — 2026-11-09

**今日学习主题：** 开发环境、Python 解释器、变量、数据类型

**完成的任务：**
1. 确认 Python 3.12.7 和 Git 2.51.0 已安装
2. 创建 conda 环境 `project_manager`（Python 3.12）
3. 初始化 Git 仓库，配置 `.gitignore`
4. 创建项目目录结构（models / services / storage / data）
5. 创建 `main.py` 入口文件并验证运行成功
6. 编写 `README.md`
7. 完成首次 Git 提交
8. 创建 GitHub 仓库 (zBZXz/project-manager-cli)，配置 SSH 远程地址并推送成功
9. 编写 Day 1 数据类型练习脚本 `practice/day01_data_types.py`
10. 练习了 Python 基础数据类型：str、int、float、bool、None
11. 用字典模拟了"项目"和"任务"的数据结构
12. 练习了类型转换：int()、str()、bool()

**遇到的问题：**
1. `git push -u origin main` 认证失败
   - 原因：远程地址用了 HTTPS，GitHub 已不支持密码认证
   - 解决：`git remote set-url origin git@github.com:zBZXz/project-manager-cli.git` 切换为 SSH
2. 最初使用了 venv，后改为 conda 环境管理
   - 原因：个人习惯使用 conda 管理环境
   - 解决：删除 venv 目录，创建 conda 环境 `project_manager`

**今天真正理解的内容：**
1. conda 环境的作用：隔离项目依赖，统一管理不同项目的 Python 版本和包
2. `.gitignore` 的作用：告诉 Git 忽略不需要追踪的文件（如 __pycache__、.pyc）
3. GitHub 的 HTTPS 与 SSH 两种认证方式的区别
4. Python 基础数据类型：str、int、float、bool、None 以及 `type()` 查看类型
5. 字典（dict）可以用来组织结构化数据（如项目信息、任务信息）
6. 类型转换时的注意点：空字符串、0、None 转 bool 都是 False

**仍未理解的内容：**
1. （待补充）

**明日计划：**
1. 学习字符串、数字、布尔值、类型转换的更多用法
2. 设计项目的基本信息字段（名称、描述、状态、创建时间等）
3. 在 `models/project.py` 中开始实现
