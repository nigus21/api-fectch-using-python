import requests

for x in range(100):
    response = requests.get('https://randomuser.me/api?gender=male')
    first_name = response.json()['results'][0]['name']['first']
    last_name = response.json()['results'][0]['name']['last']
    print(f'{first_name} {last_name}')

