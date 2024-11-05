from pathlib import Path
import os

from strtobool import strtobool

from dotenv import load_dotenv


ENV_PATH = Path(f'{os.getcwd()}/.env')
load_dotenv(dotenv_path=ENV_PATH, override=True)


def get_env(env_name: str) -> str:
    return os.getenv(env_name)


def get_env_fastapi_config() -> dict:
    config: dict = {
        "app": os.getenv('FASTAPI_APP'),
        "host": os.getenv('FASTAPI_HOST'),
        "port": int(os.getenv('FASTAPI_PORT')),
        "log_level": os.getenv('FASTAPI_LOG_LEVEL'),
        "reload": strtobool(os.getenv('FASTAPI_RELOAD')),
        "workers": int(os.getenv('FASTAPI_WORKERS'))
    }
    return config
