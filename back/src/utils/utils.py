from datetime import datetime
from pathlib import Path
import logging
import time
import sys
import os

from strtobool import strtobool

from dotenv import load_dotenv

FORMAT: str = '%(asctime)s  - %(levelname)s - %(message)s'
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


def process_timer(process_func, *args, **kwargs):
    start_time = time.time()  # Record the start time
    process_func(*args, **kwargs)  # Run the specified process
    end_time = time.time()  # Record the end time

    # Calculate the duration
    duration_seconds = int(end_time - start_time)
    hours, remainder = divmod(duration_seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    # Return the formatted duration
    return f"{hours:02}:{minutes:02}:{seconds:02}"


def set_current_directory() -> str:
    """Get current directory of current .py execution

    Returns:
        str: The path
    """

    directory: str = ''
    
    # determine if application is a script file or frozen exe
    if getattr(sys, 'frozen', False):
        # Running as a PyInstaller bundle
        application_path = os.path.dirname(sys.executable)
        directory = os.path.abspath(os.path.join(application_path))
    elif __file__:
        # Running as a standard Python script
        application_path = os.path.dirname(__file__)
        directory = os.path.abspath(os.path.join(application_path, '..'))

    # set current directory
    os.chdir(directory)

    return directory


# Create log folder
try: 
    os.mkdir(set_current_directory() + '/log/')
except:
    pass


# Logging config/call
logging.basicConfig(filename=set_current_directory() + '/log/LOG_' + datetime.now().strftime("%Y%m") + '.log', 
                    filemode='a', 
                    format=FORMAT,
                    level='INFO',
                    encoding='utf-8')


add_log = logging.getLogger(__name__)
