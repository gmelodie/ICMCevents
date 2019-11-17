import requests
from bs4 import BeautifulSoup


def get_icmc_events(debug=False):
    icmc_events = []
    link = 'https://www.icmc.usp.br/eventos'
    page = requests.get(link)

    if debug:
        print(page)

    soup = BeautifulSoup(page.content, 'html.parser')
    quadros = soup.select(".bloco")[0].select(".quadro")

    for quadro in quadros:
        item = {}
        item["link"] = quadro.a["href"]
        item["title"] = quadro.h4.text
        item["date"] = quadro.p.text
        icmc_events.append(item)

    if debug:
        print(icmc_events)

    return icmc_events


def get_iot_news(debug=False):
    with open('apikey.txt') as f:
        key = f.read()[:-1] # remove line breaks

    if debug:
        print(key)

    link = ('https://newsapi.org/v2/top-headlines?'
            'country=br&'
            'apiKey=' + key)
    response = requests.get(link)

    if debug:
        print(response.json())

    return response.json()


if __name__ == '__main__':
    get_icmc_events(debug=True)
    get_iot_news(debug=True)
