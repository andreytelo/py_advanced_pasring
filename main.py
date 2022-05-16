import requests
import bs4
from fake_useragent import UserAgent

ua = UserAgent()
KEYWORDS = ['Почему', 'Unit-экономика', 'распродажу']
url = 'https://habr.com/ru/all/'
headers = {'User-Agent': ua.chrome}

response = requests.get(url, headers=headers)
text = response.text

soup = bs4.BeautifulSoup(text, features='html.parser')


def main():
    articles = soup.find_all('article')
    for article in articles:
        kws = article.find(class_='tm-article-snippet__title tm-article-snippet__title_h2')
        kws = kws.text
        for kw in kws.split():
            if kw in KEYWORDS:
                href = article.find(class_='tm-article-snippet__title-link').attrs['href']
                link = 'https://habr.com' + href
                title = article.find('h2').find('span').text
                public_date = article.find('time').attrs['title']
                res = f'Статья "{title}" вышла {public_date} и доступна по ссылке: {link}'
                print(res)


if __name__ == "__main__":
    main()
