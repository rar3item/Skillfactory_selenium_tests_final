from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

driver = webdriver.Chrome('/Usr/local/bin/chromedriver.exe')
driver.implicitly_wait(10)

@pytest.fixture(autouse=True)
def testing():
   driver.get('https://b2c.passport.rt.ru')

def test_registration_with_email_valid_data():
   driver.find_element(By.XPATH, '(//a[@class="rt-link rt-link--orange"])[2]').click()
   assert WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'register')))
   driver.find_element(By.NAME, 'firstName').send_keys('Имя')
   driver.find_element(By.NAME, 'lastName').send_keys('Фамилия')
   driver.find_element(By.ID, 'address').send_keys('test@test.com')
   driver.find_element(By.NAME, 'password').send_keys('abcdefG1!')
   driver.find_element(By.NAME, 'password-confirm').send_keys('abcdefG1!')
   driver.find_element(By.XPATH, '//button[@type="submit"]').click()
   assert WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.sdi-container--medium')))

def test_registration_with_phone_valid_data():
   driver.find_element(By.XPATH, '(//a[@class="rt-link rt-link--orange"])[2]').click()
   assert WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'register')))
   driver.find_element(By.NAME, 'firstName').send_keys('Имя')
   driver.find_element(By.NAME, 'lastName').send_keys('Фамилия')
   driver.find_element(By.ID, 'address').send_keys('+79500000000')
   driver.find_element(By.NAME, 'password').send_keys('abcdefG1!')
   driver.find_element(By.NAME, 'password-confirm').send_keys('abcdefG1!')
   driver.find_element(By.XPATH, '//button[@type="submit"]').click()
   assert WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.sdi-container--medium')))

def test_autorization_with_valid_email():
   driver.find_element(By.ID, 'username').send_keys('email')
   driver.find_element(By.ID, 'password').send_keys('password')
   driver.find_element(By.ID, 'kc-login').submit()
   assert WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'h3.card-title')))
   assert driver.find_element(By.CSS_SELECTOR, 'h3.card-title').text[0:14] == 'Учетные данные'

def test_autorization_with_valid_phone():
   driver.find_element(By.ID, 'username').send_keys('+9500000000')
   driver.find_element(By.ID, 'password').send_keys('password')
   driver.find_element(By.ID, 'kc-login').submit()
   assert WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'h3.card-title')))
   assert driver.find_element(By.CSS_SELECTOR, 'h3.card-title').text[0:14] == 'Учетные данные'

def test_autorization_with_valid_login():
    driver.find_element(By.ID, 'username').send_keys('login')
    driver.find_element(By.ID, 'password').send_keys('password')
    driver.find_element(By.ID, 'kc-login').submit()
    assert WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'h3.card-title')))
    assert driver.find_element(By.CSS_SELECTOR, 'h3.card-title').text[0:14] == 'Учетные данные'

def test_registration_with_empty_data():
   driver.find_element(By.XPATH, '(//a[@class="rt-link rt-link--orange"])[2]').click()
   assert WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'register')))
   driver.find_element(By.XPATH, '//button[@type="submit"]').click()
   assert WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.rt-input-container--error')))

def test_registration_with_different_password_and_check_password():
   driver.find_element(By.XPATH, '(//a[@class="rt-link rt-link--orange"])[2]').click()
   assert WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'register')))
   driver.find_element(By.NAME, 'firstName').send_keys('Антон')
   driver.find_element(By.NAME, 'lastName').send_keys('Антонов')
   driver.find_element(By.ID, 'address').send_keys('test@test.com')
   driver.find_element(By.NAME, 'password').send_keys('abcdeFG1!')
   driver.find_element(By.NAME, 'password-confirm').send_keys('abdceFG1*')
   driver.find_element(By.XPATH, '//button[@type="submit"]').click()
   assert WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//span[text()="Пароли не совпадают"]')))

def test_registration_with_latin_name_and_email_format_error():
   driver.find_element(By.XPATH, '(//a[@class="rt-link rt-link--orange"])[2]').click()
   assert WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'register')))
   driver.find_element(By.NAME, 'firstName').send_keys('Anton')
   driver.find_element(By.NAME, 'lastName').send_keys('Antonov')
   driver.find_element(By.ID, 'address').send_keys('testtest.com')
   driver.find_element(By.NAME, 'password').send_keys('abcdeFG1!')
   driver.find_element(By.NAME, 'password-confirm').send_keys('abcdeFG1!')
   driver.find_element(By.XPATH, '//button[@type="submit"]').click()
   assert WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '(//span[@class="rt-input-container__meta rt-input-container__meta--error"])[1]')))
   assert WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '(//span[@class="rt-input-container__meta rt-input-container__meta--error"])[2]')))
   assert WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '(//span[@class="rt-input-container__meta rt-input-container__meta--error"])[3]')))

def test_registration_with_num_name_and_phone_format_error():
   driver.find_element(By.XPATH, '(//a[@class="rt-link rt-link--orange"])[2]').click()
   assert WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'register')))
   driver.find_element(By.NAME, 'firstName').send_keys('0000000')
   driver.find_element(By.NAME, 'lastName').send_keys('000000000')
   driver.find_element(By.ID, 'address').send_keys('+7950abcdefg')
   driver.find_element(By.NAME, 'password').send_keys('abcdeFG1!')
   driver.find_element(By.NAME, 'password-confirm').send_keys('abcdeFG1!')
   driver.find_element(By.XPATH, '//button[@type="submit"]').click()
   assert WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '(//span[@class="rt-input-container__meta rt-input-container__meta--error"])[1]')))
   assert WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '(//span[@class="rt-input-container__meta rt-input-container__meta--error"])[2]')))
   assert WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '(//span[@class="rt-input-container__meta rt-input-container__meta--error"])[3]')))

def test_registration_with_max_allowed_number_of_symbol_email_255_symbol():
   driver.find_element(By.XPATH, '(//a[@class="rt-link rt-link--orange"])[2]').click()
   assert WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'register')))
   driver.find_element(By.NAME, 'firstName').send_keys('Ааааааааааааааааааааааааааааа')
   driver.find_element(By.NAME, 'lastName').send_keys('Ааааааааааааааааааааааааааааа')
   driver.find_element(By.ID, 'address').send_keys('test@SwT9z0oM6CwFxpCzbvmv7XB5btk4bMkt9rHB39EUTXBC19ZKkJZ0SFjwyIrjGnz3sA0gNQxR8RxDIBsNz0Oog5cySDgpaRaVhbX0x76SPrIlq8YZLgS2d3QtXUWoaO4sUPUHFCvXbaN0D0vkf4pa2NF5dIbkFT7e8ZOxRqmEZ1AgEQAtlJEL7BhaGBZ80JKTygl6ZhKlLHpoM859CGBtXmnkjEddTscoZBGWnwcxcj4no7Q5Jql6Ade.ru')
   driver.find_element(By.NAME, 'password').send_keys('abcdeFG1!0000000000')
   driver.find_element(By.NAME, 'password-confirm').send_keys('abcdeFG1!0000000000')
   driver.find_element(By.XPATH, '//button[@type="submit"]').click()
   assert WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.sdi-container--medium')))

def test_registration_with_special_symbols():
   driver.find_element(By.XPATH, '(//a[@class="rt-link rt-link--orange"])[2]').click()
   assert WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'register')))
   driver.find_element(By.NAME, 'firstName').send_keys('う^#%ひ&へ')
   driver.find_element(By.NAME, 'lastName').send_keys('う^#%ひ&へ')
   driver.find_element(By.ID, 'address').send_keys('う^#%ひ&へ')
   driver.find_element(By.NAME, 'password').send_keys('う^#%ひ&へ')
   driver.find_element(By.NAME, 'password-confirm').send_keys('う^#%ひ&へ')
   driver.find_element(By.XPATH, '//button[@type="submit"]').click()
   assert WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.rt-input-container--error')))

def test_autorization_with_inexisting_user_by_phone():
   driver.find_element(By.ID, 'username').send_keys('+79000000000')
   driver.find_element(By.ID, 'password').send_keys('password')
   driver.find_element(By.ID, 'kc-login').submit()
   assert WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'form-error-message')))

def test_autorization_with_inexisting_user_by_mail():
   driver.find_element(By.ID, 'username').send_keys('test@test.mail')
   driver.find_element(By.ID, 'password').send_keys('password')
   driver.find_element(By.ID, 'kc-login').submit()
   assert WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'form-error-message')))

def test_autorization_with_exist_phone_invalid_pass():
   driver.find_element(By.ID, 'username').send_keys('+79*********')
   driver.find_element(By.ID, 'password').send_keys('password')
   driver.find_element(By.ID, 'kc-login').submit()
   assert WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'form-error-message')))

def test_autorization_with_exist_email_invalid_pass():
   driver.find_element(By.ID, 'username').send_keys('pavel.ryazansky@yandex.ru')
   driver.find_element(By.ID, 'password').send_keys('password')
   driver.find_element(By.ID, 'kc-login').submit()
   assert WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'form-error-message')))

def test_autorization_with_email_and_pass_255_symbols():
   driver.find_element(By.ID, 'username').send_keys('test@SwT9z0oM6CwFxpCzbvmv7XB5btk4bMkt9rHB39EUTXBC19ZKkJZ0SFjwyIrjGnz3sA0gNQxR8RxDIBsNz0Oog5cySDgpaRaVhbX0x76SPrIlq8YZLgS2d3QtXUWoaO4sUPUHFCvXbaN0D0vkf4pa2NF5dIbkFT7e8ZOxRqmEZ1AgEQAtlJEL7BhaGBZ80JKTygl6ZhKlLHpoM859CGBtXmnkjEddTscoZBGWnwcxcj4no7Q5Jql6Ade.ru')
   driver.find_element(By.ID, 'password').send_keys('test@SwT9z0oM6CwFxpCzbvmv7XB5btk4bMkt9rHB39EUTXBC19ZKkJZ0SFjwyIrjGnz3sA0gNQxR8RxDIBsNz0Oog5cySDgpaRaVhbX0x76SPrIlq8YZLgS2d3QtXUWoaO4sUPUHFCvXbaN0D0vkf4pa2NF5dIbkFT7e8ZOxRqmEZ1AgEQAtlJEL7BhaGBZ80JKTygl6ZhKlLHpoM859CGBtXmnkjEddTscoZBGWnwcxcj4no7Q5Jql6Ade.ru')
   driver.find_element(By.ID, 'kc-login').submit()
   assert WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'form-error-message')))

def test_forgot_password_is_available():
   driver.find_element(By.ID, 'forgot_password').click()
   assert WebDriverWait(driver, 10).until(EC.url_changes('https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/reset-credentials?client_id=account_b2c&tab_id=jW9hY4kh9BY'))

def test_license_agreement_is_available():
   driver.find_element(By.XPATH, '(//a[@class="rt-link rt-link--orange"])[1]').click()
   assert WebDriverWait(driver, 10).until(EC.url_changes('https://b2c.passport.rt.ru/sso-static/agreement/agreement.html'))
