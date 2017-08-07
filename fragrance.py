import requests
from bs4 import BeautifulSoup
import time
import sqlite3
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile


def main():

    try:
        conn = sqlite3.connect('test.db')
    except Error as e:
        print(e)
    conn.isolation_level = None
    print("Opened database successfully.")
    cursor = conn.cursor()
    cursor.execute('''create table if not exists fragrance
        (id integer primary key,
        name text,
        brand text,
        rating int,
        reviews text);''')

    print("Table created successfully.")
    cursor.execute("PRAGMA synchronous = OFF")
    cursor.execute("PRAGMA journal_mode = OFF")
    a = []

    frags = fetch_page("http://www.basenotes.net/brand/").find(
            "div", class_="abclist").find_all("a", class_="")
    for frag in frags:
        try:
            int(frag.string)
            if(frag.string != "1907" and frag.string != "4711"):
                a.append(frag.attrs['href'])
        except ValueError:
            pass

    for b in a:
        print(b)
        cursor.execute("begin")
        t0 = time.time()
        cursor = fetch_frag_info(fetch_page(b), cursor)
        t1 = time.time()
        print(t1-t0)
        cursor.execute("commit")

    conn.commit()
    print("Done.")
    df = pd.read_sql_query('''select * from fragrance''', conn)
    writer = ExcelWriter('fragrances.xlsx')
    df.to_excel(writer, sheet_name='Sheet1')

# Close the Pandas Excel writer and output the Excel file.
    writer.save()
    conn.close()


def fetch_page(href):
    r = requests.get(href)
    data = r.content
    soup = BeautifulSoup(data, "lxml")
    return soup


def fetch_frag_info(brandsoup, cursor):

    allfrag = brandsoup.find_all("h3")
    for onefrag in allfrag:
        soup = fetch_page(onefrag.contents[0].attrs["href"])
        data1 = soup.find(itemprop="name").text
        data2 = soup.find(itemprop="brand manufacturer").text

        if(soup.find(itemprop="ratingValue") is None):
            data3 = None
        else:
            data3 = soup.find(itemprop="ratingValue")["content"]

        if(soup.find(itemprop="reviewCount") is None):
            data4 = None
        else:
            data4 = soup.find(itemprop="reviewCount").text

        try:
            cursor.execute(
                '''insert into fragrance(id, name, brand, rating, reviews)
            values(?,?,?,?,?)''', (
                    None,
                    data1,
                    data2,
                    data3,
                    data4))
        except sqlite3.IntegrityError:
            print('Error: ID already exists in PRIMARY KEY')
    if(brandsoup.find(title="Next Page") is not None):
        print(brandsoup.find(title="Next Page").attrs['href'])
        cursor = fetch_frag_info(
                        fetch_page(
                            brandsoup.find(
                                title="Next Page").attrs['href']), cursor)
    return cursor


if __name__ == '__main__':
    main()
    time.sleep(60)
