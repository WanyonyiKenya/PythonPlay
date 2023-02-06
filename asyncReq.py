import grequests
import json

urls = [
    'https://jsonplaceholder.typicode.com/todos',
    'https://jsonplaceholder.typicode.com/todos',
    'https://jsonplaceholder.typicode.com/todos',
    'https://jsonplaceholder.typicode.com/todos',
    'https://jsonplaceholder.typicode.com/todos'
]
response = (grequests.get(u) for u in urls)
responses = grequests.map(response)
print(responses)

for i in responses:
    print(json.loads(i.text))