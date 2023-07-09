import asyncio
import random

async def producer(queue):
    while True:
        item = random.randint(1, 10)
        await queue.put(item)
        print(f"Produced: {item}")
        await asyncio.sleep(random.uniform(0.5, 2.0))

async def consumer(queue):
    while True:
        item = await queue.get()
        print(f"Consumed: {item}")
        await asyncio.sleep(random.uniform(0.5, 2.0))
        queue.task_done()

async def main():
    queue = asyncio.Queue()
    producer_task = asyncio.create_task(producer(queue))
    consumer_task = asyncio.create_task(consumer(queue))
    await asyncio.gather(producer_task, consumer_task)

# Run the main coroutine using asyncio.run()
asyncio.run(main())

"""
Produced: 5
Consumed: 5
Produced: 5
Consumed: 5
Produced: 9
Consumed: 9
Produced: 10
Consumed: 10
Produced: 5
Consumed: 5
Produced: 4
Consumed: 4
...
"""