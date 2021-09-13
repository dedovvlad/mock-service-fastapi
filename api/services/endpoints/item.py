from typing import Optional
from fastapi import APIRouter, Response
from fastapi_utils.cbv import cbv
from time import sleep

router = APIRouter()


@cbv(router)
class ItemClass:
    STATUS = 0
    TIMEOUT = 0
    BODY = None

    @router.get("/item/{item_id}")
    async def read_item(
        self,
        response: Response,
        item_id: int,
        tag: Optional[str] = None
    ):
        sleep(self.TIMEOUT)
        if self.STATUS:
            response.status_code = self.STATUS
        if self.BODY is not None:
            return self.BODY
        return {"item_id": item_id, "tag": tag}

    @router.put("/item/config")
    async def update_item(
        self,
        status: Optional[int] = None,
        timeout: Optional[int] = 0,
        body: Optional[dict] = None,
    ):
        ItemClass.STATUS = status
        ItemClass.TIMEOUT = timeout
        ItemClass.BODY = body
        return {
            "data mock changed": "OK",
            "status": self.STATUS,
            "timeout": self.TIMEOUT,
        }
