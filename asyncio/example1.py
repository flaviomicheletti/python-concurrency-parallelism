import asyncio

async def say_hello():
    print("Hello")
    await asyncio.sleep(1)  # Pause execution for 1 second
    print("World")

# Create an event loop
loop = asyncio.get_event_loop()

# Run the coroutine
loop.run_until_complete(say_hello())

# Close the event loop
loop.close()

"""
 DeprecationWarning: There is no current event loop
  loop = asyncio.get_event_loop()
Hello
World
"""