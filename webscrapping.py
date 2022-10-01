from selenium import webdriver
import chromedriver_binary
import time
from selenium.webdriver.common.by import By
import re  # Регулярные выражения


def parse_hh(job: str):
    # Можно добавить опцию --headless => тогда не будет видно окна
    browser = webdriver.Chrome()  # Создаем браузера
    browser.maximize_window()
    browser.get("http://hh.ru")   # Открываем сайт

    search_input = browser.find_element(By.ID, "a11y-search-input")
    search_input.send_keys(job)  # Отправить нажатия клавиш

    search_button = browser.find_element(By.CSS_SELECTOR, '[data-qa="search-button"]')
    search_button.click()

    text = browser.find_element(By.CSS_SELECTOR, '[data-qa="vacancies-search-header"] h1').text
    jobs_count = re.sub(r"\D", "", text)  # Замена
    browser.close()  # Завершаем
    return jobs_count
