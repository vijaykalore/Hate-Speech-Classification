from hate.pipeline.train_pipeline import TrainPipeline
from fastapi import FastAPI, Query
import uvicorn
import sys
from starlette.responses import RedirectResponse
from fastapi.responses import Response, JSONResponse
from pydantic import BaseModel
from typing import Optional
from hate.pipeline.prediction_pipeline import PredictionPipeline
from hate.exception import CustomException
from hate.constants import *


text:str = "What is machine learing?"

app = FastAPI()

@app.get("/", tags=["authentication"])
async def index():
    return RedirectResponse(url="/docs")


@app.get("/health")
async def health():
    return {"status": "ok"}


@app.get("/train")
async def training():
    try:
        train_pipeline = TrainPipeline()

        train_pipeline.run_pipeline()
    return JSONResponse({"status": "ok", "message": "Training successful"})

    except Exception as e:
        return Response(f"Error Occurred! {e}")

class PredictInput(BaseModel):
    text: str


@app.post("/predict")
async def predict_route(body: Optional[PredictInput] = None, text: Optional[str] = Query(default=None)):
    try:
        value = (body.text if body and body.text else text)
        if not value:
            return JSONResponse(status_code=400, content={"status": "error", "message": "Provide 'text' in JSON body or as query param."})

        obj = PredictionPipeline()
        prediction = obj.run_pipeline(value)
        return JSONResponse({"status": "ok", "input": value, "prediction": prediction})
    except Exception as e:
        raise CustomException(e, sys) from e


if __name__=="__main__":
    uvicorn.run(app, host=APP_HOST, port=APP_PORT)

