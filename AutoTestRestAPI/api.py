import json
import os
import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder
class PetFriends:
    def __init__(self):
        self.base_url = 'https://petfriends.skillfactory.ru'

    def get_api_key(self, email, password):

        headers = {
            'email': email,
            'password': password
        }
        res = requests.get(self.base_url+'/api/key', headers=headers)
        status = res.status_code
        result = ''
        try:
            result = res.json()
        except:
            result = res.text
        return status, result



    def get_list_of_pets(self, auth_key, filter):
        headers = {'auth_key':auth_key['key']}
        filter = {'filter':filter}

        res = requests.get(self.base_url+'/api/pets', headers=headers, params=filter)

        status = res.status_code
        result = ''
        try:
            result = res.json()
        except:
            result = res.text
        return status, result


    def add_new_pet(self, auth_key: json, name: str, animal_type: str,
                    age: str, pet_photo: str) -> json:
        data = MultipartEncoder(
            fields={
                'name': name,
                'animal_type': animal_type,
                'age': age,
                'pet_photo': (pet_photo, open(pet_photo, 'rb'), 'image/jpeg')
            })
        headers = {'auth_key': auth_key['key'], 'Content-Type': data.content_type}

        res = requests.post(self.base_url + 'api/pets', headers=headers, data=data)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        print(result)
        return status, result


    def add_new_pet_without_photo(self, auth_key: json, name: str, animal_type: str, age: str,) -> json:
        data = MultipartEncoder(
            fields={
                'name': name,
                'animal_type': animal_type,
                'age': age
            })
        headers = {'auth_key': auth_key['key'], 'Content-Type': data.content_type}
        res = requests.post(self.base_url + '/api/create_pet_simple', headers=headers, data=data)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        print(result)
        return status, result


    def add_photo_of_pet(self, auth_key: json, pet_id: str, pet_photo: str) -> json:
        """Добавляет фото питомца с правильной табуляцией"""
        try:
            if not os.path.exists(pet_photo):
                return 404, {"error": f"File {pet_photo} not found"}
            with open(pet_photo, 'rb') as file:
                data = MultipartEncoder(
                    fields={
                        'pet_id': pet_id,
                        'pet_photo': (os.path.basename(pet_photo), file, 'image/jpeg')
                    } )

                headers = {
                    'auth_key': auth_key['key'],
                    'Content-Type': data.content_type
                }

                res = requests.post(
                    self.base_url + f'/api/pets/set_photo/{pet_id}',
                    headers=headers,
                    data=data
                )
                status = res.status_code
                try:
                    result = res.json()
                except ValueError:
                    result = res.text
                return status, result
        except PermissionError:
            return 403, {"error": f"No permission to read file {pet_photo}"}
        except Exception as e:
            return 500, {"error": f"Internal server error: {str(e)}"}
