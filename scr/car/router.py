from fastapi import APIRouter
from starlette.responses import FileResponse

router = APIRouter(
    tags=['Car']
)


@router.get('/download/file')
async def download_file(file_name: str):
    """
    param
        file_name: your file name

    :return:
        file
    """
    if file_name != ';LK12%!@$SA#@$DJ124@$#!@*&@_!*@$:lxkn?<??@><$@':
        file_location = 'secret/messages.txt'
        return FileResponse(file_location, media_type='application/octet-stream', filename='messages_from_you.txt')
    return {"messages": 'я на 5050'}


@router.get('/decode/login/password')
async def decode(login: str, password: str):
    """
    As you asked, Karl. I made a function to decrypt your password and login. I hope you won't forget this too...
    """
    if login == '!@$?<?><!@><M!@#!' and password == '%@)(*{!@!1!&%':
        file_location = 'secret/check.txt'
        return FileResponse(file_location, media_type='application/octet-stream', filename='fast.txt')
    return {'messages': 'NO',
            'status': 400}


@router.get('/login/download/')
async def download_if_login(login: str, password: str):
    pass
