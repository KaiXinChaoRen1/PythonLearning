import logging
import logging.config
import os
from pathlib import Path
from typing import Optional, Union

# 确保当前目录在Python路径中
import sys
sys.path.insert(0, str(Path(__file__).parent))

from common import env_bool


def setup_logging(project_root: Optional[Union[str, Path]] = None) -> None:
    level = os.getenv("ASAT_LOG_LEVEL", "INFO").strip().upper() or "INFO"
    console_enabled = env_bool("ASAT_LOG_CONSOLE", True)
    max_bytes = int(os.getenv("ASAT_LOG_MAX_BYTES", "10485760").strip() or "10485760")
    backup_count = int(os.getenv("ASAT_LOG_BACKUP_COUNT", "5").strip() or "5")
    sql_level = os.getenv("ASAT_SQL_LOG_LEVEL", "WARNING").strip().upper() or "WARNING"

    base = Path(project_root) if project_root is not None else Path.cwd()
    log_dir = Path(os.getenv("ASAT_LOG_DIR", str(base / "logs"))).expanduser().resolve()
    log_dir.mkdir(parents=True, exist_ok=True)
    log_file = os.getenv("ASAT_LOG_FILE", str(log_dir / "asat.log"))

    handlers = {
        "file": {
            "class": "logging.handlers.RotatingFileHandler",
            "level": level,
            "formatter": "standard",
            "filename": log_file,
            "maxBytes": max_bytes,
            "backupCount": backup_count,
            "encoding": "utf-8",
        }
    }

    root_handlers = ["file"]
    if console_enabled:
        handlers["console"] = {
            "class": "logging.StreamHandler",
            "level": level,
            "formatter": "standard",
            "stream": "ext://sys.stdout",
        }
        root_handlers.append("console")

    logging.config.dictConfig(
        {
            "version": 1,
            "disable_existing_loggers": False,
            "formatters": {
                "standard": {
                    "format": "%(asctime)s %(levelname)s %(name)s [%(threadName)s] %(message)s"
                }
            },
            "handlers": handlers,
            "root": {"level": level, "handlers": root_handlers},
            "loggers": {
                "sqlalchemy.engine": {"level": sql_level, "propagate": True},
                "sqlalchemy.pool": {"level": sql_level, "propagate": True},
            },
        }
    )
    logging.captureWarnings(True)
