import requests
from bs4 import Beautifulsoup4
import csv
#URL TO SCRAPE
url="https://example.com"
#Send request
response=requests.get(url)
#parse HTML
soup =Beautifulsoup4(response.text,"html.parser")
#Find all headings
headings = soup.find_all("h2")
#Create CSV file 
with open("Scraped_data.csv","w",newline="",encoding="utf-8")as file:
    writer = csv.writer(file)
    writer.writerow(["Title"])
    for heading in headings:
        writer.writerrow([heading.text.strip()])
        print("Data scraped and saved successfully.")