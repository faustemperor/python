import asyncio

async def add_customers(queue):
    for i in range(1, 11):
        customer = f"Покупатель {i}"
        await queue.put(customer)
        print(f"Добавлен в очередь: {customer}")
        await asyncio.sleep(1)

async def serve_customers(queue):
    while not queue.empty() or not customers_served == 10:
        if not queue.empty():
            customer = await queue.get()
            print(f"Обслуживаю: {customer}")
            await asyncio.sleep(2)
            queue.task_done()

async def main():
    global customers_served
    customers_served = 0
    queue = asyncio.Queue()
    await asyncio.gather(
        add_customers(queue),
        serve_customers(queue)
    )

asyncio.run(main())