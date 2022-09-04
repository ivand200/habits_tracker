from fastapi import FastAPI

from routers.users import router as router_users


app = FastAPI()


@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Habits tracker"}


app.include_router(
    router_users,
    prefix="/user",
    tags=["users"]
)