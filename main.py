from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse

app = FastAPI()
app.mount("/", StaticFiles(directory="public", html = True), name="static")

@app.get("/test", response_class=HTMLResponse)
async def read_root():
    return """
    <html>
        <body>
            <h1>되는거냐?!</h1>
        </body>
    </html>
    """
