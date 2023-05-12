import requests
from bs4 import BeautifulSoup
import pandas as pd



category = 'sequential art_5'.replace(' ' ,'-')

book_url = f"https://books.toscrape.com/catalogue/category/books/{category}/"


response = requests.get(book_url)
soup = BeautifulSoup(response.content, 'html.parser')

items = []

book_title = soup.find_all('h3')
book_price = soup.find_all('p',{'class' : "price_color"})

for i in range(1,5):
        print(f'Loading page...{i} ' + book_url + f'page-{i}.html')

        for title,price in zip(book_title, book_price):
                # print(title.text, " - " ,price.text)

                
                try:
                        b_title = title.text
                        b_price = price.text
                        items.append([b_title , b_price])
                        
                        # print(title.text, " - " ,price.text)
                except ArithmeticError:
                        continue
df = pd.DataFrame(items,columns=['Book Title', 'Price'])
print(df)
df.to_excel(f'{category}.xlsx')
    

