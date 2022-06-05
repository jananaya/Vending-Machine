import JsonFile

PATH = "./data/coins.json"

arrCoins = JsonFile.read(PATH)


def sortByDenominationDes(arrAvaibleCoins):
    return sorted(arrAvaibleCoins, key=lambda x: x["denomination"], reverse=False)


def searchCoinByDenomination(nDenomination):
    for i in range(len(arrCoins)):
        if arrCoins[i]["denomination"] == nDenomination:
            return i

    return -1


def updateCoinsQuantity(arrLostCoins):
    for lostCoin in arrLostCoins:
        coinIndex = searchCoinByDenomination(lostCoin["denomination"])

        if (coinIndex == -1):
            continue

        c = arrCoins[coinIndex]
        c["quantity"] -= lostCoin["quantity"]
        arrCoins[coinIndex] = c

        JsonFile.update(PATH, arrCoins)


def updateCoin(coin):
    coinIndex = searchCoinByDenomination(coin["denomination"])

    if coinIndex == -1:
        return False

    arrCoins[coinIndex] = coin

    return JsonFile.update(PATH, arrCoins)
