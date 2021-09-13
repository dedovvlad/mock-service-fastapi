from api.services.routes import router
from fastapi import FastAPI
import uvicorn
from core.config import PREFIX


def get_application():
    application = FastAPI()
    application.include_router(
        router=router,
        prefix=PREFIX,
    )
    return application


fastapi = get_application()

if __name__ == "__main__":
    uvicorn.run(app=fastapi, host="0.0.0.0", port=5000)
