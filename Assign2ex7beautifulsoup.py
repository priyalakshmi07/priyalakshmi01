
import requests
from bs4 import BeautifulSoup as bs
from openpyxl import Workbook


URL = 'https://www.geeksforgeeks.org/page/'
req = requests.get(URL)
soup = bs(req.text, 'html.parser')

titles = soup.find_all('div', attrs={'class', 'head'})
titles_list = []

count = 1
for title in titles:
    d = {}
    d['Title Number'] = f'Title {count}'
    d['Title Name'] = title.text
    count +=1
    titles_list.append(d)

import pandas as pd
df = pd.DataFrame(data = titles_list[1:],columns =titles_list[0])
df.to_excel('user-page-html.xlsx')
