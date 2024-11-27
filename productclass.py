import os
from urllib.parse import urljoin, urlparse
import aiohttp
from bs4 import BeautifulSoup
from datetime import datetime
from config import *
from price import Price
from dataclasses import dataclass, field
from language import LanguageCode, LocaleLanguage

class Procuct:
    def __init__(self, product_id : str, apijson: dict, soup : BeautifulSoup = None):
        self.apijson = apijson
        self.soup = soup
        ##
        self.product_id : str = product_id  
        self.site : SITECode = self.get_site()
        self.wishlist : int = self.get_wishlist()
        self.work : str = self.get_work()
        self.price : Price = self.get_price()
        self.is_discount : bool = self.get_isdiscount()
        self.is_only : bool = self.get_isonly()  # 獨家專賣
        self.options : list[LanguageCode, OPTIONCode] = self.get_option()
        self.language : list[LanguageCode] = self.get_language()
        self.release_date : datetime = self.get_release_date()
        self.title : str = self.get_title()
        self.is_free : bool = self.get_isfree()
        self.type : TYPECode = self.get_type()
        self.sales : int = self.get_sales()
        self.circle : str = None
        self.age_category : AgeCode = self.get_age()
        self.genre : list[str] = None
        ##
        self.everyone_translateinfo = self.get_everyone_translateinfo()
    @classmethod
    async def create(cls, productid, apijson, soup = None):
        instance = cls(productid, apijson, soup) 
        instance.circle = await instance.get_circle()
        instance.genre = await instance.get_genre(False)
        return instance
    
    def __str__(self):
        # Formatting the product information
        return (
            f'Product ID: {self.product_id}\n'
            f'Age cat: {self.age_category}\n'
            f'Work Name: {self.work}\n'
            f'Title: {self.title[0]}\n'
            f'Site: {self.site}\n'
            f'Circle: {self.circle[0]}\n'
            f'Wishlist Count: {self.wishlist}\n'
            f'Price: {self.price}\n'
            f'Release Date: {self.release_date}\n'
            f'Type: {self.type}\n'
            f'Language: {", ".join(map(str, self.language))}\n'
            f'Options: {", ".join(map(str, self.options))}\n'
            f'Genre: {", ".join(map(str, self.genre))}\n'
            f'Sales: {self.sales}\n'
            f'Is Discounted: {"Yes" if self.is_discount else "No"}\n'
            f'Is Free: {"Yes" if self.is_free else "No"}\n'
            f'Is Only Sale: {"Yes" if self.is_only else "No"}\n'
        )
    
    def get_site(self):
        return SITECode(self.apijson.get('site_id'))

    def get_wishlist(self):
        return self.apijson.get('wishlist_count')
    
    def get_work(self):
        return self.apijson.get('work_name')
    
    def get_price(self):
        return Price.from_dict(self.apijson.get('currency_price'))

    def get_isdiscount(self):
        return self.apijson.get('is_oly')

    def get_isonly(self): ## 獨家專賣
        return self.apijson.get('is_discount')

    def get_everyone_translateinfo(self):
        return  self.apijson.get('translation_info')

    def get_language(self):
        detail = self.apijson.get('dl_count_items')
        ret = [LanguageCode['JPN']]
        if detail and len(detail) > 0:
            for d in detail:
                if LanguageCode.has_value(d.get('lang')) and LanguageCode[d.get('lang')] not in ret :
                    ret.append(LanguageCode[d.get('lang')])
            return ret
        for option in self.options:
            if type(option) == LanguageCode and option not in ret :
                ret.append(option)

        return ret

    def get_release_date(self):
        return datetime.strptime(self.apijson.get('regist_date'), '%Y-%m-%d %H:%M:%S')

    async def get_circle(self):  # return [circle_name, maker_id]
        id = self.apijson.get('maker_id')
        url = f'https://www.dlsite.com/maniax/circle/profile/=/maker_id/{id}.html'
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                html =  await response.text()
        soup = BeautifulSoup(html, 'html.parser')
        if soup.find('strong', class_ = 'prof_maker_name'):
            return [soup.find('strong', class_ = 'prof_maker_name').get_text(), id]
        else:
            return [None, None]

    def get_title(self):   # return [title_name, title_id]
        if self.apijson.get('title_id') :
            return [self.apijson.get('title_name'), self.apijson.get('title_id')]
        else :
            return [None, None]
        
    def get_isfree(self): 
        return self.apijson.get('is_free')

    def get_type(self):
        return TYPECode(self.apijson.get('work_type'))

    def get_option(self):
        optionlist =  self.apijson.get('options').split('#')
        ret = []
        for option in optionlist:
            if OPTIONCode.has_value(option) :
                obj =  OPTIONCode(option)
                ret.append(obj)
            elif LanguageCode.has_value(option) :
                obj =  LanguageCode[option]
                ret.append(obj)
            else :
                raise ValueError(f'Invalid option value: {option}')
        return ret

    async def save_image(self):
        images_dir = os.path.join(os.getcwd(), 'images')
        if not os.path.exists(images_dir):
            os.makedirs(images_dir)
        img_src = self.apijson.get('work_image')
        img_url = urljoin('https:', img_src) if img_src.startswith('//') else img_src
        filename = os.path.basename(urlparse(img_url).path)
        filepath = os.path.join(images_dir, filename)
        async with aiohttp.ClientSession() as session:
            async with session.get(img_url) as img_response:
                if img_response.status == 200:
                    with open(filepath, 'wb') as img_file:
                        while True:
                            chunk = await img_response.content.read(1024)
                            if not chunk:
                                break
                            img_file.write(chunk)
                    print(f'{filename} 已經下載完成')
                else:
                    print(f'下載 {filename} 時出現錯誤: 狀態碼 {img_response.status}')

    def get_sales(self):
        detail = self.apijson.get('dl_count_items')
        if detail and len(detail) > 0:
            ret = []
            for d in detail:
                ret.append(int(d.get('dl_count')))
            return ret
        else:
            return [int(self.apijson.get('dl_count'))]
    
    def get_age(self):
        return AgeCode(self.apijson.get('age_category'))
    
    async def get_genre(self, returnid = True, locale = LocaleLanguage.jp):
        global GENREDIC
        url = f'https://www.dlsite.com/maniax/work/=/product_id/{self.product_id}.html'
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                html =  await response.text()
        soup = BeautifulSoup(html, 'html.parser')
        ret = []
        try:
            maing = soup.find('div', class_ = 'main_genre')
            maing = maing.find_all('a')
            for g in maing:
                id = g['href'].split('/')[-3]
                if returnid:
                    ret.append(id)
                else:
                    if id not in GENREDIC.keys():
                        GENREDIC[id] = dict()
                        GENREDIC[id][LocaleLanguage.jp.name] = g.get_text()
                    ret.append(GENREDIC[id][locale.name])
        except Exception as e:
            print(f'error when getting genre {e}')
        return ret
