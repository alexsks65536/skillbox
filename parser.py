# ЗАДАНИЕ: Дописать код
import json

datafile = open("webinars.json", "r") # Открыть файл
data = json.load(datafile)
print([webinar["date"] for webinar in data])
