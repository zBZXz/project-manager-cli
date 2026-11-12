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

---

## Day 2~4 — 2026-11-12

**今日学习主题：** 模块与包结构设计、`__init__.py` 底层机制、任务数据模型实现

**完成的任务：**
1. 独立编写并完善 `models/task.py` 任务模型（支持 `project_id`, `task_id`, `title`, `priority`, `status`, `description` 等）
2. 在 `models/task.py` 中实现默认值参数配置，修复时间格式化（`%m` 月份与 `%M` 分钟的区别）
3. 补充了各包目录下的 `__init__.py` 文件（`project_manager/`、`models/`、`services/`、`storage/`）
4. 将主入口 `main.py` 的导入方式统一规范为绝对包路径 `from project_manager.models...`
5. 验证根目录下使用 `python -m project_manager.main` 成功运行
6. 深入探讨并整理技术专题笔记：[Python 包管理机制与 `__init__.py` 深度解析](notes/python_package_and_init.md)

**遇到的问题：**
1. `datetime.now().strftime("%Y-%M-%d")` 输出了错误的日期
   - 原因：`%M` 代表 Minute（分钟），月份必须使用小写 `%m`（Month）
   - 解决：修改为 `%Y-%m-%d %H:%M:%S`
2. `ModuleNotFoundError: No module named 'models'` 报错
   - 原因：在项目根目录下使用 `-m` 执行时，`sys.path[0]` 为根目录，直接 `from models` 无法被识别
   - 解决：使用正规包导入 `from project_manager.models...`
3. 对比了现代 Python 3.3+ (PEP 420) 不写 `__init__.py` 与写 `__init__.py` 的区别

**今天真正理解的内容：**
1. **常规包 vs 命名空间包**：
   - 有 `__init__.py`：声明独立完整的包，遇到同名目录会**排他遮蔽**，防止被外部同名文件夹意外污染；
   - 无 `__init__.py`：允许多个不同物理路径下的同名文件夹**合并拼装**（如企业级大库/SDK 插件）。
2. **`python -m` 运行机制**：将代码置于根包命名空间下运行，统一了模块解析路径，是工程化标准规范。
3. **参数默认值与类型注解**：提高函数的易用性与代码自解释性。

**仍未理解的内容：**
1. （待补充）

**明日计划：**
1. 在 `models/task.py` 中补充状态流转函数 `update_task_status`，自动联动 `done_at`
2. 学习 List 与 Dict 的高级操作，实现根据条件过滤和查询任务列表
