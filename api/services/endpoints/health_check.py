from fastapi import APIRouter, Response, status

router = APIRouter()


@router.get("/health_check", status_code=status.HTTP_201_CREATED)
def health_check(response: Response):
    # response.status_code = status.HTTP_200_OK
    return {"service": "OK"}
