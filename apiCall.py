import requests

headers = {
    'Content-Type': 'application/json',
    }

data = '{"number": "5"}'


response = requests.post('http://localhost:8000/square', headers=headers, data=data,auth=('block', 'science'))
print(response.json()[0]['Result'])
