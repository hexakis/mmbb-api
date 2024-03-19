import os
from pathlib import Path



class Settings:
    PROJECT_NAME: str = os.getenv("PROJECT_NAME")
    PROJECT_VERSION: str = os.getenv("PROJECT_VERSION")
    DATABASE_URL: str = os.getenv("DATABASE_URL")
    NOOB_TOKEN: str = os.getenv("NOOB_TOKEN")


settings = Settings()