import requests
from bs4 import BeautifulSoup

url = 'http://finance.daum.net/api/market_index/days?page=1&perPage=100&market=KOSPI&pagination=true'
# Daum은 header 정보 확인해 임의의 header를 넣어줌
header = {'Referer' :'http://finance.daum.net/domestic/kospi',
          'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0...Safari/537.36'}
res = requests.get(url, headers = header) 		# headers 인자로 fake 접속하기

soup = BeautifulSoup(res.content, 'html.parser')
print(soup.prettify())

import json
rt_dict = json.loads(res.content)
print(rt_dict, rt_dict.keys())
import pandas as pd
pd.DataFrame(rt_dict['data'])
