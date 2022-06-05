from asyncio.windows_events import NULL

import JsonFile

PATH = "./data/products.json"

arrProducts = JsonFile.read(PATH)

def searchProductByTag(arrProducts, strTag):
    for product in arrProducts:
        if product["tag"] == strTag:
            return product

    return NULL

def updateProduct(product):
    for i, _product in enumerate(arrProducts):
        if _product["tag"] == product["tag"]:
            arrProducts[i] = product
            return JsonFile.update(PATH, arrProducts)
    
    return False
