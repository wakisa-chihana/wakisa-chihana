from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware  # Import CORS middleware
from datetime import datetime, timedelta

app = FastAPI()

# Add CORS middleware to allow requests from any origin
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins (you can restrict this to specific domains if needed)
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)

# Centralized countdown time (6:30 PM CAT)
def get_end_time():
    now = datetime.utcnow()
    end_time = datetime.utcnow().replace(hour=16, minute=30, second=0, microsecond=0)  # 16:30 UTC = 6:30 PM CAT
    if now > end_time:
        end_time += timedelta(days=1)  # If past 6:30 PM, set it for the next day
    return end_time

end_time = get_end_time()

@app.get("/getEndTime")
async def get_end_time_api():
    # Return the end time as a timestamp in milliseconds
    return {"endTime": int(end_time.timestamp() * 1000)}
