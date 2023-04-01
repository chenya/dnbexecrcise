import httpx
import pytest

from dnbexecrcise.src.stocks.models import Stock, StockPerformance


@pytest.fixture(scope="module")
async def mock_stock() -> Stock:
    open_close: dict = {
        "afterHours": 162.44,
        "close": 162.36,
        "from": "2023-03-30",
        "high": 162.47,
        "low": 161.271,
        "open": 161.53,
        "preMarket": 161.15,
        "status": "OK",
        "symbol": "AAPL",
        "volume": 49210289.0,
    }
    performance: dict[str, str] = {
        "5 Day": "2.45%",
        "1 Month": "8.70%",
        "3 Month": "26.35%",
        "YTD": "26.35%",
        "1 Year": "-5.82%",
    }

    amount: int = 0
    return Stock(
        **open_close,
        performance=StockPerformance(**performance),
        amount=amount,
    )


@pytest.mark.asyncio
async def test_retrieve_stock_data(
    async_client: httpx.AsyncClient, mock_stock: Stock
) -> None:
    url = f"/stock/{mock_stock.symbol}"
    response = await async_client.get(url)

    assert response.status_code == 200
    assert response.json()["symbol"] == f"{mock_stock.symbol}"


@pytest.mark.asyncio
async def test_update_amount(
    async_client: httpx.AsyncClient, mock_stock: Stock
) -> None:
    url = f"/stock/{mock_stock.symbol}"
    payload = {"amount": 10}
    response = await async_client.post(url, json=payload)

    assert response.status_code == 201
    assert (
        response.json()["message"]
        == f"{payload['amount']} units of stock {mock_stock.symbol} were added to your stock record"
    )
