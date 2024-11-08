# Esse script acessa algum site e printa todos os link's existentes no html

import requests
import re

url = 'https://www.vooo.pro/insights/tutorial-sobre-expressoes-regulares-para-iniciantes-em-python/'
check = []
r = requests.get(url)
html = r.text.encode("utf8")
search = re.findall(r'<a href=[\'"?](https[://\w\-._]+)', html.decode("utf8"))

for link in search:
    if link not in check:
        check.append(link)
        print(link)