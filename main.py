import asyncio
from productclass import Procuct
from crawler import get_Procuct
# RJ01165984
# RJ01284758
# RJ01282013

# RJ01170484
# RJ01228943
plist = ['RJ01165984', 'RJ01284758', 'RJ01282013', 'RJ01289104']

for p in plist:
    product : Procuct = asyncio.run(get_Procuct(p))
    print(product)
