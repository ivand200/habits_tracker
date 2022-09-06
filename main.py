from fastapi import FastAPI
import uvicorn

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


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
    # uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)