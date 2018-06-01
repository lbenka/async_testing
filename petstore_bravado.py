from bravado.client import SwaggerClient


def get_pet(client):
    return client.pet.getPetById(petId=2).result(timeout=4)


def get_10():
    client = SwaggerClient.from_url('http://petstore.swagger.io/v2/swagger.json')
    for _ in range(10):
        r = get_pet(client)
        print(r)


if __name__ == '__main__':
    get_10()
