from requests_html import HTMLSession
import datetime
import sqlite3

#storing data in db by creating/connecting to db
conn =sqlite3.connect('amazontracker1.db')
#cursor will let us manipulate tables in database & exec commands on db, here c is cursor
c = conn.cursor()
c.execute('''CREATE TABLE prices(date DATE, asin TEXT, price FLOAT, title TEXT)''')


#asin are the unique unique identifiers of each prod which is added at the end of the link
asins = ['B08P3VT685','B08F7PTF54','B08F5VCNCY','B07S59ZSMN','B08PV9FJC2']

#start session
s = HTMLSession()

#scrape data
for asin in asins:
    r = s.get(f'https://www.amazon.com/dp/{asin}')
    r.html.render(sleep=1)

    title = r.html.find("#productTitle")[0].text.replace("—","").replace("-","").strip()
    #print(title)

    price = r.html.find("#priceblock_ourprice")[0].text.replace('$', '').replace(",", "").strip()
    #print(price)

    date = datetime.datetime.today()
    #print(asin, price, date)

    #insert values into table
    c.execute('''INSERT INTO prices VALUES(?,?,?,?)''' , (date, asin, price, title))
    print(f'Added for {asin}, {price}')

conn.commit()
print("Committed")

