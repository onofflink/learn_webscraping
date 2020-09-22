import requests, time
from bs4 import BeautifulSoup

# download wikipage
jobsearchUrl = "https://www.google.com/search?sxsrf=ALeKk03e98mgrZzyS-zhBj0F09ts0Gr_1A%3A1600752239063&ei=b4ppX7ezA6WSr7wP3b2jwA8&q=%EC%B7%A8%EC%97%85%EC%82%AC%EC%9D%B4%ED%8A%B8&oq=%EC%B7%A8%EC%97%85%EC%82%AC%EC%9D%B4%ED%8A%B8&gs_lcp=CgZwc3ktYWIQAzIECAAQRzIECAAQRzIECAAQRzIECAAQRzIECAAQRzIECAAQRzIECAAQRzIECAAQR1AAWABgnIUQaABwAngAgAEAiAEAkgEAmAEAqgEHZ3dzLXdpesgBCMABAQ&sclient=psy-ab&ved=0ahUKEwj3ptTkgvzrAhUlyYsBHd3eCPgQ4dUDCA0&uact=5"
result = requests.get(jobsearchUrl, allow_redirects=True)
print(result)

#open(result, 'wb').write(result.cotent)

if result.status_code == 200:
    soup = BeautifulSoup(result.content, "lxml")

parameters = soup.findAll(name='a')

for parameter in parameters:
    print(type(parameters), parameters)
    sleep.time(1)
    



"""
links = soup.select('a')
print(type(links), len(links))
print(links)
for link in links:
    print(type(link), link)
    print('_'*100)

"""