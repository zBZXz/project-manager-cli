# Python 实战避坑指南与工程规范笔记

本文档总结了在开发「AI 项目管理与任务记录系统 (CLI)」过程中遇到的一系列典型问题、Bug 诱因、解决方案以及工业级最佳实践。

---

## 目录

- [一、 基础语法与条件逻辑陷阱](#一-基础语法与条件逻辑陷阱)
  - [1.1 条件判断中的 Truthy 陷阱（`or` 运算机制）](#11-条件判断中的-truthy-陷阱or-运算机制)
  - [1.2 字符串 `"None"` 与内置对象 `None` 的混淆](#12-字符串-none-与内置对象-none-的混淆)
  - [1.3 数据状态联动的一致性处理](#13-数据状态联动的一致性处理)
- [二、 控制流与函数设计规范](#二-控制流与函数设计规范)
  - [2.1 防御式编程与「卫语句（Guard Clause）」](#21-防御式编程与卫语句guard-clause)
  - [2.2 列表推导式的适用场景：集合筛选 vs 单项查找](#22-列表推导式的适用场景集合筛选-vs-单项查找)
  - [2.3 迭代中的变量名混淆与短路退出](#23-迭代中的变量名混淆与短路退出)
- [三、 文件持久化与 I/O 异常处理](#三-文件持久化与-io-异常处理)
  - [3.1 `os.makedirs` 目录已存在报错（`FileExistsError`）](#31-osmakedirs-目录已存在报错fileexistserror)
  - [3.2 目录创建与文件打开的「因果先后顺序」](#32-目录创建与文件打开的因果先后顺序)
  - [3.3 文件读取时的防御性异常捕获（平稳降级）](#33-文件读取时的防御性异常捕获平稳降级)
- [四、 工程规范与代码整洁度（Clean Code）](#四-工程规范与代码整洁度clean-code)
  - [4.1 消除魔法值（Magic Values）与常量抽离](#41-消除魔法值magic-values与常量抽离)
  - [4.2 保持一致的动词命名规范](#42-保持一致的动词命名规范)
  - [4.3 避免平台死绑的硬编码绝对路径](#43-避免平台死绑的硬编码绝对路径)

---

## 一、 基础语法与条件逻辑陷阱

### 1.1 条件判断中的 Truthy 陷阱（`or` 运算机制）

#### ❌ 常见踩坑代码
```python
elif new_status == "todo" or "in_progress":
    task["done_at"] = None
```

#### 🔍 核心原理与原因
在 Python 中，比较运算符（`==`）的优先级高于逻辑运算符（`or`）。上述代码的实际求值顺序等价于：
```python
(new_status == "todo") or ("in_progress")
```
- 如果 `new_status` 为 `"done"`，左侧 `new_status == "todo"` 为 `False`；
- Python 继续计算右侧表达式 `"in_progress"`；
- **非空字符串在布尔上下文中永远被视为真值（Truthy）**；
- 最终结果等同于 `False or True` -> **永远为 `True`**！这会导致该分支永远被误触发。

#### ✅ 正确写法
```python
# 方式 1：使用 in 配合元组/集合（推荐，简洁且易于扩展）
elif new_status in ("todo", "in_progress"):
    task["done_at"] = None

# 方式 2：显式写全两个比较表达式
elif new_status == "todo" or new_status == "in_progress":
    task["done_at"] = None
```

---

### 1.2 字符串 `"None"` 与内置对象 `None` 的混淆

#### ❌ 常见踩坑代码
```python
task["done_at"] = "None"  # 误存为字符串
```

#### 🔍 核心原理与原因
- Python 的 `None` 是一个唯一的单例内置对象（表示空/未定义值），其布尔转换结果为 `False`：`bool(None) == False`。
- 字符串 `"None"` 是一个包含 4 个字符的普通字符串，其布尔转换结果为 `True`：`bool("None") == True`。
- 如果在业务逻辑中判断 `if task["done_at"]:`，存入字符串 `"None"` 会被错误地识别为“该任务已有完成时间”，引发致命的逻辑漏洞。

#### ✅ 正确写法
```python
task["done_at"] = None  # 裸写 None，不加引号
```

---

### 1.3 数据状态联动的一致性处理

#### ❌ 常见踩坑代码
```python
def create_task(..., status: str = "todo"):
    task = {
        ...,
        "status": status,
        "done_at": None,  # 硬编码写死为 None
    }
```
**问题表现**：当调用方传入 `create_task(..., status="done")` 时，虽然任务标记为已完成，但完成时间却依然是 `None`，造成数据状态不一致。

#### ✅ 正确写法（三元表达式联动）
```python
task = {
    ...,
    "status": status,
    "done_at": now if status == "done" else None,
}
```

---

## 二、 控制流与函数设计规范

### 2.1 防御式编程与「卫语句（Guard Clause）」

#### ❌ 传统互斥平级 `if`
```python
def update_task_status(task: dict, new_status: str) -> None:
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if new_status in ("todo", "in_progress", "done"):
        task["status"] = new_status
        task["done_at"] = now if new_status == "done" else None

    if new_status not in ("todo", "in_progress", "done"):
        raise ValueError(f"目标任务状态不合法 {new_status}")
```
**缺点**：
1. 条件互斥却写了两个平级 `if`，多做一次判断；
2. 即使参数非法，也会提前无谓地执行 `datetime.now()` 浪费开销；
3. 核心业务逻辑被迫缩进在 `if` 块内部。

#### ✅ 卫语句写法（Guard Clause）
```python
def update_task_status(task: dict, new_status: str) -> None:
    """更新任务状态"""
    # 1. 卫语句：前置参数校验，非法立即阻断
    if new_status not in VALID_TASK_STATUSES:
        raise ValueError(f"目标任务状态不合法: '{new_status}'")

    # 2. 核心业务平铺书写，结构清爽
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    task["status"] = new_status
    task["done_at"] = now if new_status == "done" else None
```

---

### 2.2 列表推导式的适用场景：集合筛选 vs 单项查找

#### ❌ 单项查找误用列表推导式
```python
# 函数签名声明返回单个字典或 None
def get_project_by_id(projects: list[dict], project_id: int) -> dict | None:
    return [project for project in projects if project["id"] == project_id]
```

#### 🔍 问题分析：
1. **类型不匹配**：列表推导式 `[...]` 永远返回 `list`。找到时返回 `[{...}]`，找不到时返回 `[]`，外部用字典方式取值会引发 `TypeError`。
2. **无法短路退出**：即使列表中有 10,000 个元素，且目标正是第 1 个，列表推导式仍会固执地遍历全部 10,000 个元素，性能低下。

#### ✅ 规则与对应写法：
- **筛选多个结果（集合）**：使用列表推导式。
  ```python
  def filter_projects_by_status(projects: list[dict], status: str) -> list[dict]:
      return [p for p in projects if p["status"] == status]
  ```
- **唯一键单项查找**：使用经典 `for` 循环提前 `return`（或 `next`）：
  ```python
  def get_project_by_id(projects: list[dict], project_id: int) -> dict | None:
      for project in projects:
          if project["id"] == project_id:
              return project  # 找到立刻返回，提前终止循环
      return None             # 查无结果平稳返回 None
  ```

---

### 2.3 迭代中的变量名混淆与短路退出

#### ❌ 容易忽视的变量名笔误
```python
return next((project for project in projects if project["id"] == project), None)
```
**问题**：误将比较目标 `project_id` 写成了循环变量 `project`。`project["id"]` 是整数，`project` 是字典，两者永远不可能相等，导致函数永远返回 `None`。

---

## 三、 文件持久化与 I/O 异常处理

### 3.1 `os.makedirs` 目录已存在报错（`FileExistsError`）

#### ❌ 现象与报错
```python
os.makedirs(os.path.dirname(file_path))
# 抛出：FileExistsError: [WinError 183] 当文件已存在时，无法创建该文件
```

#### 🔍 解决方案：
`os.makedirs` 默认参数 `exist_ok=False`。如果目录已存在，系统视作创建冲突。  
必须显式加上 `exist_ok=True`：
```python
dir_name = os.path.dirname(file_path)
if dir_name:  # 避免同级相对路径时 dir_name 为空字符串引发异常
    os.makedirs(dir_name, exist_ok=True)
```

---

### 3.2 目录创建与文件打开的「因果先后顺序」

#### ❌ 错误的嵌套顺序
```python
with open(file_path, "w", encoding="utf-8") as f:
    os.makedirs(os.path.dirname(file_path), exist_ok=True)  # 顺序反了！
```
**隐患**：操作系统在执行 `with open(..., "w")` 时，**要求目标目录必须已存在**。如果目录尚不存在，程序在执行到 `open` 的瞬间就抛出 `FileNotFoundError` 崩溃了，根本走不到下一行的 `os.makedirs`。

#### ✅ 正确顺序：先建目录，后开文件
```python
dir_name = os.path.dirname(file_path)
if dir_name:
    os.makedirs(dir_name, exist_ok=True)

with open(file_path, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4, ensure_ascii=False)
```

---

### 3.3 文件读取时的防御性异常捕获（平稳降级）

#### ❌ 裸奔的读取代码
```python
def load_data(file_path: str) -> list | dict:
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)
```
**隐患**：
1. 软件首次安装/启动时，数据文件尚未生成，抛出 `FileNotFoundError`；
2. 数据文件被意外清空或损坏时，抛出 `json.JSONDecodeError`。

#### ✅ 工业级防御写法（Graceful Degradation）
```python
def load_data(file_path: str) -> list | dict:
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"提示: 文件 '{file_path}' 不存在，初始化返回空数据")
        return []
    except json.JSONDecodeError:
        print(f"警告: 文件 '{file_path}' 损坏或为空，已平稳降级返回空数据")
        return []
```

---

## 四、 工程规范与代码整洁度（Clean Code）

### 4.1 消除魔法值（Magic Values）与常量抽离

- **问题**：在 `create_task`、`update_task_status` 中反复出现 `("todo", "in_progress", "done")`。如果未来新增 `"cancelled"` 状态，容易漏改。
- **最佳实践**：遵循 **DRY 原则（Don't Repeat Yourself）**，在模块顶部声明全局常量：
  ```python
  VALID_TASK_STATUSES = ("todo", "in_progress", "done")
  VALID_TASK_PRIORITIES = ("high", "medium", "low")
  ```

### 4.2 保持一致的动词命名规范

- **问题**：服务层中同时存在 `get_tasks_by_project_id`、`get_tasks_by_status` 与 `high_priority_tasks`。
- **最佳实践**：服务层方法应统一遵循动词命名规范（如统一使用 `get_...` 或 `filter_...` 前缀），重命名为 `get_high_priority_tasks`，增强 API 的自解释性与一致性。

### 4.3 避免平台死绑的硬编码绝对路径

- **问题**：代码中写死 `r"D:\personal-project\..."`，换电脑或部署到 Linux 服务器时必定报错。
- **最佳实践**：使用基于当前文件位置的动态路径解析（`pathlib.Path`）：
  ```python
  from pathlib import Path

  # 无论项目部署在什么操作系统、什么盘符，都能精准定位 data 目录
  DATA_DIR = Path(__file__).resolve().parent / "data"
  PROJECT_FILE = DATA_DIR / "project.json"
  ```
