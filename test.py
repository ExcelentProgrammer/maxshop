import requests

url = "https://airshop.uz/order_api/"

payload = {
    "stream": "https://airshop.uz/1021/tillaaaa",
    "phone": "+998943990508",
    "name": "samandar"
}
headers = {"Content-Type": "application/json",
           "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
           }

response = requests.request("POST", url, json=payload, headers=headers )

print(response.text)
