from fastapi import APIRouter
from api.services.endpoints import health_check, item

router = APIRouter()

router.include_router(router=health_check.router, tags=["Checkout mock service"])
router.include_router(router=item.router, tags=["Item"])
