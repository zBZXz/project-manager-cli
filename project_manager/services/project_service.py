"""项目服务层"""


def get_project_by_id(projects: list[dict], project_id: int) -> dict | None:
    """根据 ID 查找项目，若不存在返回 None。"""
    for project in projects:
        if project["id"] == project_id:
            return project
    return None


def filter_projects_by_status(projects: list[dict], status: str) -> list[dict]:
    """根据状态筛选项目列表。"""
    return [project for project in projects if project["status"] == status]
