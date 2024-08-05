#
# скачать к себе на компьютер
# 100 последних фотографий со
# страницы  https://www.flickr.com/explore/
import requests
from bs4 import BeautifulSoup


def hw55_1_input():
    # site = input('Enter the name of the site: ')
    # if site == '':
    site = "https://www.flickr.com/explore/"
    return site


def hw55_1(name_of_site):
    list_img = []
    print(f'Get list of href from the site {name_of_site}')
    try:
        html = requests.get(name_of_site)
    except requests.exceptions.MissingSchema:
        print('The site is not available')
        return
    soup = BeautifulSoup(html.text, "html.parser")
    try:
        links = soup.find_all("img")
    except AttributeError:
        print('The site is not available')
        return
    for i in links:
        href = i.attrs.get("src")
        try:
            if href[:2] == "//":
                print(f"https:{href}")
                list_img.append(f"https:{href}")
        except:
            print(href)
    return list_img


if __name__ == '__main__':
    # n = 5
    # sum = 0
    # while n > 0:
    #     sum += n
    #     n -= 1
    # print(sum)
    #
    # text = "Hello. Word"
    # print(text[7:12])
    #
    # numbers = [1, 2, 3, 4, 5]
    # numbers.append(6)
    # print(numbers)
    #
    # person = {
    #     "name": "John",
    #     "age": 30,
    #     "city": "New York"
    # }
    # del person["age"]
    # print(person)
    #
    # import re
    #
    # text = "The price is $20"
    # result = re.search(r'\d+', text)
    # print(result.group())
    #
    #
    # class Dog:
    #     def __init__(self, name):
    #         self.name = name
    #
    #     def bark(self):
    #         return "Woof!"
    #
    #
    # dog1 = Dog("Buddy")
    # dog2 = Dog("Max")
    # print(dog1.bark() + dog2.name)
    #
    # colors = ['Red', 'Blue', 'Green', 'Black', 'White']
    # del colors[-1]
    # colors.remove('Green')
    #
    # print(colors)

    print("hw55_1")
    name_of_site = hw55_1_input()
    list_links = hw55_1(name_of_site)
    for img in list_links:
        with open(f'img_{list_links.index(img)}.jpg', 'wb') as file:
            file.write(requests.get(img).content)
