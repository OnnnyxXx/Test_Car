from fastapi import FastAPI, Request, Form, Depends
from fastapi.templating import Jinja2Templates
from starlette.responses import HTMLResponse

from secret.jwt_code import secret
from scr.car.router import router as car_router

templates = Jinja2Templates(directory="templates")

app = FastAPI()


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
# uvicorn main:app --reload
