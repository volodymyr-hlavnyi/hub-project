import requests
from bs4 import BeautifulSoup
from hw.tools.service import print_name


def hw36_1_input():
    site = input('Enter the name of the site: ')
    if site == '':
        site = "https://realpython.com"
    return site


def hw36_1(name_of_site):
    print(f'Get list of href from the site {name_of_site}')
    try:
        html = requests.get(name_of_site)
    except requests.exceptions.MissingSchema:
        print('The site is not available')
        return
    soup = BeautifulSoup(html.text, "html.parser")
    try:
        links = soup.find_all("a")
    except AttributeError:
        print('The site is not available')
        return
    for i in links:
        href = i.attrs.get("href")
        try:
            if href[:4] == "http":
                print(href)
        except:
            print(href)


def hw36_2_input():
    site = input('Enter the name of the site: ')
    if site == '':
        site = "https://realpython.com"
    level = input('Enter the level: ')
    if level == '':
        level = 2
    return site, level


def hw36_2(name_of_site, level):
    print(f'Get list of href from the site {name_of_site} with level {level}')
    try:
        html = requests.get(name_of_site)
    except requests.exceptions.MissingSchema:
        print('The site is not available')
        return
    soup = BeautifulSoup(html.text, "html.parser")
    h_text = soup.find_all(f"h{level}")
    for tag in h_text:
        text = tag.string
        print(text)


if __name__ == '__main__':
    print("hw36_1")
    name_of_site = hw36_1_input()
    hw36_1(name_of_site)

    print("hw36_2")
    name_of_site, level = hw36_2_input()
    hw36_2(name_of_site, level)
