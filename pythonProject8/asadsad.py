import asyncio
async def fetch_data_1():
    await asyncio.sleep(2)
    return "Данные 1"
async def fetch_data_2():
    await asyncio.sleep(3)
    return "Данные 2"
async def fetch_data_3():
    await asyncio.sleep(1)
    return "Данные 3"
async def fetch_all():
    results = await asyncio.gather(fetch_data_1(), fetch_data_2(), fetch_data_3())
    print(f"Результаты: {results}")
async def main():
    await fetch_all()
if __name__ == "__main__":
    asyncio.run(main())