import JsonFile

PATH = "../data/coins.json"

arr_coins = JsonFile.read(PATH)


def sort_by_denomination(arr_available_coins):
    return sorted(arr_available_coins, key=lambda x: x["denomination"], reverse=False)


def search_coin_by_denomination(n_denomination):
    for i in range(len(arr_coins)):
        if arr_coins[i]["denomination"] == n_denomination:
            return i

    return -1


def update_coins_quantity(arr_lost_coins):
    for lostCoin in arr_lost_coins:
        coin_index = search_coin_by_denomination(lostCoin["denomination"])

        if coin_index == -1:
            continue

        c = arr_coins[coin_index]
        c["quantity"] -= lostCoin["quantity"]
        arr_coins[coin_index] = c

        JsonFile.update(PATH, arr_coins)


def update_coin(coin):
    coin_index = search_coin_by_denomination(coin["denomination"])

    if coin_index == -1:
        return False

    arr_coins[coin_index] = coin

    return JsonFile.update(PATH, arr_coins)
