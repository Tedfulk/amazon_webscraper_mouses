from requests_html import HTMLSession
from datetime import date
import sqlite3

conn = sqlite3.connect("amazontracker.db")

c = conn.cursor()
c.execute("""CREATE TABLE prices(date DATE, asin TEXT, price FlOAT, Title TEXT)""")

asins = ["B09HM94VDS", "B07QN369XX", "B07L4BM851"]

for asin in asins:
    session = HTMLSession()
    response = session.get(f"https://www.amazon.com/dp/{asin}")
    response.html.render(sleep=1)

    price = response.html.find(".a-price-whole", first=True)
    title = response.html.find("#productTitle", first=True)
    price = price.text.replace(".", "").strip()
    title = title.text.strip()
    asin = asin
    date = date.today()
    c.execute("""INSERT INTO prices VALUES(?,?,?,?)""", (date, asin, price, title))
    print(f"added data for {asin}, {price}, {date}, {title}")

conn.commit()
print("commited data to db")
