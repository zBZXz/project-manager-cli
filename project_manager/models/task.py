"""任务数据模型

用字典表示一个任务，包含以下字段：
- project_id: int  所属项目 ID
- task_id: int     任务唯一标识
- title: str       任务标题
- priority: str    优先级（high / medium / low）
- status: str      状态（todo / in_progress / done）
- description: str 任务描述
- created_at: str  创建时间
- done_at: str     完成时间
"""

from datetime import datetime

# 合法的任务状态与优先级常量
VALID_TASK_STATUSES = ("todo", "in_progress", "done")
VALID_TASK_PRIORITIES = ("high", "medium", "low")


def create_task(
    project_id: int,
    task_id: int,
    title: str,
    priority: str = "medium",
    status: str = "todo",
    description: str | None = None,
) -> dict:
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
        "done_at": now if status == "done" else None,
    }

    return task


def display_task_info(task: dict) -> None:
    """格式化打印任务信息。"""
    done_str = task["done_at"] or "（未完成）"
    print(f"[任务 #{task['task_id']}] {task['title']}")
    print(f"  所属项目: #{task['project_id']}")
    print(f"  优先级:   {task['priority']}")
    print(f"  状态:     {task['status']}")
    print(f"  创建时间: {task['created_at']}")
    print(f"  完成时间: {done_str}")


def update_task_status(task: dict, new_status: str) -> None:
    """更新任务状态。

    参数：
        task: 待更新的任务字典
        new_status: 目标状态，必须为 VALID_TASK_STATUSES 之一
    """
    # 卫语句：先拦截非法状态
    if new_status not in VALID_TASK_STATUSES:
        raise ValueError(
            f"update_task_status: 目标任务状态 '{new_status}' 不合法，合法状态为: {VALID_TASK_STATUSES}"
        )

    # 核心业务逻辑
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    task["status"] = new_status
    task["done_at"] = now if new_status == "done" else None
