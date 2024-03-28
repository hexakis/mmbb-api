import os
from pathlib import Path



class Settings:
    if os.getenv("PROJECT_STATUS") == "PROD":
        PROJECT_NAME: str = os.getenv("PROJECT_NAME")
        PROJECT_VERSION: str = os.getenv("PROJECT_VERSION")
        DATABASE_URL: str = os.getenv("DATABASE_URL")
        NOOB_TOKEN: str = os.getenv("NOOB_TOKEN")
        HASHING_SECRET: str = os.getenv("HASH_SECRET")
    elif os.getenv("PROJECT_STATUS") == "DEV":
        PROJECT_NAME: str = os.getenv("DEV_NAME")
        PROJECT_VERSION: str = os.getenv("DEV_VERSION")
        DATABASE_URL: str = os.getenv("DEV_DATABASE_URL")
        NOOB_TOKEN: str = os.getenv("NOOB_TOKEN")
        HASHING_SECRET: str = os.getenv("HASH_SECRET")


settings = Settings()