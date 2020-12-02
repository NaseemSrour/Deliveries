from datetime import datetime
import logging
import os
import sys

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
    print("Creat logging dir")
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
    LOGFILE = f"{LOGGING_DIR_ABS}/{os.path.basename(__file__)}.log"
else: 
    LOGFILE = f"{LOGGING_DIR_ABS}/{os.path.basename(__file__)}.{datetime.now().strftime('%Y%m%dT%H%M%S')}.log"

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
        'file': {
            'class': 'logging.FileHandler',
            'formatter': 'default',
            'level': 'DEBUG',
            'filename': LOGFILE,
            'mode': 'w',
        },
    },
    'loggers': { 
        '': {  # root logger
            'handlers': ['default', 'file'],
            'level': 'WARNING',
            'propagate': False
        },
        'my.packg': { 
            'handlers': ['default'],
            'level': 'INFO',
            'propagate': False
        },
        '__main__': {  # if __name__ == '__main__'
            'handlers': ['default'],
            'level': 'DEBUG',
            'propagate': False
        },
    } 
}