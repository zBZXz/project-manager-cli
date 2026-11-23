"""AI 项目管理与任务记录系统 - 主入口"""

from project_manager.models.project import create_project, display_project_info
from project_manager.models.task import (
    create_task,
    display_task_info,
    update_task_status,
)
from project_manager.services.project_service import (
    filter_projects_by_status,
    get_project_by_id,
)
from project_manager.services.task_service import (
    get_high_priority_tasks,
    get_tasks_by_project_id,
    get_tasks_by_status,
)


def main():
    print("=" * 45)
    print("   AI 项目管理与任务记录系统")
    print("=" * 45)
    print()

    # 1. 创建示例项目
    p1 = create_project("Python 学习计划", "11月系统学习 Python 基础")
    p2 = create_project("个人博客")
    p3 = create_project("CLI 工具开发", "开发一个命令行项目管理工具")
    projects = [p1, p2, p3]

    print(f"【项目列表】共有 {len(projects)} 个项目：\n")
    for project in projects:
        display_project_info(project)
        print()

    # 2. 创建示例任务
    t1 = create_task(p1["id"], 1, "学习 Python 基础知识", priority="medium", status="todo")
    t2 = create_task(p1["id"], 2, "整理总结笔记", priority="high", status="todo")
    t3 = create_task(p2["id"], 3, "部署个人网站", priority="low", status="done")
    tasks = [t1, t2, t3]

    print("=" * 45)
    print(f"【任务列表】共有 {len(tasks)} 个任务：\n")
    for task in tasks:
        display_task_info(task)
        print()

    # 3. 测试服务层查询功能
    print("=" * 45)
    print("【服务层功能测试】")
    print("=" * 45)

    # 3.1 根据 ID 查找项目（正常查找与未找到边界）
    found_p = get_project_by_id(projects, 1)
    print(f"-> 查找 ID=1 的项目: {found_p['name'] if found_p else '未找到'}")

    not_found_p = get_project_by_id(projects, 999)
    print(f"-> 查找 ID=999 的项目: {not_found_p}")

    # 3.2 筛选项目
    active_projects = filter_projects_by_status(projects, "active")
    print(f"-> active 状态的项目数: {len(active_projects)}")

    # 3.3 查找指定项目的所有任务
    p1_tasks = get_tasks_by_project_id(tasks, p1["id"])
    print(f"-> 项目 #{p1['id']} 下的任务数: {len(p1_tasks)}")

    # 3.4 查找紧急未完成任务（high priority）
    urgent_tasks = get_high_priority_tasks(tasks)
    print(f"-> 紧急未完成任务数: {len(urgent_tasks)}")
    for ut in urgent_tasks:
        print(f"   * [紧急] #{ut['task_id']} {ut['title']}")

    print()

    # 4. 测试状态流转与异常防御
    print("=" * 45)
    print("【任务状态流转与异常测试】")
    print("=" * 45)

    print("-> 将任务 #1 状态更新为 done...")
    update_task_status(t1, "done")
    display_task_info(t1)
    print()

    print("-> 尝试传入非法状态 'unknown_status'...")
    try:
        update_task_status(t1, "unknown_status")
    except ValueError as e:
        print(f"-> [成功拦截非法操作] 捕获到预期异常: {e}")


if __name__ == "__main__":
    main()
