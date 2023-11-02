from fastapi import FastAPI
from fastapi.responses import ORJSONResponse
from models import employee
from sqlalchemy import create_engine

#wil create table int database
employee.base.metadata.create_all(bind=engine)

app = FastAPI(
    title="FastAPI CRUD",
    description = "Having request methods",
    version= "1.0.0"
)





@app.get("/homepage")
async def homepage():
    try:
        return ORJSONResponse({
            "resp": "This is a test message"
            }, status_code= 200)
    except Exception as err:
        return ORJSONResponse(
            {
                "error": err
            }, 400
        )
