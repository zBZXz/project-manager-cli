"""任务服务层"""


def get_tasks_by_project_id(tasks: list[dict], project_id: int) -> list[dict]:
    """获取指定项目下的所有任务。"""
    return [task for task in tasks if task["project_id"] == project_id]


def get_tasks_by_status(tasks: list[dict], status: str) -> list[dict]:
    """根据状态筛选任务。"""
    return [task for task in tasks if task["status"] == status]


def get_high_priority_tasks(tasks: list[dict]) -> list[dict]:
    """获取所有高优先级且尚未完成的任务。"""
    return [
        task
        for task in tasks
        if task["priority"] == "high" and task["status"] != "done"
    ]
