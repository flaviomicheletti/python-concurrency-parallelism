import asyncio

async def say_hello():
    print("Hello")
    await asyncio.sleep(1)  # Pause execution for 1 second
    print("World")

# Run the coroutine using asyncio.run()
asyncio.run(say_hello())

"""
Hello
(after 1 second)
World
"""