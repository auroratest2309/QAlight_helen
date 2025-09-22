from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By

# створюємо сервіс с драйвером
service = Service(ChromeDriverManager().install())

# запускаем браузер з цим сервісом
driver = webdriver.Chrome(service=service)

driver.get("http://localhost:8000/dz.html")
time.sleep(1)

# перемикаємось на перший фрейм
driver.switch_to.frame("frame1")


frame_1 = driver.find_element(By.ID, "input1")
frame_1.send_keys("Frame1_Secret")
time.sleep(1)

check_button_1 = driver.find_element(By.XPATH, "//button")
check_button_1.click()
time.sleep(1)

# обробка alert
alert = driver.switch_to.alert
assert alert.text == "Верифікація пройшла успішно!", f"Ожидали 'Верифікація пройшла успішно!', а получили '{alert.text}'"
alert.accept()  # закриваем

time.sleep(2)

# негативний кейс
frame_1.clear()  # очищуєм поле
frame_1.send_keys("Frame1_Not_Secret")
time.sleep(1)

check_button_1.click()
time.sleep(2)

alert = driver.switch_to.alert
assert alert.text == "Введено неправильний текст!", f"Ожидали 'Введено неправильний текст!', а получили '{alert.text}'"
alert.accept()

driver.switch_to.default_content()



# перемикаємось на другий фрейм
driver.switch_to.frame("frame2")


frame_2 = driver.find_element(By.ID, "input2")
frame_2.send_keys("Frame2_Secret")
time.sleep(1)

check_button_2 = driver.find_element(By.XPATH, "//button")
check_button_2.click()
time.sleep(1)

# обробка alert
alert = driver.switch_to.alert
assert alert.text == "Верифікація пройшла успішно!", f"Ожидали 'Верифікація пройшла успішно!', а получили '{alert.text}'"
alert.accept()  # закриваєм

time.sleep(2)

# негативний кейс
frame_2.clear()  # очищуєм поле
frame_2.send_keys("Frame2_Not_Secret")
time.sleep(1)

check_button_2.click()
time.sleep(2)

alert = driver.switch_to.alert
assert alert.text == "Введено неправильний текст!", f"Ожидали 'Введено неправильний текст!', а получили '{alert.text}'"
alert.accept()

driver.switch_to.default_content()


driver.quit()


