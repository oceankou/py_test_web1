import requests
from lxml import etree
import openpyxl

url = 'https://www.xs8.cn/'
headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36'}
resp = requests.get(url,headers=headers)
if resp.status_code == 200:
    pass
else:
    print(f"1111111111111111:{resp.status_code}")

e = etree.HTML(resp.text)




