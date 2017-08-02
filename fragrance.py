import requests
from bs4 import BeautifulSoup
import time
import sqlite3


def main():

    try:
        conn = sqlite3.connect('test.db')
    except Error as e:
        print(e)
    print("Opened database successfully.")
    cursor = conn.cursor()
    cursor.execute('''create table if not exists fragrance
        (id int primary key not null,
        name text not null,
        brand text not null,
        rating text,
        reviews text);''')
    conn.commit()
    print("Table created successfully.")
    r = requests.get("http://www.basenotes.net/ID26126902.html")

    data = r.content

    soup = BeautifulSoup(data)

    cursor.execute(
        '''insert into fragrance(id, name, brand, rating, reviews)
        values(?,?,?,?,?)''',
        (
            "1",
            soup.find(itemprop="name").text,
            soup.find(itemprop="brand manufacturer").text,
            soup.find(itemprop="ratingValue")["content"],
            soup.find(itemprop="reviewCount").text))

    cursor.execute('''select * from fragrance''')
    allrows = cursor.fetchall()
    for row in allrows:
        print('{0} : {1} {2} {3} {4}'.format(
                row[0], row[1], row[2], row[3], row[4]))
    conn.close()

    r = requests.get("http://www.basenotes.net/brand/")

    data = r.content

    soup = BeautifulSoup(data)

    data1 = soup.find("a", string="Gucci")
    data2 = data1.attrs['href']
    data3 = data1.find_next()
    data4 = data3.attrs['href']
    print(data1)
    print(data2)
    print(data3)
    print(data4)

    r = requests.get(data4)
    data = r.content
    soup = BeautifulSoup(data)

    data1 = soup.find_all("h3")
    for single in data1:
        print(single.contents[0].attrs["href"])
#    data2 = data1.contents[0].attrs["href"]
#    print(data2)
#   for i in range(20):
    #    data1 = data1.find_next("h3")
    #    data2 = data1.contents[0].attrs["href"]
    #    print(data2)


if __name__ == '__main__':
    main()
    time.sleep(60)
