import requests
from bs4 import BeautifulSoup
import csv

# get the html
url = "https://www.amazon.com/gp/new-releases/books/23/ref=zg_bsnr_nav_books_1"
headers = {
  'user-agent':
  'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'
}

page = requests.get(url, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')

books = soup.find_all(id="gridItemRoot")

book = books[0]


csv_headers = ['Rank', 'Title', 'Author', 'Price']
with open('amazon_books.csv', 'w', encoding='utf-8', newline='') as f:
  writer = csv.writer(f)
  writer.writerow(csv_headers)

for book in books:
  
  rank = book.find('span', class_='zg-bdg-text').text[1:]
    
  romance = book.find('div', class_="zg-grid-general-faceout").div
  romance.contents[0]

  title = romance.contents[1].text
  author = romance.contents[2].text
  price = romance.contents[-1].text
  
  print(price)
  print(author)
  print(title)
  print(rank)
