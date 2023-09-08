import pytz


from fastapi import FastAPI , APIRouter 
from datetime import datetime


app = FastAPI()

router = APIRouter()

@router.get("/api")
async def endpoint(slack_name :str , track:str):
    
    daytime = datetime.now()
    
    return {"slack" : slack_name,
            "current_day" : daytime.strftime("%A"),
            "utc_time" : daytime.astimezone(tz = pytz.UTC),
            "track": track,
            "github_file_url": "https://github.com/tephlonee/hngx/blob/main/app.py",
             "github_repo_url": "https://github.com/tephlonee/hngx",
             "status_code" : 200
        }

app.include_router(router)