# Este programa acessa um site via selenium, coleta nome do livro, valor e estoque.

import pandas as pd 
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service,options=options)

# URL alvo
url = ('https://books.toscrape.com/')
driver.get(url)

# Busca e guarda todos os livros na lista
titleElements = driver.find_elements(By.TAG_NAME, 'a')[54:94:2]
titleList = [title.get_attribute('title') for title in titleElements]

# Busca e guarda a quantidade em estoque de todos os livros
stockList = []
precoList = []
for title in titleElements:
    title.click()
    qtsEstoque = int(driver.find_element(By.CLASS_NAME,'instock').text.replace('In stock (','').replace(' available)',''))
    stockList.append(qtsEstoque)
    preco = float(driver.find_element(By.CLASS_NAME,'price_color').text.replace('£',''))
    precoList.append(preco)
    driver.back()

# Mostra titulo e estoque de cada livro
dictDF = {'title': titleList,
          'preco': precoList,
          'stock': stockList}

print(pd.DataFrame(dictDF))

input('presione enter') 