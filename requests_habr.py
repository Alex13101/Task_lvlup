
import requests
import bs4
from bs4 import BeautifulSoup
from lxml import html, etree


def get(url):
    resp = requests.get(url)
    if resp.status_code == 200:
        return resp
    return None


if __name__ == '__main__':
    resp = get('https://habr.com/ru/news/')
    print(resp.status_code)

    text = resp.text   # Что это за инфа????
    with open("habr.html", "w", encoding='utf-8') as f:
        f.write(resp.text)


    soup = bs4.BeautifulSoup(text, "lxml")

    feed_child = soup.find("div", class_="tm-articles-list")
    print(len(feed_child))
    post_content = feed_child.find_all('a', class_="tm-title__link")
    long = len(post_content)
    urls = []

    for a in post_content:
        urls.append(a['href'])

    print(urls)
    for i in range(0, long):
        print(f'https://habr.com{urls[i]} -  {post_content[i].text}')
