import logging
import os
from pathlib import Path
from logging_config import setup_logging

# 打印当前工作目录
print(f"当前工作目录: {Path.cwd()}")

# 配置日志
setup_logging()

# 获取logger
logger = logging.getLogger(__name__)

# 测试不同级别的日志
logger.debug("这是一条DEBUG级别的日志")
logger.info("这是一条INFO级别的日志")
logger.warning("这是一条WARNING级别的日志")
logger.error("这是一条ERROR级别的日志")
logger.critical("这是一条CRITICAL级别的日志")

# 测试异常日志
try:
    1 / 0
except Exception as e:
    logger.exception("发生了异常")

# 检查日志文件是否存在
log_dir = Path.cwd() / "logs"
log_file = log_dir / "asat.log"
print(f"日志目录是否存在: {log_dir.exists()}")
print(f"日志文件是否存在: {log_file.exists()}")

if log_file.exists():
    print(f"日志文件大小: {log_file.stat().st_size} 字节")
    print("\n日志文件内容:")
    with open(log_file, 'r', encoding='utf-8') as f:
        print(f.read())
else:
    print("日志文件不存在，请检查配置")