import asyncio

from aiobravado.client import SwaggerClient


class Petstore(object):

    @classmethod
    async def create(cls):
        self = Petstore()
        self.client = await SwaggerClient.from_url('http://petstore.swagger.io/v2/swagger.json')
        return self

    async def get_pet(self, num):
        pet = await self.client.pet.getPetById(petId=5).result(timeout=30)
        print(f"request number {num}, {pet}")
        return pet


async def main():
    petstore = await Petstore.create()
    await asyncio.gather(*[petstore.get_pet(i) for i in range(20)])


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
