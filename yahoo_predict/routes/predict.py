from fastapi import APIRouter
from pydantic import BaseModel
from ..controllers.predict_controller import PredictController

router = APIRouter()


class PredictRequest(BaseModel):
    stock_symbol: str


@router.post("/predict")
def predict():
    try:
        controller = PredictController()
        return controller.predict()
    except Exception as e:
        print(e)
        return {"error": str(e)}
