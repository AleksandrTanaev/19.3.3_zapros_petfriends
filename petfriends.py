import requests
import json

status = 'available'

res_get = requests.get(f'https://petstore.swagger.io/v2/pet/findByStatus?status={status}', headers={'assept':'application/json'})


print(res_get.status_code)
print(res_get.text)
print(res_get.json())


dat = {
      "id": 0,
      "category": {
        "id": 0,
        "name": "string"
      },
      "name": "doggie",
      "photoUrls": [
        "string"
      ],
      "tags": [
        {
          "id": 0,
          "name": "string"
        }
      ],
      "status": "available"
    }

res_post = requests.post('https://petstore.swagger.io/v2/pet', headers={'accept': 'application/json', 'Content-Type': 'application/json'}, data=dat)


print('....')
print(res_post.status_code)
print(res_post.text)


#DELETE
res_d = requests.delete(f'https://petstore.swagger.io/v2/pet/9223372036854572002', headers = {'accept': 'application/json'})
print(res_d.status_code, 'запрос DELETE')
print(res_d.json())

#PUT

data = {
  "id": 9223372036854765198,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "doggie",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
}
res_put = requests.put(f'https://petstore.swagger.io/v2/pet', headers = {'accept': 'application/json', 'Content-Type': 'application/json'}, data = json.dumps(data))
print(res_put.status_code, 'запрос PUT')
print(res_put.json())