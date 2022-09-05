# -*- coding:utf-8 -*-
# author TokeyJs

import requests

def get_ip():

    target_url = 'https://proxypool.scrape.center/random'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
    }

    res = requests.get(url=target_url, headers=headers).text

    print(res)
    proxies={'https': res}
    code = requests.get(url="http://www.baidu.com", proxies=proxies, headers=headers).status_code
    if code != "200":
        return None

    return proxies






