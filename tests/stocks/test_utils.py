import httpx
import pytest
from datetime import date
from ...src.stocks.models import StockPerformance
from ...src.stocks.utils import (
    PERFORMANCE_BASE_URL,
    REST_BASE_URL,
    REST_HEADERS,
    get_stock_open_close_data,
    get_stock_performance_data,
    make_async_get_request,
    scarping_data,
)


def test_scarping_data_expected_result_same_values(html_sample) -> None:
    expected_result: dict[str, str] = {
        "5 Day": "1.82%",
        "1 Month": "8.04%",
        "3 Month": "25.58%",
        "YTD": "25.58%",
        "1 Year": "-6.39%",
    }
    sdata: dict[str, str] = scarping_data(html_sample)
    assert set(expected_result.values()) ^ set(sdata.values()) == set()


def test_scarping_data_expected_result_same_keys(html_sample) -> None:
    expected_result: dict[str, str] = {
        "5 Day": "1.82%",
        "1 Month": "8.04%",
        "3 Month": "25.58%",
        "YTD": "25.58%",
        "1 Year": "-6.39%",
    }
    sdata: dict[str, str] = scarping_data(html_sample)
    assert set(sdata.keys()) ^ set(expected_result.keys()) == set()


@pytest.mark.asyncio
async def test_async_get_request_success():
    url = "https://www.google.com/"
    response: httpx.Response = await make_async_get_request(url)

    assert response.status_code == 200


@pytest.mark.asyncio
async def test_async_get_request_failed():
    url: str = "https://www.google.comcomcomcom/"
    with pytest.raises(httpx.ConnectError):
        response: httpx.Response = await make_async_get_request(url)
        assert response.status_code != 200


@pytest.mark.asyncio
async def test_get_AAPL_stock_open_close_data():
    stock_symbol: str = "AAPL"
    stock_symbol_data: dict = await get_stock_open_close_data(stock_symbol)
    assert stock_symbol_data["symbol"] == stock_symbol


@pytest.mark.asyncio
async def test_get_AAPL_stock_open_close_data_not_trade_day():
    stock_symbol: str = "AAPL"
    non_trade_day: date = date.fromisoformat("2022-12-26")
    stock_symbol_data = await get_stock_open_close_data(
        stock_symbol, non_trade_day
    )
    assert stock_symbol_data["symbol"] == stock_symbol


@pytest.mark.asyncio
async def test_get_not_exists_stock_open_close_data():
    stock_symbol: str = "AAAAAPL"
    with pytest.raises(httpx.HTTPStatusError):
        await get_stock_open_close_data(stock_symbol)


@pytest.mark.asyncio
async def test_get_AAPL_stock_performance_data():
    stock_symbol: str = "AAPL"
    stock_symbol_data: dict = await get_stock_performance_data(stock_symbol)
    StockPerformance(**stock_symbol_data)


@pytest.mark.asyncio
async def test_get_not_exists_stock_performance_data():
    stock_symbol: str = "AAAAAPL"
    with pytest.raises(httpx.HTTPStatusError):
        await get_stock_performance_data(stock_symbol)
