from selenium import webdriver
import chromedriver_binary
import time
from selenium.webdriver.common.by import By
import re  # Регулярные выражения

# Можно добавить опцию --headless => тогда не будет видно окна
browser = webdriver.Chrome()  # Создаем браузера
browser.maximize_window()
browser.get("http://hh.ru")   # Открываем сайт

search_input = browser.find_element(By.ID, "a11y-search-input")
search_input.send_keys("Senior Python")  # Отправить нажатия клавиш

search_button = browser.find_element(By.CSS_SELECTOR, '[data-qa="search-button"]')
search_button.click()

text = browser.find_element(By.CSS_SELECTOR, '[data-qa="vacancies-search-header"] h1').text

# "1 614 вакансий «Senior Python»" => 1614
# Заменям \D на ""
# \D - "все что не является числом"
# \w - "все из чего состоит слово"
# * - "сколько угодно"
#

jobs_count = re.sub(r"\D", "", text)  # Замена
print(f"Jobs Found: {jobs_count}")
time.sleep(1)  # Ждем 5 сек
browser.close()  # Завершаем