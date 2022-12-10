import requests
from bs4 import BeautifulSoup

def send_news():

    global link
    # Отправка GET-запроса на сайт газеты
    url = "https://www.gazeta.ru/news/"
    page = requests.get(url)

    # Превращение html-страницы в текст
    soup = BeautifulSoup(page.text, "html.parser")
    soup1 = BeautifulSoup(page.content, "html.parser")

    # Считывание заголовков и ссылок страницы
    header = soup.findAll("div", class_="b_ear-title")
    articles = soup1.find_all('div', class_='w_col_840')
    for a in articles:
        link = "https://www.gazeta.ru" + a.find('a')['href']

    return header[0].text + "Газета.ру" + "\n" + link


