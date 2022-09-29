import requests
from bs4 import BeautifulSoup

"""
    http - запросы
"""

skillbox = requests.get("https://live.skillbox.ru/")
# http - ответ
print(skillbox.status_code)

# webinar-card__title
print(skillbox.headers["Content-Type"])

skillsoup = BeautifulSoup(skillbox.content, "html.parser")
webinars = skillsoup.findAll(class_="webinar-card__title")

# print(webinars)
# print([w.string.strip() for w in webinars])

# пробуем получить дату и название
# webinars__item

webinars_full = skillsoup.findAll(class_="webinars__item")
for webinar in webinars_full:
    title = webinar.find(class_="webinar-card__title").string.strip()
    date = webinar.find(class_="webinar-card__date").string.strip()
    print(f'Вебинар: {title}, прошел: {date}')
