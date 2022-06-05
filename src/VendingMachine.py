from asyncio.windows_events import NULL
import math

import Coins
import Products

def returnChange(productValue, nMoney, arrAvaibleCoins):
    change = {
        "value": nMoney - productValue,
        "coins": []
    }

    coinStack = Coins.sortByDenominationDes(arrAvaibleCoins)
    moneyToReturn = change["value"]

    while moneyToReturn > 0 and coinStack:
        machineCoin = coinStack.pop()

        denomination = machineCoin["denomination"]
        
        quantity = math.trunc(moneyToReturn / denomination)
        
        quantityOnMachine = machineCoin["quantity"]

        if quantity > 0:
            if quantity > quantityOnMachine:
                quantity = quantityOnMachine

            userCoin = {
                "quantity": quantity,
                "denomination": denomination
            }
            change["coins"].append(userCoin)
            moneyToReturn -= quantity * denomination

    return change


def toSell(arrProducts, arrAvaibleCoins):
    strProductTag = input('Enter product tag: ')

    product = Products.searchProductByTag(arrProducts, strProductTag)

    if product == NULL:
        print(
            f"Error, the product with tag \"{strProductTag}\" doesn't exist!")
        return

    nMoney = int(input('Enter money: '))
    productValue = product['value']

    if productValue > nMoney:
        print("Error, the money is not enough!\n")
        return

    

    change = returnChange(productValue, nMoney, arrAvaibleCoins)

    print(f"The change is {change['value']}\n")

    product["quantity"] -= 1

    if not Products.updateProduct(product):
        print("Error inesperado!")
        return

    coins = change['coins']

    for coin in coins:
        quantity = coin['quantity']
        message = ""

        if quantity == 1:
            message = f"1 coin of {coin['denomination']}"
        else:
            message = f"{coin['quantity']} coins of {coin['denomination']}"

        print(message)

    Coins.updateCoinsQuantity(coins)