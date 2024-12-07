import asyncio
async def async_timer(seconds_list):
    for seconds in seconds_list:
        await asyncio.sleep(seconds)
        print(f"Прошло {seconds} секунд!")
async def main():
    await async_timer([1, 2, 3])
if __name__ == "__main__":
    asyncio.run(main())