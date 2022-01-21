
import requests
from pprint import pprint
url="https://api.coindesk.com/v1/bpi/currentprice.json"
r=requests.get(url) #it gives response object
bitcoin_info=r.json() #converts json into python dict
print("Current Bitcoin price is:-", end=" ")
print(bitcoin_info['bpi']['USD']['rate'])