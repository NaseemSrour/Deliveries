from datetime import datetime
import logging
import os
import sys
from typing import Any

from .config import APP_MODE, AppMode

############## LOGGING #################
""" The following config is based on a couple of examples from the internet:
 https://gist.github.com/gongzhitaao/0072e4df3533d282b5b3928447df7195 - credit to @gongzhitaao

 https://stackoverflow.com/questions/7507825/where-is-a-complete-example-of-logging-config-dictconfig
"""

LOGGING_DIR = "logs"
LOGGING_DIR_ABS = os.path.abspath(LOGGING_DIR)

# create directory for logs if it does not exist
if not os.path.isdir(LOGGING_DIR_ABS):
    print("Create logging dir")
    try: 
        os.mkdir(LOGGING_DIR_ABS)
    except Exception as err: 
        raise ValueError(f"Failed to create logging directory at {LOGGING_DIR_ABS}")


# Set up main log file
if (APP_MODE == AppMode.DEVELOPEMENT):
    # remove old logs 
    for f in os.listdir(LOGGING_DIR_ABS):
        try: 
            os.remove(os.path.join(LOGGING_DIR_ABS, f))
        except Exception as err:
            logging.warn("Failed to remove old log files...")
            logging.error(err)


def get_logfile_name(postfix: str) -> str: 
    if (APP_MODE == AppMode.DEVELOPEMENT):
        return f"{LOGGING_DIR_ABS}/log_{postfix}.log"
    else: 
        return f"{LOGGING_DIR_ABS}/log_{postfix}.{datetime.now().strftime('%Y%m%dT%H%M%S')}.log"


MODULES = ["resources", "database", "controllers", "models", "utils", "config"]
def get_module_file_handlers() -> dict[str, Any]:
    file_handlers = {}
    for module in MODULES:
        file_handlers[f'{module}_file'] = {
                'class': 'logging.FileHandler',
                'formatter': 'default',
                'level': 'DEBUG',
                'filename': get_logfile_name(module),
                'mode': 'w',
            }
    return file_handlers

def get_module_loggers() -> dict[str, Any]:
    loggers = {}
    for module in MODULES:
        loggers[module] = { 
            'handlers': ['default', f'{module}_file'],
            'level': 'INFO',
            'propagate': True
        }
    return loggers


DEFAULT_LOGGING = { 
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'default': {
            'format': logging.BASIC_FORMAT
        },
        'simpler': { 
            'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
        },
    },
    'handlers': { 
        'default': { 
            'level': 'DEBUG',
            'formatter': 'default',
            'class': 'logging.StreamHandler',
            'stream': 'ext://sys.stdout',  # Default is stderr
        },
        'root_file': {
            'class': 'logging.FileHandler',
            'formatter': 'default',
            'level': 'DEBUG',
            'filename': get_logfile_name("root"),
            'mode': 'w',
        },
        'main_file': {
            'class': 'logging.FileHandler',
            'formatter': 'default',
            'level': 'DEBUG',
            'filename': get_logfile_name("main"),
            'mode': 'w',
        },
        **get_module_file_handlers()
    },
    'loggers': { 
        '': {  # root logger
            'handlers': ['root_file'],
            'level': 'DEBUG',
            'propagate': False
        },
        '__main__': {  # if __name__ == '__main__'
            'handlers': ['default', 'main_file'],
            'level': 'DEBUG',
            'propagate': True
        },
        **get_module_loggers()
    } 
}