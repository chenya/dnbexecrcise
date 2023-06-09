from fastapi import APIRouter, HTTPException, status
from stocks.models import Amount, PostRequestMessage, Stock, StockPerformance
from stocks.utils import get_stock_open_close_data, get_stock_performance_data

stocks_router: APIRouter = APIRouter(tags=["Stocks"])
stocks_record: dict[str, int] = {}


@stocks_router.get("/{stock_symbol}")
async def retrieve_stock_data(stock_symbol: str) -> Stock:
    try:
        stock_open_close_data: dict = await get_stock_open_close_data(
            stock_symbol
        )

    except:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Stock {stock_symbol} open close  not found",
        )
    try:
        stock_performance_data: dict = await get_stock_performance_data(
            stock_symbol
        )
    except:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Stock {stock_symbol} performance data not found",
        )

    amount: int = 0
    if stocks_record.get(stock_symbol):
        amount = stocks_record[stock_symbol]

    stock: Stock = Stock(
        **stock_open_close_data,
        performance=StockPerformance(**stock_performance_data),
        amount=amount,
    )

    return stock


@stocks_router.post(
    "/{stock_symbol}", status_code=201, response_model=PostRequestMessage
)
async def update_amount(
    stock_symbol: str, amount_data: Amount
) -> PostRequestMessage:
    if stocks_record.get(stock_symbol):
        stocks_record[stock_symbol] += amount_data.amount
    else:
        stocks_record[stock_symbol] = amount_data.amount

    return PostRequestMessage(
        message=f"{amount_data.amount} units of stock {stock_symbol} were added to your stock record"
    )
