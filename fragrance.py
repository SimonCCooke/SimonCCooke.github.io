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
        (id integer primary key,
        name text not null,
        brand text not null,
        rating text,
        reviews text);''')

    print("Table created successfully.")

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
        r = requests.get(single.contents[0].attrs["href"])
        data = r.content
        soup = BeautifulSoup(data)
        cursor.execute('''insert into fragrance(name, brand, rating, reviews)
                values(?,?,?,?)''', ("2", "3", "4", "5"))


if __name__ == '__main__':
    main()
    time.sleep(60)
