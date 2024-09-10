from fastapi import FastAPI
import subprocess
import uvicorn

app = FastAPI()

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

# Example route for a simple health check
@app.get("/")
def read_root():
    return {"status": "Server is running"}

if __name__ == "__main__":
    # Run the FastAPI app with specified host and port
    uvicorn.run(app, host="0.0.0.0", port=8000)
