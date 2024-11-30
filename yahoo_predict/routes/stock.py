from fastapi import APIRouter
from pydantic import BaseModel
from ..controllers.stock_controller import StockController

router = APIRouter()


class ImportRequest(BaseModel):
    stock_symbol: str


@router.post("/import/stock")
async def import_stock_data(request: ImportRequest):
    stock_symbol = request.stock_symbol
    controller = StockController()
    return await controller.import_data(stock_symbol)
