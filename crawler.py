import aiohttp
from productclass import Procuct
from loader import update_genre, load_genre, load_lang
import os

async def get_Procuct(product_id, updata_gen = False):
    if not os.path.exists('./genre.json') or updata_gen == True:
        await update_genre()
    load_genre()
    load_lang()
    apidata = await fetch_html(product_id, True)
    product = await Procuct.create(product_id, apidata)
    return product


async def fetch_html(product_id, json = False):
    if json :
        url = f'https://www.dlsite.com/maniax/product/info/ajax?product_id={product_id}&cdn_cache_min=1'
    else:
        url = f'https://www.dlsite.com/maniax/work/=/product_id/{product_id}.html'
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if json :
                data = await response.json()
                return data.get(product_id)
            else:
                return await response.text()