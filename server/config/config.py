from enum import Enum

class AppMode(Enum):
    DEVELOPEMENT = "DEVELOPEMENT"
    PRODUCTION = "PRODUCTION"

APP_MODE: AppMode = AppMode.DEVELOPEMENT