from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import subprocess
import uvicorn
from starlette.templating import Jinja2Templates
from starlette.requests import Request

app = FastAPI()

# Setup template directory
templates = Jinja2Templates(directory="templates")

# Serve static files (optional, if you have CSS or JS files)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Start the first script as a subprocess
@app.on_event("startup")
async def start_main():
    global process1
    process1 = subprocess.Popen(['python', 'main.py'])

# Start the second script as a subprocess
@app.on_event("startup")
async def start_bot():
    global process2
    process2 = subprocess.Popen(['python', 'bot.py'])

# Stop both scripts when the FastAPI server shuts down
@app.on_event("shutdown")
async def shutdown_event():
    process1.terminate()
    process2.terminate()

# Serve custom HTML page as the index page
@app.get("/", response_class=HTMLResponse)
async def read_index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

if __name__ == "__main__":
    # Run the FastAPI app with specified host and port
    uvicorn.run(app, host="0.0.0.0", port=8000)
