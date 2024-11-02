from fastapi import APIRouter, HTTPException
from starlette.responses import FileResponse

from scr.car.models import Decode
from scr.database.models import DBConnect

router = APIRouter(
    tags=['DB']
)


@router.get('/info')
async def info_db():
    return "Короче, я всё уже расписал нужно подключиться к db и найти его уже"


@router.post('/connect/db/')
async def connect(connect_to: DBConnect):
    return connect_to
