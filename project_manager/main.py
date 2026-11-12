"""AI 项目管理与任务记录系统 - 主入口"""

from project_manager.models.project import create_project, display_project_info
from project_manager.models.task import create_task, display_task_info


def main():
    print("=" * 40)
    print("  AI 项目管理与任务记录系统")
    print("=" * 40)
    print()

    # 创建几个示例项目
    p1 = create_project("Python 学习计划", "11月系统学习 Python 基础")
    p2 = create_project("个人博客")
    p3 = create_project("CLI 工具开发", "开发一个命令行项目管理工具")

    # 把项目放进列表
    projects = [p1, p2, p3]

    # 显示所有项目
    print(f"共有 {len(projects)} 个项目：\n")
    for project in projects:
        display_project_info(project)
        print()

    print("=" * 40)
    print(" 任务列表")
    print("=" * 40)
    print()

    # 创建几个示例任务
    t1 = create_task(p1["id"], 1, "学习 Python 基础知识")
    t2 = create_task(p1["id"],2,"整理总结笔记","high","done")

    tasks = [t1, t2]

    # 显示所有项目
    print(f"共有 {len(tasks)} 个任务：\n")
    for task in tasks:
        display_task_info(task)
        print()

if __name__ == "__main__":
    main()
