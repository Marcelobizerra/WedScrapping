#Importando Libs
from requests import get
from bs4 import BeautifulSoup
from warnings import warn
from time import sleep
from random import randint
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import requests
import seaborn as sns

paginas = np.arange(1, 5, 50)
headers = {'Accept-Language': 'pt-BR,pt;q=0.8'}

titulos = [] 
anos = []
generos = []
tempo_duracao = []
votos = []
ratings = []
imdb_ratings = []
imdb_ratings_standardized = []

for pagina in paginas:
    
    response = get("https://www.imdb.com/search/title?genres=sci-fi&"
    + 'start' + str(pagina) + "&explore=title_type,genres&ref_=adv_prv", headers=headers)

# print(response)
    sleep(randint(8, 16))
    if response.status_code != 200:
        warn(f'O pedido: {requests} retornou o código: {response.status_code}') 

#Pegando informações das páginas
    pagina_html = BeautifulSoup(response.text, 'html.parser')
# print(pagina_html)

# Pegando informações por containers

    movie_containers = pagina_html.find_all('div', class_ = 'lister-item mode-advanced')
print(movie_containers)
