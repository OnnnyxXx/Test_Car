from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import HTMLResponse
from starlette.staticfiles import StaticFiles

from secret.jwt_code import secret
from scr.car.router import router as car_router
from scr.database.router import router as db_router
from scr.gellery.router import router as gallery_router

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



app.include_router(car_router)
app.include_router(gallery_router)
app.include_router(db_router)

# uvicorn main:app --reload

# @app.on_event("startup")
# async def on_startup():
#     async with engine.begin() as conn:
#         await conn.run_sync(Base.metadata.create_all)
