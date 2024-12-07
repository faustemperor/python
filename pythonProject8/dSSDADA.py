import asyncio
import random


async def process_task(queue):
    while True:
        task = await queue.get()
        print(f"Обрабатываю: {task}")
        await asyncio.sleep(random.uniform(1, 2))
        queue.task_done()
        if queue.empty():
            break


async def main():
    queue = asyncio.Queue()

    for i in range(1, 6):
        await queue.put(f"Задача {i}")

    await asyncio.gather(process_task(queue), process_task(queue))

    await queue.join()
    print("Все задачи обработаны!")


if __name__ == "__main__":
    asyncio.run(main())