import requests
from bs4 import BeautifulSoup


globo_url = 'https://www.globo.com/'
page = requests.get(globo_url)

resposta = page.text

soup = BeautifulSoup(resposta, 'html.parser')

noticias = soup.find_all('h2', {'class': 'post__title'})
link = soup.find_all('a', {'class': ['post__link', 'keychainify-checked']})



for i in range (len(noticias)):
    print(noticias[i].text, ' o link: ', link[i].get('href'),'\n')