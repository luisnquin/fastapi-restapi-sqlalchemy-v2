from fastapi.routing import APIRouter

router = APIRouter()

@router.get("/", tags=["GET Functions"])
async def getNothing():
    return
