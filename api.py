print("Start api read application")

# pip install requests

import requests

paginaresult = requests.get('https://catfact.ninja/facts')
feitjes = paginaresult.json()
print(feitjes["current_page"])
print(feitjes["data"][0])