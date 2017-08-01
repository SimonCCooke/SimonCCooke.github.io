import requests
from bs4 import BeautifulSoup
import time


def main():

    r = requests.get("http://www.basenotes.net/ID26126902.html")

    data = r.content

    soup = BeautifulSoup(data)

    print(soup.find(itemprop="name").text)
    print(soup.find(itemprop="brand manufacturer").text)
    print(soup.find(itemprop="ratingValue")["content"])
    print(soup.find(itemprop="reviewCount").text)


if __name__ == '__main__':
    main()
    time.sleep(60)
