from fastapi import APIRouter
from scr.database.models import DBConnect

router = APIRouter(
    tags=['DB']
)


@router.get('/info')
async def info_db():
    return "Короче, я всё уже расписал нужно подключиться к db и найти его уже"


@router.post('/connect/db/')
async def connect(check_code: str):
    connect_to_db = DBConnect()
    if check_code == ';LK12%!@$SA#@$DJ124@$#!@*&@_!*@$:lxkn?<??@><$@':
        return connect_to_db
    return 'You need to read fast'
