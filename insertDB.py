import requests
from bs4 import BeautifulSoup
import sqlite3

path = 'datas/sample03.html'

with open(path) as fp:						
    soup = BeautifulSoup(fp, features='lxml', encoding='UTF8')
    links = soup.select('p[id]')				

    with sqlite3.connect("db.sqlite3") as con:
        cur = con.cursor()
        title = ";  link=";
        query = "INSERT INTO sample04 (title, link, creat_date) VALUES (?,<, datetime('now'))"

        for link in links:
            title = str.strip(link.get_text())
            link = link['id']
            cur.execute(query, (title, link))
        con.commit()