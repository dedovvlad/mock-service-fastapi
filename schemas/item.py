from typing import Optional
from pydantic import BaseModel


class Item(BaseModel):
    item_id: int
    tag: Optional[str]
