from fastapi import APIRouter

from app.services.stock_service import get_all_stocks


router = APIRouter(
    prefix="/stocks",
    tags=["stocks"],
)


@router.get("/spot")
def stock_spot():

    stocks = get_all_stocks()

    return {
        "count": len(stocks),
        "data": stocks,
    }
