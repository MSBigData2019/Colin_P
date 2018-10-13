# -*-coding:utf-8 -*

#
#  Lesson 2 - Scrapping HTML - 12/10/18 - CP
#
#  Besoin métier: Analyser les performances financières des sociétés cotées
#               pour décider d'une stratégie d'investissement.
#
# Récupérer les infos suivantes :
# * les ventes au quartier à fin décembre 2018
# * le prix de l'action et son % de changement au moment du crawling
# * le % Shares Owned des investisseurs institutionels
# * le dividend yield de la company, le secteur et de l'industrie
#
# pour les sociétés suivantes : Aribus, LVMH et Danone.
# Un exemple de page https://www.reuters.com/finance/stocks/financial-highlights/LVMH.PA.
# _____________________________________________________________


import requests
import pandas as pd
import datetime
from scraper_data_fonction import *

# Création du dataframe pandas pour stockage des sorties
columns = ['Company', 'Date', 'Sale quarter', 'Shares price', 'Shares percent', 'Shares_owned',
           'Dividend yield company', 'Dividend yield sector', 'Dividend yield industry']
df = pd.DataFrame(columns=columns)

# Sociétés cibles
# Possibilité de rajouter des indices selon sigle reuters
company_list = ['LVMH.PA', 'AIR.PA', 'DANO.PA']
square_link = 'https://www.reuters.com/finance/stocks/financial-highlights/'

# Récupération des pages HTML brutes
# Stockage des sigles sociétés dans le df
html_req_get_list = []
for i, company in enumerate(company_list):
    html_req_get_list.append(requests.get(square_link + company))
    df.loc[i] = [company, str(datetime.date.today()), '', '', '', '', '', '', '']

# Scrap des indices définis dans 'columns' et stock dans le dataframe
for i, html in enumerate(html_req_get_list):
    soup = html_to_soup(html)
    df.loc[i][2] = sale_quarter_crawler(soup)
    df.loc[i][3] = shares_price_crawler(soup)
    df.loc[i][4] = shares_percent_crawler(soup)
    df.loc[i][5] = shares_owned_institutions_crawler(soup)
    df.loc[i][6] = dividend_yield_crawler(soup)[0]
    df.loc[i][7] = dividend_yield_crawler(soup)[1]
    df.loc[i][8] = dividend_yield_crawler(soup)[2]

print(df)
