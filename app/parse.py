import requests
from bs4 import BeautifulSoup
from pprint import pprint


URL = 'https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population'
HEADERS = {
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/92.0.4515.159 Safari/537.36',
    'accept': '*/*'}


def get_html(url):
    r = requests.get(url, headers=HEADERS)
    return r


def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    trs = soup.select('table.wikitable tbody tr')

    countries = []
    for tr in trs:
        if tr.td:
            country = tr.a.text
            region = tr.select('td')[1].get_text()
            population = tr.select('td')[2].get_text().replace(',', '')
            countries.append((country, region, population))

    return countries[1:]


def parse():
    html = get_html(URL)

    if html.status_code == 200:
        countries = get_content(html.text)
        return countries
    else:
        print('Error')


if __name__ == '__main__':
    data = parse()
    pprint(data)
    print(len(data))
