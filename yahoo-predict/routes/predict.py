from fastapi import APIRouter
from pydantic import BaseModel
from ..controllers.predict_controller import PredictController

router = APIRouter()


class PredictRequest(BaseModel):
    stock_symbol: str


@router.post("/predict")
def predict(request: PredictRequest):
    controller = PredictController()
    return controller.predict(request)
