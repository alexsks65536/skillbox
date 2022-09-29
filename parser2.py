from bs4 import BeautifulSoup

htmlfile = open("skillbox.html", "r", encoding="utf-8")
code = htmlfile.read()
soup = BeautifulSoup(code)
links = soup.findAll("a")  # селектор "а" который найдет все теги ссылок <a></>
print([link.string.strip() for link in links])


