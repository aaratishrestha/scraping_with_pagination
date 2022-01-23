import requests
from bs4 import BeautifulSoup
import re


def scrape_data(url_with_pagination):
    print("URL: ", url_with_pagination)
    page = requests.get(url_with_pagination)
    soup = BeautifulSoup(page.content, "html.parser")
    table = soup.find("table", class_='table-hover')
    table_body = table.find("tbody")
    for td in table_body.findAll("td"):
        if td.find('div'):
            exit()
        else:
            href_data = td.find_all('a', href=re.compile("pdf"))
            if any(href_data):
                for a in href_data:
                    print("PDF URL: ", a['href'])


if __name__ == "__main__":
    url = "https://ciaa.gov.np/pressrelease?page="
    count = 1
    while True:
        print("Page count : ", count)
        scrape_data(url + str(count))
        count += 1
