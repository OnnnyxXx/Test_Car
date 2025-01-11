import os

from fastapi import APIRouter, Request, File, UploadFile, HTTPException
from starlette.responses import FileResponse, HTMLResponse
from starlette.templating import Jinja2Templates

router = APIRouter(
    tags=["Gallery"]
)
templates = Jinja2Templates(directory="templates")


@router.post('/upload/images/')
async def upload_images(file: UploadFile = File(...)):
    try:
        file_location = f"static/images/{file.filename}"
        os.makedirs(os.path.dirname(file_location), exist_ok=True)

        with open(file_location, 'wb+') as file_objects:
            file_objects.write(await file.read())

        return {'Info: ': FileResponse(str(file)).path, "location": file_location}

    except Exception as e:
        return {"message": e.args}


@router.get('/get/images/{image}/')
async def get_images(images: str):
    try:
        file_location = f"static/images/{images}"
        return FileResponse(file_location, media_type='application/octet-stream')
    except Exception as ex:
        return {"message": ex.args}


@router.delete('/delete/images/{images}')
async def delete_images(images: str):
    """
    :param images:

        deletes existing photos
    """
    file_location = f"static/images/{images}"

    try:
        if not os.path.exists(file_location):
            raise HTTPException(status_code=404, detail="File not found")

        os.remove(file_location)
        return {"message": "File deleted successfully"}

    except Exception as ex:
        raise HTTPException(status_code=500, detail=str(ex))


@router.get('/views/images/', response_class=HTMLResponse)
async def views_images(request: Request):
    try:
        image_dir = 'static/images/'
        images = os.listdir(image_dir)
        images = [img for img in images if img.endswith(('.png', '.jpg', '.jpeg', '.gif'))]

        return templates.TemplateResponse("gallery.html", {"request": request, 'images': images})
    except Exception as ex:
        return str(ex)


@router.get("/static/{file_path:path}")
async def get_static(file_path: str):
    """
    :param file_path:

        you need to specify the path with images/


    """
    return FileResponse(f"static/{file_path}")
