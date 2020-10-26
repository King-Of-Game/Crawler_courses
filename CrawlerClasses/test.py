#!/usr/bin/env python3
# __coding__ : utf-8
# __author__ : YiXuan
# __date__ : 10/13/2020 10:52 PM
# __software__ : PyCharm

import requests
import re

if __name__ == '__main__':
    # url = 'https://tinghaode.me/novel/13883/2860999.html'
    # headers = {
    #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36',
    # }
    # page_text = requests.get(url, headers).text
    # print(page_text)

    str = 'src="asdfafs.png"'
    result = re.findall('[a-z0-9]+\.[a-z0-9]{3}', str)
    print(result)
