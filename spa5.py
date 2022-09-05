# -*- coding:utf-8 -*-
# author TokeyJs
# url: https://spa5.scrape.center/

import requests

target_url = 'https://spa5.scrape.center/api/book/?limit=18&offset=0'
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
    }
for i in range(30):
    params = {
        'limit': 18*(i+1) ,
        'offset': 18*i
    }

    res = requests.get(url=target_url, params=params, headers=headers).json()
    print(f"*==* The page {i+1}:")
    print(res)


