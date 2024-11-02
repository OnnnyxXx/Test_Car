from fastapi import APIRouter, HTTPException
from starlette.responses import FileResponse

from scr.car.models import Decode

router = APIRouter(
    tags=['Files']
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


@router.post('/decode/login/password')
async def decode(user: Decode):
    """
    As you asked, Karl. I made a function to decrypt your password and login. I hope you won't forget this too...
    """
    if user.login == '!@$?<?><!@><M!@#!' and user.password == '%@)(*{!@!1!&%':
        file_location = 'secret/check.txt'
        return FileResponse(file_location, media_type='application/octet-stream', filename='fast.txt')
    if user.login == 'Karl' and user.email == 'jwt.decode@gmai.com':
        return 'Нужно это в jwt: Karl Mitnik'
    return {'messages': 'NO',
            'status': 400}


@router.post('/login/download/')
async def download_if_login(login: str, password: str):
    """
    :param login:
        your login -> login

    :param password:
         your password -> password

    :return:
        jwt.io
    """
    if login == 'login' and password == 'password':
        file_location = 'secret/jwt_postgres.txt'
        return FileResponse(file_location, media_type='application/octet-stream', filename='jwt.txt')
    else:
        raise HTTPException(status_code=401, detail="Иди нахуй!")
