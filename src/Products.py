import asyncio.windows_events

import JsonFile

PATH = "../data/products.json"

arr_products = JsonFile.read(PATH)


def search_product_by_tag(arr, str_tag):
    for product in arr:
        if product["tag"] == str_tag:
            return product

    return asyncio.windows_events.NULL


def update_product(product):
    for i, _product in enumerate(arr_products):
        if _product["tag"] == product["tag"]:
            arr_products[i] = product
            return JsonFile.update(PATH, arr_products)

    return False
