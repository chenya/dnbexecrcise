import asyncio

import httpx


async def run_tests():
    stock_symbols = sorted(["AAPL", "AMZN", "FFIV", "JNJ", "NIO"])
    async with httpx.AsyncClient() as client:
        tasks = [
            client.get(f"http://127.0.0.1:8000/stock/{symbol}")
            for symbol in stock_symbols
        ]

        result = await asyncio.gather(*tasks)

    return result


async def main():
    result = await run_tests()
    for r in result:
        print(r.json())
        print("-" * 50)


if __name__ == "__main__":
    import time

    s = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")
