"""
任务数据模型

用字典表示一个任务，字段如下：
project_id: int  所属项目
id: int          唯一标识
title: str       任务标题
priority: str    优先级（high / medium / low）
status: str      状态（todo / in_progress / done）
created_at: str  创建时间
done_at: str     完成时间
"""

from datetime import datetime


def create_task(project_id: int, task_id: int, title: str, priority: str = "medium", status: str = "todo", description: str = None):
    """创建一个新任务，返回字典。"""
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")


    task = {
        "project_id": project_id,
        "task_id": task_id,
        "title": title,
        "priority": priority,
        "status": status,
        "description": description,
        "created_at": now,
        "done_at": None,
    }

    return task

def display_task_info(task):
    """格式化打印任务信息"""
    print(f"[任务 #{task['task_id']}] {task['title']}")
    print(f"  优先级:   {task['priority']}")
    print(f"  状态:     {task['status']}")
    print(f"  创建时间: {task['created_at']}")
    print(f"  完成时间: {task['done_at']}")
