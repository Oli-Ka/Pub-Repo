import requests
import json

# Тип запроса GET
res_get_pets = requests.get(f'https://petstore.swagger.io/v2/pet/findByStatus',
    params={'status': 'available'}, headers={'accept': 'application/json'})
print(res_get_pets.status_code)
print(res_get_pets.json())

# Тип запроса POST
info = {
  "id": 0,
  "category": {
    "id": 0,
    "name": "snake"
  },
  "name": "Umberto",
  "photoUrls": [
    "no foto"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
}
res_post_add_pet = requests.post(f"https://petstore.swagger.io/v2/pet",
    headers={'accept': 'application/json', 'Content-Type': 'application/json'},
    data=json.dumps(info, ensure_ascii=False))
print(res_post_add_pet.status_code)
print(res_post_add_pet.json())

# Тип запроса DELETE
petId = 9223372036854246542
res_del_del_pet = requests.delete(f'https://petstore.swagger.io/v2/pet/{petId}')
print(res_del_del_pet.status_code)
print(res_del_del_pet.json())

# Тип запроса PUT
new_info = {
  "id": 9223372036854619078,
  "category": {
    "id": 0,
    "name": "orange snake"
  },
  "name": "Umbertinio",
  "photoUrls": [
    "no foto"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
}
res_put_rename_pet = requests.put(f"https://petstore.swagger.io/v2/pet",
    headers={'accept': 'application/json', 'Content-Type': 'application/json'},
    data=json.dumps(new_info, ensure_ascii=False))
print(res_put_rename_pet.status_code)
print(res_put_rename_pet.json())