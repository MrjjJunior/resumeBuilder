from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="static/templates")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request)-> HTMLResponse:
    return templates.TemplateResponse(request=request, name="index.html")
