import asyncio
async def progress_tracker(n):
    for i in range(1, n + 1):
        await asyncio.sleep(0.5)
        print(f"Выполнено {i * (100 // n)}%...")
    print("Выполнено 100%!")
async def main():
    await progress_tracker(10)
if __name__ == "__main__":
    asyncio.run(main())