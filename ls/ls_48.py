import requests
from bs4 import BeautifulSoup

from hw.tools.service import print_name


@print_name
def ls48_1():
    html = requests.get("https://example.com").text
    # Создание объекта Beautiful Soup из HTML-страницы
    soup = BeautifulSoup(html, "html.parser")
    # Извлечение данных из тегов
    title = soup.title.text
    links = soup.find_all("a")
    print("links", links)
    # Навигация по структуре документа
    parent = soup.find("div").parent
    print("parent", parent)
    next_sibling = soup.find("div").next_sibling
    print("next_sibling", next_sibling)
    # Манипуляции с содержимым
    new_tag = soup.new_tag("a", href="https://example.com")
    soup.body.append(new_tag)
    print("soup.body", soup.prettify())


@print_name
def ls48_2():
    # Создание объекта Beautiful Soup из сырого HTML
    html = """
    <html>
    <body>
     <h1>Заголовок</h1>
     <p>Текст параграфа</p>
     <a href="https://example.com">Ссылка</a>
    </body>
    """

    soup = BeautifulSoup(html, "html.parser")
    # Извлечение заголовка
    title = soup.find("h1").text
    print("title", title)
    # Извлечение текста параграфа
    paragraph = soup.find("p").text
    print("paragraph", paragraph)
    # Извлечение ссылки
    link = soup.find("a")["href"]
    print("link", link)


def ls48_3():
    # import requests
    # from bs4 import BeautifulSoup
    html = requests.get("https://realpython.com").text
    soup = BeautifulSoup(html, "html.parser")
    links = soup.find_all("h")
    for i in links:
        href = i.attrs.get("href")
        print(href)


# Написать программу, которая скачивает
# страницу с сайта на выбор с
# актуальным курсом валют,
# выделяет курс доллара к евро и
# выводит его.
# Можно пользоваться регулярными
# выражениями и Beautiful Soup вместе.
def get_curse():
    html = requests.get("https://tables.finance.ua/ua/currency/official/-/1").text
    soup = BeautifulSoup(html, "html.parser")
    name = soup.find_all('span', class_='index')
    title = soup.find_all('span', class_='index')
    for i in zip(name, title):
        cur = i.contents[0]
        print(i, cur)


if __name__ == '__main__':
    # ls48_1()
    # ls48_2()
    # ls48_3()
    get_curse()
