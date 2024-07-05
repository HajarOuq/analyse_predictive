import requests
from bs4 import BeautifulSoup
import pandas as pd


def scraping(marque):
    if marque == "Shein":
        url = "https://www.ebuyclub.com/avis/shein-7494"
    elif marque == "Bershka":
        url = "https://www.ebuyclub.com/avis/bershka-6699"
    elif marque == "Pimkie":
        url = "https://www.ebuyclub.com/avis/pimkie-858"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36'}

    s = requests.Session()
    s.headers.update(headers)
    r = s.get(url)

    soup = BeautifulSoup(r.content, "html5lib")

    container_name_brand = soup.find("div", {"class": "fmu-titre flex flex-h titre-page"})
    brand = container_name_brand.img["alt"]

    list_c = []
    
    for z in soup.findAll('div', {'class': 'avis'}):
        commentaire = z.find('p', {'class': 'avis-texte'}).text
        # print(commentaire)
        d = {
            'commentaire': commentaire,
            'brand': brand
        }
        list_c.append(d)

    df = pd.DataFrame(list_c)
    df.to_json(r'data.json')
