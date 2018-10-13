import requests
import numpy as np
from scraper_data_fonction import *

brands = ['acer', 'dell', 'lenovo', 'asus', 'hp']
pages = ['', '_2', '_3', '_4', '_5']

promos = {}
for brand in brands:
    promos[brand] = [0]
    for page in pages:
        link = f'https://www.darty.com/nav/achat/informatique/ordinateur_portable/portable/' \
               f'marque{page}__{brand}__{brand.upper()}.html'
        soup = BeautifulSoup(requests.get(link).content, "html.parser")
        promo_raw = soup.find_all('p', 'darty_prix_barre_remise darty_small separator_top')
        if len(promo_raw) > 0:
            promo_int = [int(promo_int.next_element[-3:-1]) for promo_int in promo_raw]
            promos[brand] += promo_int

for brand in brands:
    print(f'Promo {brand.upper()} moyenne = {int(np.mean(promos[brand]))}')


