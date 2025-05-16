import requests
from bs4 import BeautifulSoup
import csv

#Sending a request to the website
url = 'https://en.wikipedia.org/wiki/Kargil_War'  # We can place the url as we required
headers = {'User-Agent': 'Mozilla/5.0'}
response = requests.get(url, headers=headers)

#Parsing the HTML content
soup = BeautifulSoup(response.content, 'html.parser')

#Extracting article titles 
headlines = soup.find_all('a', class_='mw-jump-link')  # We can Modify selector as needed

#Extracting text and save to a list
data = []
for headline in headlines:
    title = headline.get_text(strip=True)
    data.append([title])

#Saving data to a CSV file
with open('data.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Headline'])  # It Creates Header title in the file
    writer.writerows(data)

print("Scraping complete. Data saved to 'data.csv'.")  #confirming the user that the process is completed
