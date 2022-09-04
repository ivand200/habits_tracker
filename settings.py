from typing import Optional

from pydantic import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: Optional[str] = None
    SECRET: Optional[str] = None
    ALGORITHM: Optional[str] = None

    class Config:
        env_file = ".env.dev"
        # orm_mode = True