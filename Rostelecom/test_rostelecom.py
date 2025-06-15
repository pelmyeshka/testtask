from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Инициализация драйвера для Firefox
driver = webdriver.Firefox()


def test():
    driver.get("https://lk.rt.ru/")
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID,'standard_auth_btn')))
    element.click()
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'kc-register')))
    element.click()



# Тест RTT-001: Проверка авторизации по неверным данным email и пароль
def test_RTT_001():
    driver.get("https://lk.rt.ru/")
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'standard_auth_btn')))
    element.click()
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 't-btn-tab-mail')))
    element.click()
    email_addr = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div/input[@type='text']")))
    email_addr.click()
    email_addr.send_keys("test@mail.ru")
    password = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div/input[@name='password']")))
    password.click()
    password.send_keys("123456")
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'kc-login')))
    element.click()


# Тест RTT-002: Проверка сброса пароля с некорректной капчей
def test_RTT_002():
    driver.get("https://lk.rt.ru/")
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'standard_auth_btn')))
    element.click()
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'forgot_password')))
    element.click()
    number = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'username')))
    number.click()
    number.send_keys("+79000000000")
    captcha_test = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'captcha')))
    captcha_test.click()
    captcha_test.send_keys("fgbbjrty")
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'reset')))
    element.click()

# Тест RTT-003: Проверка авторизации по несуществующему номеру телефона
def test_RTT_003():
    driver.get("https://lk.rt.ru/")
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'standard_auth_btn')))
    element.click()
    number = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'username')))
    number.click()
    number.send_keys("89000000000")
    password = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "password")))
    password.click()
    password.send_keys("123456789")
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'kc-login')))
    element.click()

# Тест RTT-004: Проверка формы регистрации с некорректными данными "Имя" и "Фамилия" граничные значения 31 символ
def test_RTT_004():
    driver.get("https://lk.rt.ru/")
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'standard_auth_btn')))
    element.click()
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'kc-register')))
    element.click()

    firstname_element = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//div/input[@name='firstName']"))
    )

    driver.execute_script("arguments[0].scrollIntoView();", firstname_element)
    firstname_element.click()
    firstname_element.send_keys("а" * 31)
    lastname_element = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//div/input[@name='lastName']"))
    )
    driver.execute_script("arguments[0].scrollIntoView();", lastname_element)
    lastname_element.click()
    lastname_element.send_keys("а" * 31)


# Тест RTT-005: Проверка формы регистрации с некорректными данными "Имя" и "Фамилия" символ #
def test_RTT_005():
    driver.get("https://lk.rt.ru/")
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'standard_auth_btn')))
    element.click()
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'kc-register')))
    element.click()

    firstname_element = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//div/input[@name='firstName']"))
    )

    driver.execute_script("arguments[0].scrollIntoView();", firstname_element)
    firstname_element.click()
    firstname_element.send_keys("#")
    lastname_element = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//div/input[@name='lastName']"))
    )
    driver.execute_script("arguments[0].scrollIntoView();", lastname_element)
    lastname_element.click()
    lastname_element.send_keys("#")
    element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'input.rt-input__input.rt-select__input.rt-input__input--rounded.rt-input__input--orange')))
    element.click()

# Тест RTT-006: Проверка регистрации с некорректным форматом имени и фамилии (цифры)
def test_RTT_006():
    driver.get("https://lk.rt.ru/")
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'standard_auth_btn')))
    element.click()
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'kc-register')))
    element.click()

    firstname_element = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//div/input[@name='firstName']")))
    firstname_element.click()
    firstname_element.send_keys("12345")
    lastname_element = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//div/input[@name='lastName']")))
    lastname_element.click()
    lastname_element.send_keys("54321")

    input_element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'input.rt-input__input.rt-select__input.rt-input__input--rounded'))
    )
    input_element.click()

    input_element.send_keys("Москва г")

    driver.execute_script("""
                    var options = document.querySelectorAll('.rt-select__list-item');
                    for (var i = 0; i < options.length; i++) {
                        if (options[i].textContent.includes('Москва г')) {
                            options[i].click();
                            break;
                        }
                    }
                """)

    email_add = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'address')))
    email_add.click()
    email_add.send_keys("test@mail.ru")
    passw = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'password')))
    passw.click()
    passw.send_keys("Test1234_")
    last_passw = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'password-confirm')))
    last_passw.click()
    last_passw.send_keys("Test1234_")
    reg = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//button[@name='register']")))
    reg.click()


# Тест RTT-007: Проверка написания неправильного формата email при регистрации
def test_RTT_007():
    driver.get("https://lk.rt.ru/")
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'standard_auth_btn')))
    element.click()
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'kc-register')))
    element.click()

    firstname_element = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//div/input[@name='firstName']")))

    firstname_element.click()
    firstname_element.send_keys("Миша")
    lastname_element = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//div/input[@name='lastName']")))

    lastname_element.click()
    lastname_element.send_keys("Крылов")

    input_element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'input.rt-input__input.rt-select__input.rt-input__input--rounded'))
    )
    input_element.click()

    input_element.send_keys("Москва г")

    driver.execute_script("""
        var options = document.querySelectorAll('.rt-select__list-item');
        for (var i = 0; i < options.length; i++) {
            if (options[i].textContent.includes('Москва г')) {
                options[i].click();
                break;
            }
        }
    """)

    email_add = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'address')))
    email_add.click()
    email_add.send_keys("notmail#mail.ru")
    passw = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'password')))
    passw.click()
    passw.send_keys("Test1234")
    last_passw = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'password-confirm')))
    last_passw.click()
    last_passw.send_keys("Test1234")
    reg = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//button[@name='register']")))
    reg.click()


# Тест RTT-008: Проверка регистрации с пустыми полями
def test_RTT_008():
    driver.get("https://lk.rt.ru/")
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'standard_auth_btn')))
    element.click()
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'kc-register')))
    element.click()
    reg = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//button[@name='register']")))
    reg.click()

# Тест RTT-009: Регистрация с уже существующим email
def test_RTT_009():
    driver.get("https://lk.rt.ru/")
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'standard_auth_btn')))
    element.click()
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'kc-register')))
    element.click()

    firstname_element = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//div/input[@name='firstName']")))

    firstname_element.click()
    firstname_element.send_keys("Миша-Ладов")
    lastname_element = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//div/input[@name='lastName']")))

    lastname_element.click()
    lastname_element.send_keys("Крылов")

    input_element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'input.rt-input__input.rt-select__input.rt-input__input--rounded'))
    )
    input_element.click()

    input_element.send_keys("Москва г")

    driver.execute_script("""
                var options = document.querySelectorAll('.rt-select__list-item');
                for (var i = 0; i < options.length; i++) {
                    if (options[i].textContent.includes('Москва г')) {
                        options[i].click();
                        break;
                    }
                }
            """)

    email_add = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'address')))
    email_add.click()
    email_add.send_keys("test@mail.ru")
    passw = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'password')))
    passw.click()
    passw.send_keys("Test1234_")
    last_passw = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'password-confirm')))
    last_passw.click()
    last_passw.send_keys("Test1234_")
    reg = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//button[@name='register']")))
    reg.click()

# Тест RTT-010: Регистрация с именем, содержащим дефис
def test_RTT_010():
    driver.get("https://lk.rt.ru/")
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'standard_auth_btn')))
    element.click()
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'kc-register')))
    element.click()

    firstname_element = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//div/input[@name='firstName']")))

    firstname_element.click()
    firstname_element.send_keys("Миша-Ладов")
    lastname_element = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//div/input[@name='lastName']")))

    lastname_element.click()
    lastname_element.send_keys("Крылов")

    input_element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'input.rt-input__input.rt-select__input.rt-input__input--rounded'))
    )
    input_element.click()

    input_element.send_keys("Москва г")

    driver.execute_script("""
            var options = document.querySelectorAll('.rt-select__list-item');
            for (var i = 0; i < options.length; i++) {
                if (options[i].textContent.includes('Москва г')) {
                    options[i].click();
                    break;
                }
            }
        """)

    email_add = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'address')))
    email_add.click()
    email_add.send_keys("test321@mail.ru")
    passw = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'password')))
    passw.click()
    passw.send_keys("Test1234_")
    last_passw = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'password-confirm')))
    last_passw.click()
    last_passw.send_keys("Test1234_")
    reg = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//button[@name='register']")))
    reg.click()

# Тест RTT-011: Некорректный код для подтверждения email
def test_RTT_011():
    driver.get("https://lk.rt.ru/")
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'standard_auth_btn')))
    element.click()
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'kc-register')))
    element.click()

    firstname_element = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//div/input[@name='firstName']")))

    firstname_element.click()
    firstname_element.send_keys("Артем")
    lastname_element = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//div/input[@name='lastName']")))

    lastname_element.click()
    lastname_element.send_keys("Иванов")

    input_element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'input.rt-input__input.rt-select__input.rt-input__input--rounded'))
    )
    input_element.click()

    input_element.send_keys("Москва г")

    driver.execute_script("""
                var options = document.querySelectorAll('.rt-select__list-item');
                for (var i = 0; i < options.length; i++) {
                    if (options[i].textContent.includes('Москва г')) {
                        options[i].click();
                        break;
                    }
                }
            """)

    email_add = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'address')))
    email_add.click()
    email_add.send_keys("test321@mail.ru")
    passw = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'password')))
    passw.click()
    passw.send_keys("Test1234_")
    last_passw = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'password-confirm')))
    last_passw.click()
    last_passw.send_keys("Test1234_")
    reg = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//button[@name='register']")))
    reg.click()



# Тест RTT-012: Регистрация с пробелами в начале/конце имени и фамилии
def test_RTT_012():
    driver.get("https://lk.rt.ru/")
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'standard_auth_btn')))
    element.click()
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'kc-register')))
    element.click()

    firstname_element = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//div/input[@name='firstName']")))

    firstname_element.click()
    firstname_element.send_keys("     Артем     ")
    lastname_element = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//div/input[@name='lastName']")))

    lastname_element.click()
    lastname_element.send_keys("     Иванов     ")

    input_element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'input.rt-input__input.rt-select__input.rt-input__input--rounded'))
    )
    input_element.click()

    input_element.send_keys("Москва г")

    driver.execute_script("""
                    var options = document.querySelectorAll('.rt-select__list-item');
                    for (var i = 0; i < options.length; i++) {
                        if (options[i].textContent.includes('Москва г')) {
                            options[i].click();
                            break;
                        }
                    }
                """)

    email_add = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'address')))
    email_add.click()
    email_add.send_keys("test321@mail.ru")
    passw = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'password')))
    passw.click()
    passw.send_keys("Test1234_")
    last_passw = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'password-confirm')))
    last_passw.click()
    last_passw.send_keys("Test1234_")
    reg = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//button[@name='register']")))
    reg.click()

# Тест RTT-013: Регистрация с email в верхнем регистре
def test_RTT_013():
    driver.get("https://lk.rt.ru/")
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'standard_auth_btn')))
    element.click()
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'kc-register')))
    element.click()

    firstname_element = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//div/input[@name='firstName']")))

    firstname_element.click()
    firstname_element.send_keys("Артем")
    lastname_element = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//div/input[@name='lastName']")))

    lastname_element.click()
    lastname_element.send_keys("Иванов")

    input_element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'input.rt-input__input.rt-select__input.rt-input__input--rounded'))
    )
    input_element.click()

    input_element.send_keys("Москва г")

    driver.execute_script("""
                    var options = document.querySelectorAll('.rt-select__list-item');
                    for (var i = 0; i < options.length; i++) {
                        if (options[i].textContent.includes('Москва г')) {
                            options[i].click();
                            break;
                        }
                    }
                """)

    email_add = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'address')))
    email_add.click()
    email_add.send_keys("TEST321@MAIL.RU")
    passw = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'password')))
    passw.click()
    passw.send_keys("Test1234_")
    last_passw = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'password-confirm')))
    last_passw.click()
    last_passw.send_keys("Test1234_")
    reg = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//button[@name='register']")))
    reg.click()

# Тест RTT-014: Регистрация с паролем, содержащим спецсимволы
def test_RTT_014():
    driver.get("https://lk.rt.ru/")
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'standard_auth_btn')))
    element.click()
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'kc-register')))
    element.click()

    firstname_element = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//div/input[@name='firstName']")))

    firstname_element.click()
    firstname_element.send_keys("Артем")
    lastname_element = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//div/input[@name='lastName']")))

    lastname_element.click()
    lastname_element.send_keys("Иванов")

    input_element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'input.rt-input__input.rt-select__input.rt-input__input--rounded'))
    )
    input_element.click()

    input_element.send_keys("Москва г")

    driver.execute_script("""
                    var options = document.querySelectorAll('.rt-select__list-item');
                    for (var i = 0; i < options.length; i++) {
                        if (options[i].textContent.includes('Москва г')) {
                            options[i].click();
                            break;
                        }
                    }
                """)

    email_add = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'address')))
    email_add.click()
    email_add.send_keys("test321@mail.ru")
    passw = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'password')))
    passw.click()
    passw.send_keys("Test@#$1234_")
    last_passw = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'password-confirm')))
    last_passw.click()
    last_passw.send_keys("Test@#$1234_")
    reg = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//button[@name='register']")))
    reg.click()

# Тест RTT-015: Регистрация с пробелом в пароле
def test_RTT_015():
    driver.get("https://lk.rt.ru/")
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'standard_auth_btn')))
    element.click()
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'kc-register')))
    element.click()

    firstname_element = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//div/input[@name='firstName']")))

    firstname_element.click()
    firstname_element.send_keys("Артем")
    lastname_element = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//div/input[@name='lastName']")))

    lastname_element.click()
    lastname_element.send_keys("Иванов")

    input_element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'input.rt-input__input.rt-select__input.rt-input__input--rounded'))
    )
    input_element.click()

    input_element.send_keys("Москва г")

    driver.execute_script("""
                        var options = document.querySelectorAll('.rt-select__list-item');
                        for (var i = 0; i < options.length; i++) {
                            if (options[i].textContent.includes('Москва г')) {
                                options[i].click();
                                break;
                            }
                        }
                    """)

    email_add = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'address')))
    email_add.click()
    email_add.send_keys("test321@mail.ru")
    passw = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'password')))
    passw.click()
    passw.send_keys("Tes t@#$1234_")
    last_passw = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'password-confirm')))
    last_passw.click()
    last_passw.send_keys("Tes t@#$1234_")
    reg = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//button[@name='register']")))
    reg.click()

#Тест RTT-016: Проверка регистрации с паролем, содержащим только цифры
def test_RTT_016():
    driver.get("https://lk.rt.ru/")
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'standard_auth_btn')))
    element.click()
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'kc-register')))
    element.click()

    firstname_element = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//div/input[@name='firstName']")))

    firstname_element.click()
    firstname_element.send_keys("Артем")
    lastname_element = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//div/input[@name='lastName']")))

    lastname_element.click()
    lastname_element.send_keys("Иванов")

    input_element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'input.rt-input__input.rt-select__input.rt-input__input--rounded'))
    )
    input_element.click()

    input_element.send_keys("Москва г")

    driver.execute_script("""
                            var options = document.querySelectorAll('.rt-select__list-item');
                            for (var i = 0; i < options.length; i++) {
                                if (options[i].textContent.includes('Москва г')) {
                                    options[i].click();
                                    break;
                                }
                            }
                        """)

    email_add = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'address')))
    email_add.click()
    email_add.send_keys("test321@mail.ru")
    passw = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'password')))
    passw.click()
    passw.send_keys("123456")
    last_passw = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'password-confirm')))
    last_passw.click()
    last_passw.send_keys("123456")
    reg = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//button[@name='register']")))
    reg.click()


#Тест RTT-017: Проверка регистрации с несовпадающими полями пароля
def test_RTT_017():
    driver.get("https://lk.rt.ru/")
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'standard_auth_btn')))
    element.click()
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'kc-register')))
    element.click()

    firstname_element = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//div/input[@name='firstName']")))

    firstname_element.click()
    firstname_element.send_keys("Артем")
    lastname_element = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//div/input[@name='lastName']")))

    lastname_element.click()
    lastname_element.send_keys("Иванов")

    input_element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'input.rt-input__input.rt-select__input.rt-input__input--rounded'))
    )
    input_element.click()

    input_element.send_keys("Москва г")

    driver.execute_script("""
                                var options = document.querySelectorAll('.rt-select__list-item');
                                for (var i = 0; i < options.length; i++) {
                                    if (options[i].textContent.includes('Москва г')) {
                                        options[i].click();
                                        break;
                                    }
                                }
                            """)

    email_add = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'address')))
    email_add.click()
    email_add.send_keys("test321@mail.ru")
    passw = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'password')))
    passw.click()
    passw.send_keys("Test@#$4321_")
    last_passw = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'password-confirm')))
    last_passw.click()
    last_passw.send_keys("Test@#$1234_")
    reg = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//button[@name='register']")))
    reg.click()

# Тест RTT-018: Проверка регистрации с использованием некорректного формата email (с двумя @)
def test_RTT_018():
    driver.get("https://lk.rt.ru/")
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'standard_auth_btn')))
    element.click()
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'kc-register')))
    element.click()

    firstname_element = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//div/input[@name='firstName']")))

    firstname_element.click()
    firstname_element.send_keys("Артем")
    lastname_element = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//div/input[@name='lastName']")))

    lastname_element.click()
    lastname_element.send_keys("Иванов")

    input_element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'input.rt-input__input.rt-select__input.rt-input__input--rounded'))
    )
    input_element.click()

    input_element.send_keys("Москва г")

    driver.execute_script("""
                                    var options = document.querySelectorAll('.rt-select__list-item');
                                    for (var i = 0; i < options.length; i++) {
                                        if (options[i].textContent.includes('Москва г')) {
                                            options[i].click();
                                            break;
                                        }
                                    }
                                """)

    email_add = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'address')))
    email_add.click()
    email_add.send_keys("test321@@mail.ru")
    passw = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'password')))
    passw.click()
    passw.send_keys("Test@#$1234_")
    last_passw = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'password-confirm')))
    last_passw.click()
    last_passw.send_keys("Test@#$1234_")
    reg = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//button[@name='register']")))
    reg.click()

# Тест RTT-019: Проверка регистрации с именем и фамилией на английском языке
def test_RTT_019():
    driver.get("https://lk.rt.ru/")
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'standard_auth_btn')))
    element.click()
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'kc-register')))
    element.click()

    firstname_element = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//div/input[@name='firstName']")))

    firstname_element.click()
    firstname_element.send_keys("Artem")
    lastname_element = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//div/input[@name='lastName']")))

    lastname_element.click()
    lastname_element.send_keys("Ivanov")

    input_element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'input.rt-input__input.rt-select__input.rt-input__input--rounded'))
    )
    input_element.click()

    input_element.send_keys("Москва г")

    driver.execute_script("""
                                        var options = document.querySelectorAll('.rt-select__list-item');
                                        for (var i = 0; i < options.length; i++) {
                                            if (options[i].textContent.includes('Москва г')) {
                                                options[i].click();
                                                break;
                                            }
                                        }
                                    """)

    email_add = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'address')))
    email_add.click()
    email_add.send_keys("test321@mail.ru")
    passw = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'password')))
    passw.click()
    passw.send_keys("Test@#$1234_")
    last_passw = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'password-confirm')))
    last_passw.click()
    last_passw.send_keys("Test@#$1234_")
    reg = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//button[@name='register']")))
    reg.click()

# Тест RTT-020: Проверка регистрации с использованием некорректного формата email (с точкой в начале)
def test_RTT_020():
    driver.get("https://lk.rt.ru/")
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'standard_auth_btn')))
    element.click()
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'kc-register')))
    element.click()

    firstname_element = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//div/input[@name='firstName']")))

    firstname_element.click()
    firstname_element.send_keys("Маша")
    lastname_element = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//div/input[@name='lastName']")))

    lastname_element.click()
    lastname_element.send_keys("Иванова")

    input_element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'input.rt-input__input.rt-select__input.rt-input__input--rounded'))
    )
    input_element.click()

    input_element.send_keys("Москва г")

    driver.execute_script("""
                                            var options = document.querySelectorAll('.rt-select__list-item');
                                            for (var i = 0; i < options.length; i++) {
                                                if (options[i].textContent.includes('Москва г')) {
                                                    options[i].click();
                                                    break;
                                                }
                                            }
                                        """)

    email_add = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'address')))
    email_add.click()
    email_add.send_keys(".test321@mail.ru")
    passw = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'password')))
    passw.click()
    passw.send_keys("Test@#$1234_")
    last_passw = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'password-confirm')))
    last_passw.click()
    last_passw.send_keys("Test@#$1234_")
    reg = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//button[@name='register']")))
    reg.click()

# Тест RTT-021: Проверка регистрации с использованием дефисов и лишними цифрами в номере телефона
def test_RTT_021():
    driver.get("https://lk.rt.ru/")
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'standard_auth_btn')))
    element.click()
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'kc-register')))
    element.click()

    firstname_element = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//div/input[@name='firstName']")))

    firstname_element.click()
    firstname_element.send_keys("Маша")
    lastname_element = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//div/input[@name='lastName']")))

    lastname_element.click()
    lastname_element.send_keys("Иванова")

    input_element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'input.rt-input__input.rt-select__input.rt-input__input--rounded'))
    )
    input_element.click()

    input_element.send_keys("Москва г")

    driver.execute_script("""
                                            var options = document.querySelectorAll('.rt-select__list-item');
                                            for (var i = 0; i < options.length; i++) {
                                                if (options[i].textContent.includes('Москва г')) {
                                                    options[i].click();
                                                    break;
                                                }
                                            }
                                        """)

    email_add = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'address')))
    email_add.click()
    email_add.send_keys("7-900-111-22-3333")
    passw = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'password')))
    passw.click()
    passw.send_keys("Test@#$1234_")
    last_passw = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'password-confirm')))
    last_passw.click()
    last_passw.send_keys("Test@#$1234_")
    reg = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//button[@name='register']")))
    reg.click()