from fastapi import FastAPI

from apps import router
from core.admin import admin
from core.config import settings


class App(FastAPI):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


app = App(
    title=settings.PROJECT_NAME,
    responses=settings.VALIDATION_ERROR_RESPONSE,
)

app.include_router(router)


@app.on_event("startup")
async def startup():
    admin.mount_to(app)


if __name__ == "__main__":
    import uvicorn

    server = uvicorn.Server(
        uvicorn.Config(
            app,
            host=settings.HOST,
            port=settings.PORT,
        )
    )

    server.run()
