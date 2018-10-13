# -*-coding:utf-8 -*

#
#  Lesson 2 - Scrapping HTML - 12/10/18 - CP
#
#       Fonction pour récupérer les indices
#           Company, Date, Sale quarter, Shares price, Shares percent, Shares_owned,
#           Dividend yield company, Dividend yield sector, Dividend yield industry
#       de la page finance d'une société depuisle site reuters
#
#
# _____________________________________________________________


import re
from bs4 import BeautifulSoup


def html_to_soup(html_raw):
    """ Parse html to Soup navigable tree for BeautifulSoup
    """
    return BeautifulSoup(html_raw.content, "html.parser")


def sale_quarter_crawler(soup_to_crawl):
    """ Les ventes au quartier à fin décembre 2018 (moyenne)
    """
    sale_quarter = soup_to_crawl.find_all('td', 'data')[1].string
    return sale_quarter


def shares_price_crawler(soup_to_crawl):
    """ le prix de l'action
    """
    shares_price_raw = soup_to_crawl.find('span', 'valueContent').span.string
    shares_price_clean = re.findall(r'-*\d+.?\d*', shares_price_raw)[0]
    return shares_price_clean


def shares_percent_crawler(soup_to_crawl):
    """ et son % de changement au moment du crawling
    """
    shares_percent_raw = soup_to_crawl.find('span', 'valueContentPercent').span.string
    shares_percent_clean = re.findall(r'[-+]\d+.?\d*', shares_percent_raw)[0]
    return shares_percent_clean


def shares_owned_institutions_crawler(soup_to_crawl):
    """le % Shares Owned des investisseurs institutionels
    """
    shares_owned_institutions = soup_to_crawl.find(string='% Shares Owned:').next_element.next_element.string
    return shares_owned_institutions


def dividend_yield_crawler(soup_to_crawl):
    """le dividend yield de la company, le secteur et de l'industrie
    """
    dividen_yield_company = soup_to_crawl.find(string='Dividend Yield').findNext('td').string
    dividen_yield_sector = dividen_yield_company.findNext('td').string
    dividen_yield_industry = dividen_yield_sector.findNext('td').string
    return dividen_yield_company, dividen_yield_sector, dividen_yield_industry