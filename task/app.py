import pytz


from fastapi import FastAPI , APIRouter 
from datetime import datetime


app = FastAPI()

router = APIRouter()

@router.get("/api")
async def endpoint(slack_name :str , track:str):
    
    daytime = datetime.now()
    
    return {"slack" : slack_name,
             "utc_time" : daytime.astimezone(tz = pytz.UTC).strftime('%Y-%m-%dT%H:%M:%SZ'),
            "current_day" : daytime.strftime("%A"),
            "track": track,
            "github_file_url": "https://github.com/tephlonee/hngx/blob/main/task/app.py",
             "github_repo_url": "https://github.com/tephlonee/hngx",
             "status_code" : 200
        }

app.include_router(router)