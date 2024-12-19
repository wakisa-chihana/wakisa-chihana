from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from datetime import datetime, timedelta
import time

app = FastAPI()

# Mount the static folder for serving HTML, CSS, and JS
app.mount("/static", StaticFiles(directory="static"), name="static")

# Centralized countdown time (6:30 PM CAT)
def get_end_time():
    now = datetime.utcnow()
    end_time = datetime.utcnow().replace(hour=16, minute=30, second=0, microsecond=0)  # 16:30 UTC = 6:30 PM CAT
    if now > end_time:
        end_time += timedelta(days=1)  # If past 6:30 PM, set it for the next day
    return end_time

end_time = get_end_time()

@app.get("/")
async def read_index():
    return HTMLResponse(open("static/index.html").read())

@app.get("/getEndTime")
async def get_end_time_api():
    return {"endTime": int(end_time.timestamp() * 1000)}  # Send the end time as timestamp in milliseconds

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
