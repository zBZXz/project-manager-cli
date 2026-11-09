"""
Day 1 练习：Python 数据类型探索
运行方式：python practice/day01_data_types.py
"""

# ========== 1. 基础数据类型 ==========

# 字符串 str
project_name = "AI 项目管理系统"
print(f"项目名称: {project_name}, 类型: {type(project_name)}")

# 整数 int
project_id = 1
print(f"项目 ID: {project_id}, 类型: {type(project_id)}")

# 浮点数 float
progress = 0.0
print(f"进度: {progress}, 类型: {type(progress)}")

# 布尔值 bool
is_active = True
print(f"是否激活: {is_active}, 类型: {type(is_active)}")

# None —— 表示"还没有值"
description = None
print(f"描述: {description}, 类型: {type(description)}")

print()

# ========== 2. 用字典模拟一个"项目" ==========

project = {
    "id": 1,                          # int
    "name": "AI 项目管理系统",          # str
    "description": "一个 CLI 工具",     # str
    "status": "active",               # str
    "created_at": "2026-11-09",       # str
}

print("===== 项目信息 =====")
print(f"ID:       {project['id']}")
print(f"名称:     {project['name']}")
print(f"描述:     {project['description']}")
print(f"状态:     {project['status']}")
print(f"创建时间: {project['created_at']}")

print()

# ========== 3. 用字典模拟一个"任务" ==========

task = {
    "id": 1,                          # int
    "project_id": 1,                  # int —— 属于哪个项目
    "title": "搭建开发环境",            # str
    "priority": "high",               # str —— high / medium / low
    "status": "done",                 # str —— todo / in_progress / done
    "created_at": "2026-11-09",       # str
}

print("===== 任务信息 =====")
print(f"ID:       {task['id']}")
print(f"所属项目: {task['project_id']}")
print(f"标题:     {task['title']}")
print(f"优先级:   {task['priority']}")
print(f"状态:     {task['status']}")
print(f"创建时间: {task['created_at']}")

print()

# ========== 4. 类型转换练习 ==========

print("===== 类型转换 =====")

# str -> int
user_input = "42"
number = int(user_input)
print(f"'{user_input}' 转为 int: {number}, 类型: {type(number)}")

# int -> str
id_str = str(project_id)
print(f"{project_id} 转为 str: '{id_str}', 类型: {type(id_str)}")

# str -> bool（注意：非空字符串都是 True）
print(f"bool('hello') = {bool('hello')}")
print(f"bool('')      = {bool('')}")
print(f"bool(0)       = {bool(0)}")
print(f"bool(1)       = {bool(1)}")
print(f"bool(None)    = {bool(None)}")

print()
print("练习完成！试着修改上面的值，观察输出有什么变化。")
