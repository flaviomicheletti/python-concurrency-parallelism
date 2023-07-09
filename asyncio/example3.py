import asyncio
import aiohttp
import json
from pprint import pprint

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()

async def main():
    async with aiohttp.ClientSession() as session:
        urls = [
            "https://api.chucknorris.io/jokes/random",
            "https://api.chucknorris.io/jokes/categories",
            "https://api.chucknorris.io/jokes/random?category=food"
        ]
        tasks = []
        for url in urls:
            task = asyncio.create_task(fetch(session, url))
            tasks.append(task)

        results = await asyncio.gather(*tasks)
        for url, result in zip(urls, results):
            print(f"Response from {url}:")
            pprint(json.loads(result))
            print("")

# Run the main coroutine using asyncio.run()
asyncio.run(main())
