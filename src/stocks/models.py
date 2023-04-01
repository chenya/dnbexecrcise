from datetime import date

from pydantic import BaseModel


class StockPerformance(BaseModel):
    five_days: str
    one_month: str
    three_months: str
    year_to_date: str
    one_year: str

    class Config:
        allow_population_by_field_name = True
        fields = {
            "five_days": "5 Day",
            "one_month": "1 Month",
            "three_months": "3 Month",
            "year_to_date": "YTD",
            "one_year": "1 Year",
        }


class Stock(BaseModel):
    afterHours: float
    close: float
    from_: date
    high: float
    low: float
    open: float
    preMarket: float
    status: str
    symbol: str
    volume: float
    performance: StockPerformance
    amount: int

    class Config:
        allow_population_by_field_name = True
        fields = {"from_": "from"}


class Amount(BaseModel):
    amount: int


class PostRequestMessage(BaseModel):
    message: str
