import os

import pytest

from api import PetFriends
from settings import valid_email, valid_password

pf = PetFriends()


def test_add_without_photo():
    """Тест проверяет добавление нового питомца без фотографии"""
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet_without_photo(
        auth_key,
        name='гавс',
        animal_type='собака',
        age='22'
    )
    assert status == 200
    assert result['name'] == 'гавс'
    assert result['pet_photo'] == ""


def test_add_pet_with_empty_fields():
    """Негативный тест на добавление питомца с пустыми полями"""
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet_without_photo(
        auth_key,
        name='',
        animal_type='',
        age=''
    )
    assert status == 200 # здесь == потому что сервис разрешает такие значения



def test_add_pet_with_max_length():
    """Тест проверяет добавление питомца с максимально длинными значениями полей"""
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    long_name='a'* 256
    long_type='a'* 256
    long_age= '19'* 256

    status, result = pf.add_new_pet_without_photo(
        auth_key,
        name=long_name,
        animal_type=long_type,
        age=long_age
    )
    assert status == 200
    assert len(result['name']) == 256


def test_add_nonexistent_photo():
    """Негативный тест на добавление несуществующего фото"""
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    pet_photo = 'images/fu17d.jpg'
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    pet_id = 'dfc898ce-1f75-4170-9c9c-5e2c6b3f77ea'

    status, result = pf.add_photo_of_pet(auth_key, pet_id, pet_photo )
    assert status != 200

def test_add_pet_with_special_symbols():
    """Тест проверяет добавление питомца со специальными символами в полях"""
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet_without_photo(
        auth_key,
        name='!@#$%^?:%;%?;&*()',
        animal_type='Кот*?%?:(',
        age='3.?*%?:5'
    )
    assert status == 200
    assert result['name'] == '!@#$%^?:%;%?;&*()'


def test_add_photo_with_invalid_pet_id():
    """Негативный тест на добавление фото с неверным ID питомца"""
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    pet_photo = 'images/cat1.jpg'
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    pet_id = 'fdgfdgdfdgs23'

    if not os.path.exists(pet_photo):
        pytest.fail(f'File {pet_photo} not found')

    status, result = pf.add_photo_of_pet(auth_key, pet_id, pet_photo)
    assert status != 200


def test_add_photo_to_existing_pet():
    """Тест проверяет добавление фото к существующему питомцу"""
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    pet_photo = 'images/cat1.jpg'
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    pet_id = 'dfc898ce-1f75-4170-9c9c-5e2c6b3f77ea'

    if not os.path.exists(pet_photo):
        pytest.fail(f'File {pet_photo} not found')

    status, result = pf.add_photo_of_pet(auth_key, pet_id, pet_photo)

    assert status == 200
    assert 'pet_photo' in result


def test_add_pet_with_invalid_age_format():
    """Негативный тест проверяет добавление питомца с нечисловым возрастом"""
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet_without_photo(
        auth_key,
        name='Мурзик',
        animal_type='Кот',
        age='два года'
    )
    assert status == 200 # здесь == потому что сервис разрешает такие значения



def test_add_pet_with_whitespace():
    """Тест на добавление питомца с полями, содержащими только пробелы"""
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet_without_photo(
        auth_key,
        name='    ',
        animal_type='    ',
        age='    '
    )
    assert status == 200


def test_add_pet_with_max_age_value():
    """Тест на добавление питомца с максимально возможным возрастом"""
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet_without_photo(
        auth_key,
        name = 'Попи',
        animal_type = 'Черепаха',
        age = '5465474373235'
    )

    assert status == 200
    assert result['age'] == '5465474373235'
