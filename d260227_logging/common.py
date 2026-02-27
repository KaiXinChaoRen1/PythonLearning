import os

def env_bool(key: str, default: bool = False) -> bool:
    """获取环境变量并转换为布尔值"""
    value = os.getenv(key)
    if value is None:
        return default
    value = value.strip().lower()
    return value in ('true', '1', 'yes', 'y', 'on')