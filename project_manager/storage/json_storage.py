# JSON 文件存储
import json
import os

def save_data(file_path: str, data: list | dict) -> None:
    """持久化保存数据到指定 JSON 文件。"""
    # 1. 确保父目录存在（exist_ok=True,避免存在时报错）
    dir_name = os.path.dirname(file_path)
    if dir_name:
        os.makedirs(dir_name, exist_ok=True)

    # 2. 写入 JSON 数据
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def load_data(file_path: str) -> list | dict:
    """从指定 JSON 文件加载数据，如文件不存在或损坏则返回空列表。"""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"文件 {file_path} 不存在，返回空数据")
        return []
    except json.JSONDecodeError:
        print(f"文件 {file_path} 格式损坏或为空，返回空数据")
        return []