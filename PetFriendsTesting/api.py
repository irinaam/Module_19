import json
import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder

class PetFriends:
    def __init__(self):
        self.base_url = "https://petfriends1.herokuapp.com/"
# 1
    def get_api_key(self, email: str, passwd: str) -> json:

        headers = {
            'email': email,
            'password': passwd
        }
        res = requests.get(self.base_url+'api/key', headers=headers)
        status = res.status_code
        result = ""

        try:
            result = res.json()

        except json.decoder.JSONDecodeError:
            result = res.text

        return status, result
# 2
    def get_list_of_pets(self, auth_key, filter):

        headers = {'auth_key': auth_key['key']}

        filter = {'filter': filter}


        res = requests.get(self.base_url+'api/pets', headers=headers, params=filter)

        status = res.status_code
        result = ""

        try:
            result = res.json()

        except json.decoder.JSONDecodeError:
            result = res.text

        return status, result
# 3
    def add_new_pet(self, auth_key: json, name: str, animal_type: str, age: str, pet_photo: str) -> json:

        data = MultipartEncoder(
            fields={
                'name': name,
                'animal_type': animal_type,
                'age': age,
                'pet_photo': (pet_photo, open(pet_photo, 'rb'), 'image/jpeg')
            })
        headers = {'auth_key': auth_key['key'], 'Content-Type': data.content_type}

        res = requests.post(self.base_url+'api/pets', headers=headers, data=data)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:

            result = res.text

        print(result)

        return status, result

# 4
    def delete_pet(self, auth_key: json, pet_id: str) -> json:
        headers = {'auth_key': auth_key['key']}
        res = requests.delete(self.base_url+'api/pets/' + pet_id, headers=headers)
        status = res.status_code
        result = ""
        try:
            result = res.json()

        except json.decoder.JSONDecodeError:

            result = res.text

        return status, result

# 5
    def update_pet_info(self,  auth_key: json, pet_id: str, name: str, animal_type: str, age: int) -> json:

        headers = {'auth_key': auth_key['key']}
        data = {
            'name': name,
            'age': age,
            'animal_type': animal_type
        }
        res = requests.put(self.base_url + 'api/pets/' + pet_id, headers=headers, data=data)
        status = res.status_code
        result = ""
        try:
            result = res.json()

        except json.decoder.JSONDecodeError:

            result = res.text

        return status, result

# 6
    def add_photo_of_pet(self, auth_key: json, pet_id: str, pet_photo: str) -> json:

        data = MultipartEncoder(
            fields={
                'pet_photo': (pet_photo, open(pet_photo, 'rb'), 'image/jpeg')
            })
        headers = {'auth_key': auth_key['key'], 'Content-Type': data.content_type}
        res = requests.post(self.base_url + 'api/pets/set_photo/' + pet_id, headers=headers, data=data)

        status = res.status_code
        result = ''

        try:
            result = res.json()

        except json.decoder.JSONDecodeError:

            result = res.text

        return status, result

# 7
    def delete_pets(self, auth_key: json, pet_id: str) -> json:
        headers = {'auth_key': auth_key['key'], 'pet_id': pet_id}
        res = requests.delete(self.base_url + 'api/pets/' + pet_id, headers=headers)
        status = res.status_code
        result = ""

        try:
            result = res.json()

        except json.decoder.JSONDecodeError:

            result = res.text

        return status, result

# 8
    def add_new_pet_without_photo(self, auth_key: json, name: str, animal_type: str, age: str) -> json:
        headers = {'auth_key': auth_key['key']}
        data = {
            'name': name,
            'age': age,
            'animal_type': animal_type
        }

        res = requests.post(self.base_url + 'api/create_pet_simple', headers=headers, data=data)
        status = res.status_code
        result = ""

        try:
            result = res.json()

        except json.decoder.JSONDecodeError:

            result = res.text

        return status, result
# 9
    def get_api_key_invalid_request(self, email: str, password: str) -> json:
        headers = {'email': email, 'password': password}
        res = requests.put(self.base_url + 'api/key', headers=headers)
        status = res.status_code
        result = ''

        try:
            result = res.json()
        except json.decoder.JSONDecodeError:

            result = res.text

        return status, result