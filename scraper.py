from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup

import csv
import requests
import json
import time

listings = []
listings_file = open('./listings_file.csv','w')
listings_writer = csv.writer(listings_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
for page in range(2,129):
    print(page)
    try:
        html = urlopen("https://www.immobilienscout24.de/Suche/S-T/P-{page}/Wohnung-Kauf/Berlin/Berlin/-/1,00-2,00".format(page=page))
    except HTTPError as e:
        print(e)
    except URLError:
        print("Server down or incorrect domain")
    else:
        res = BeautifulSoup(html.read(), "html5lib")
        listings = res.findAll("li", {"class": "result-list__listing"})
        for listing in listings:
            listing_id = listing["data-id"]
            address = listing.find("div", {"class": "result-list-entry__address"})
            price = listing.find("dd", {"class": "font-nowrap"})
            rooms = listing.find("span", {"class": "onlyLarge"})
            if(address is not None and price is not None and rooms is not None):
                
                address = address.getText()
                parameters = {
                    "address": address,
                    "key": "AIzaSyAANx7P7Rpn-0vnq8lQnpxtCVV-AArQRnI"
                }
                response = requests.get("https://maps.googleapis.com/maps/api/geocode/json", params=parameters)
                json_response = response.json()
                if(json_response["results"][0]["geometry"]["location"] is not None):
                    lat = json_response["results"][0]["geometry"]["location"]["lat"]
                    lng = json_response["results"][0]["geometry"]["location"]["lng"]

                price = price.getText()
                price = price.replace(".","")
                price = price.replace(" €","")

                rooms = rooms.getText()

                row = [listing_id, address, lat, lng, rooms, price]
                print(row)
                listings_writer.writerow(row)

                time.sleep(1)