import requests
from bs4 import BeautifulSoup
import pandas as pd

#url = 'https://skysports.com/premier-league-table'

def CallApi(url):
    res = requests.get(url)
    res = res.text
    table_list = []
    soup = BeautifulSoup(res, 'html.parser')
    soup = soup.find('table', class_='standing-table__table')
    for table in soup.find_all('tbody'):
        rows = table.find_all('tr')
        for row in rows:
            pl_team = row.find('td', class_='standing-table__cell standing-table__cell--name').text.strip()
            #Finding all td with class number='standing-table__cell' at index number 9
            pl_points = row.find_all('td', class_='standing-table__cell')[9].text
            #printing pl_team alongside pl_points
            print(pl_team, pl_points)
            scrapedTable = {'Team': pl_team,
                            'Pts': pl_points}
            table_list.append(scrapedTable)
    return table_list


data = CallApi('https://www.skysports.com/premier-league-table')
our_data = pd.DataFrame(data)
print(our_data.head())
print(our_data)

our_data.to_csv('ourdata.csv')






