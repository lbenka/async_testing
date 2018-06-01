import asyncio
import aiohttp

async def get_pet():
    async with aiohttp.ClientSession() as session:
        response = await session.get('http://petstore.swagger.io/v2/pet/5')
        data = await response.text()
    print(data)
    return data


async def main():
    await asyncio.gather(*[get_pet() for _ in range(100)])

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
