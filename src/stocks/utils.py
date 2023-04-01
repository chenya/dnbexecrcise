import asyncio
import os
from datetime import date, timedelta

import httpx
from selectolax.parser import HTMLParser, Node

REST_BASE_URL: str = "https://api.polygon.io/v1/open-close"
REST_HEADERS = {"Authorization": f"Bearer {os.getenv('exercise_toekn')}"}
PERFORMANCE_BASE_URL = "https://www.marketwatch.com/investing/stock"


def previuos_day_date(day: date | None = None, days: int = 1) -> str:
    """
    Return the previuos ``days`` isoformat(YYYY-MM-DD) date.
    for ``day.isoformat() == '2023-03-10'`` and ``days == 3``
    the return will be '2023-03-07'
    """
    day_date: date = date.today() - timedelta(days=days)
    if day is not None:
        day_date = day - timedelta(days=days)

    return day_date.isoformat()


async def make_async_get_request(
    url: str, headers: dict | None = None
) -> httpx.Response:
    """
    Perform a simple async http get request using httpx.AsyncClient
    """
    async with httpx.AsyncClient() as client:
        response = await client.get(
            url,
            headers=headers,
        )
        response.raise_for_status()
        return response


async def get_stock_open_close_data(
    stock_symbol: str, day: date | None = None
) -> dict:
    """
    Get the stock open-close data.
    It will run 7 times, each time on the previous day because there is
    days without stock trading.
    """
    retries: int = 1
    num_retries: int = 7
    while retries < num_retries:
        stock_open_close_url: str = "/".join(
            [
                REST_BASE_URL,
                stock_symbol,
                previuos_day_date(day=day, days=retries),
            ]
        )
        try:
            response: httpx.Response = await make_async_get_request(
                stock_open_close_url, headers=REST_HEADERS
            )
            response.raise_for_status()
            return response.json()
        except (httpx.ConnectError, httpx.HTTPStatusError) as e:
            if e.response.json()["status"].lower() == "error":
                raise
            retries += 1
            if retries < num_retries:
                await asyncio.sleep(0.1)
            else:
                raise


def scarping_data(html_text) -> dict[str, str]:
    """
    Scarping the data using css classes in the html tags
    """

    def performance_text_key_value(tr: Node) -> tuple[str, str]:
        k, v = tr.css("td.table__cell")
        return k.text().strip(), v.text().strip()

    div_performance: list[Node] = HTMLParser(html_text).css(
        "div.performance > table > tbody > tr"
    )

    return dict([performance_text_key_value(tr) for tr in div_performance])


async def get_stock_performance_data(stock_symbol: str) -> dict[str, str]:
    """
    Retrieve the stock performance data
    """
    stock_performance_url: str = "/".join([PERFORMANCE_BASE_URL, stock_symbol])

    response: httpx.Response = await make_async_get_request(
        stock_performance_url
    )
    if response.status_code != 200:
        raise httpx.ConnectError(
            f"Could not retrieve {stock_symbol} performance data"
        )
    performance_data: dict[str, str] = scarping_data(response.text)

    return performance_data
