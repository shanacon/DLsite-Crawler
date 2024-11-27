from config import CATCode, GENREDIC, LANGNAME
from language import LocaleLanguage, LanguageCode
import json
from bs4 import BeautifulSoup
import aiohttp

async def update_genre():
    global GENREDIC
    genredic = {}
    try:
        for cat in CATCode:
            for locale in LocaleLanguage:
                url = f'https://www.dlsite.com/{cat.value}/genre/list?locale={locale.value}'
                async with aiohttp.ClientSession() as session:
                    async with session.get(url) as response:
                        catresponse =  await response.text()
                catsoup = BeautifulSoup(catresponse, 'html.parser')
                genrelist = catsoup.find_all('li', class_ = 'versatility_linklist_item')
                for g in genrelist:
                    gen = g.find('a').get_text().split('(')[0]
                    gnum = g.find('a')['href'].split('/')[-1]
                    
                    if genredic.get(gnum) == None:
                        genredic[gnum] = dict()
                        genredic[gnum] = {lang.name: None for lang in LocaleLanguage}
                    genredic[gnum][locale.name] = gen
        
        genredic = dict(sorted(genredic.items()))
        with open("genre.json", "w", encoding="utf-8") as f:
            json.dump(genredic, f, ensure_ascii = False, indent = 4)
        GENREDIC = genredic

    except Exception as e:
        print(f'error when update_genre {e}')

def load_genre():
    with open("genre.json", "r", encoding="utf-8") as f:
        GENREDIC.update(json.load(f))

def load_lang():
    with open("lang.json", "r", encoding="utf-8") as f:
        LANGNAME.update(json.load(f))


