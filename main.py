import os
import shutil

from fastapi import FastAPI, Request, Form, Depends, File, UploadFile
from fastapi.templating import Jinja2Templates
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import HTMLResponse, FileResponse
from starlette.staticfiles import StaticFiles

from database import engine, Base
from secret.jwt_code import secret
from scr.car.router import router as car_router
from scr.database.router import router as db_router

templates = Jinja2Templates(directory="templates")

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/", response_class=HTMLResponse)
async def check_code(request: Request, code: str = Form(...)):
    result = "Fuck you and your hack skill"
    status = '400'

    if code == secret:
        result = "You win car"
        status = '200'

    return templates.TemplateResponse("index.html", {"request": request, 'result': result, 'status': status})


@app.post('/upload/images/')
async def upload_images(file: UploadFile = File(...)):
    try:
        file_location = f"static/images/{file.filename}"
        with open(file_location, 'wb+') as file_objects:
            file_objects.write(file.file.read())

        return {'Info: ': FileResponse(str(file)).path, "location": file_location}

    except Exception as e:
        return {"message": e.args}


@app.get('/get/images/{image}/')
async def get_images(images: str):
    try:
        file_location = f"static/images/{images}"
        return FileResponse(file_location, media_type='application/octet-stream')
    except Exception as ex:
        return {"message": ex.args}


@app.get('/views/images/', response_class=HTMLResponse)
async def views_images(request: Request):
    try:
        image_dir = 'static/images/'
        images = os.listdir(image_dir)
        images = [img for img in images if img.endswith(('.png', '.jpg', '.jpeg', '.gif'))]

        return templates.TemplateResponse("gallery.html", {"request": request, 'images': images})
    except Exception as ex:
        return str(ex)


@app.get("/static/{file_path:path}")
async def get_static(file_path: str):
    """
    :param file_path:

        you need to specify the path with images/


    """
    return FileResponse(f"static/{file_path}")


app.include_router(car_router)
app.include_router(db_router)

# uvicorn main:app --reload

# @app.on_event("startup")
# async def on_startup():
#     async with engine.begin() as conn:
#         await conn.run_sync(Base.metadata.create_all)
