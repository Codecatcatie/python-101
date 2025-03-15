
'''
API Base address: https://pokeapi.co/api/v2
Endpoint: /berry/{id or name}

GET https://pokeapi.co/api/v2/berry/{id or name}/

'''
import requests

# Base URL for the Pokemon API
base_url = "https://pokeapi.co/api/v2"

# max 5 berries!
berries_to_harvest = ['rawst', 'cheri', 'chesto', 'pecha', 'aspear', 'persim', 'lum', 'sitrus', 'figy', 'wiki', 'mago', 'aguav', 'iapapa', 'razz', 'bluk', 'nanab', 'wepear', 'pinap', 'pomeg', 'kelpsy', 'qualot', 'hondew', 'grepa', 'tamato', 'cornn', 'magost', 'rabuta', 'nomel', 'spelon', 'pamtre', 'watmel', 'durin', 'belue', 'occa', 'passho', 'wacan', 'rindo', 'yache', 'chople', 'kebia', 'shuca', 'coba', 'payapa', 'tanga', 'charti', 'kasib', 'haban', 'colbur', 'babiri', 'chilan', 'liechi', 'ganlon', 'salac', 'petaya', 'apicot', 'lansat', 'starf', 'enigma']

# Get the Rawst Berry 
rawst_berry_response = requests.get(base_url + "/berry/rawst/")

if rawst_berry_response.status_code == 200:
    print("Rawst Berry found!")
    print(rawst_berry_response.json())
else:   
    print("Rawst Berry not found")
    print(rawst_berry_response.status_code)
    print(rawst_berry_response.text)
    #pick 5 berries and use and api key to find them in a loop.