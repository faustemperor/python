import asyncio
import random

async def produce_data(queue, producer_id):
    for _ in range(10):
        data = random.randint(1, 10)
        await queue.put(data)
        print(f"Производитель {producer_id} добавил данные: {data}")
        await asyncio.sleep(1)

async def process_data(queue, result_queue, worker_id):
    while True:
        data = await queue.get()
        result = data * 2
        print(f"Работник {worker_id} обработал данные: {data} -> {result}")
        await asyncio.sleep(1.5)
        await result_queue.put(result)
        queue.task_done()

async def save_results(result_queue):
    saved_data = []
    while True:
        while not result_queue.empty():
            result = await result_queue.get()
            saved_data.append(result)
            result_queue.task_done()
        if saved_data:
            print(f"Сохранено: {saved_data}")
        await asyncio.sleep(2)

async def main():
    task_queue = asyncio.Queue()
    result_queue = asyncio.Queue()

    producers = [asyncio.create_task(produce_data(task_queue, i)) for i in range(1, 4)]
    workers = [asyncio.create_task(process_data(task_queue, result_queue, i)) for i in range(1, 3)]
    saver = asyncio.create_task(save_results(result_queue))

    await asyncio.gather(*producers)
    await task_queue.join()

    for worker in workers:
        worker.cancel()
    await asyncio.gather(*workers, return_exceptions=True)

    await result_queue.join()
    saver.cancel()
    await asyncio.gather(saver, return_exceptions=True)

asyncio.run(main())