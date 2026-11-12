"""项目数据模型

用字典表示一个项目，包含以下字段：
- id: int          唯一标识
- name: str        项目名称
- description: str 项目描述
- status: str      状态（active / completed / archived）
- created_at: str  创建时间
- updated_at: str  最后更新时间
"""

from datetime import datetime

# 用一个模块级变量来自增 ID
_next_id = 1


def create_project(name, description=""):
    """创建一个新项目，返回一个字典。

    参数：
        name: 项目名称（字符串）
        description: 项目描述（字符串，可选）

    返回：
        一个包含项目信息的字典
    """
    global _next_id

    # 当前时间
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    project = {
        "id": _next_id,
        "name": name,
        "description": description,
        "status": "active",
        "created_at": now,
        "updated_at": now,
    }

    _next_id += 1
    return project


def display_project_info(project):
    """格式化打印项目信息。"""
    print(f"[项目 #{project['id']}] {project['name']}")
    print(f"  描述:     {project['description'] or '（无）'}")
    print(f"  状态:     {project['status']}")
    print(f"  创建时间: {project['created_at']}")
    print(f"  更新时间: {project['updated_at']}")
