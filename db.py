from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase
from settings import Settings

settings = Settings()

motor_client = AsyncIOMotorClient(f"{settings.DATABASE_URL}")
database = motor_client["test_habits"]

def get_database() -> AsyncIOMotorDatabase:
    return database