from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from lxml import html

from bs4 import BeautifulSoup


team_address_A = {
    'palmeiras' : 'palmeiras/1963',
    'botafogo' : 'botafogo/1958',
    'fluminense' : 'fluminense/1961',
    'atletico-mineiro' : 'atletico-mineiro/1977',
    'cruzeiro' : 'cruzeiro/1954',
    'athletico' : 'athletico/1967',
    'sao-paulo' : 'sao-paulo/1981',
    'santos' : 'santos/1968',
    'fortaleza' : 'fortaleza/2020',
    'red-bull-bragantino' : 'red-bull-bragantino/1999',
    'flamengo' : 'flamengo/5981',
    'gremio' : 'gremio/5926',
    'bahia': 'bahia/1955',
    'internacional': 'internacional/1966',
    'goias': 'goias/1960',
    'vasco' : 'vasco/1974',
    'corinthians' : 'corinthians/1957',
    'cuiaba' : 'cuiaba/49202',
    'america-mineiro' : 'america-mineiro/1973',
    'coritiba' : 'coritiba/1982'
}

def team_search(time:str):
    driver = webdriver.Chrome(ChromeDriverManager().install()) 
    url_base = 'https://www.sofascore.com/team/football/'

    url = url_base + team_address_A[time]

    driver.get(url)

    soup = BeautifulSoup(driver.page_source, 'html.parser')

    conteudo = str(soup)
    estrutura = html.fromstring(conteudo)

    data_dict = {}

    for i in range(2,7):
        base_xpath = f'//*[@id="__next"]/div/main/div/div[3]/div[2]/div/div[4]/div[3]/div[{i}]/div[2]/div[*]/'
        element_1 = estrutura.xpath(base_xpath + 'span[1]')
        element_2 = estrutura.xpath(base_xpath + 'span[2]')
        for data in range(len(element_1)):
            if data == 0:
                data_dict['Time'] = time.title()
            data_dict[element_1[data].text] = element_2[data].text

    return data_dict

a = team_search('flamengo')
