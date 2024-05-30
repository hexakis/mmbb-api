import os
from pathlib import Path



class Settings:
    PROJECT_NAME: str = "mmmb"
    PROJECT_VERSION: str = "1.1"
    DATABASE_URL: str = "postgresql+asyncpg:///admin:bWFyaW5lbW9uZXliYW5raW5nMjAyNCEhIQ==@0.0.0.0:5432"
    NOOB_TOKEN: str = "06cc603c-2da8-45a8-8f43-16b460207a50"
    HASHING_SECRET: str = "0980hbiausgdi7y81jbj2k13bj"


settings = Settings()