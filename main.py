from fastapi import FastAPI, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from random import randint

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

def getRandomValue( from_: int = 0, to_: int = 100 ):
    return randint( from_, to_ )

@app.get("/", response_class=HTMLResponse)
def randomValue(request: Request, value = Depends(getRandomValue)):
    return templates.TemplateResponse(
        request=request, name="index.html", context={"value": value}
    )