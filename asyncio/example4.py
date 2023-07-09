import asyncio

async def say_hello(name):
    print("Hello, " + name)
    await asyncio.sleep(1)  # Simulate an asynchronous operation
    print("Goodbye, " + name)

async def main():
    task1 = asyncio.create_task(say_hello("Alice"))
    task2 = asyncio.create_task(say_hello("Bob"))

    await asyncio.gather(task1, task2)

asyncio.run(main())

"""
Hello, Alice!
Hello, Bob!
(after 1 second)
Goodbye, Alice!
Goodbye, Bob!
"""