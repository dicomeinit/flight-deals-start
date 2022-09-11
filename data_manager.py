from pprint import pprint
import requests

SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/c2d1a856596b2c49fddf369be5c51d66/flightDeals/prices"
SHEETY_USERS_ENDPOINT = "https://api.sheety.co/c2d1a856596b2c49fddf369be5c51d66/flightDeals/users"

# response = requests.get(url=SHEETY_USERS_ENDPOINT)
# data = response.json()["users"]
# print(data)

# This class is responsible for talking to the Google Sheet.


class DataManager:

    def __init__(self):
        self.customer_data = None
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data
            )
            print(response.text)
