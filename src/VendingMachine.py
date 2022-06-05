import asyncio.windows_events
import math

import Coins
import Products


def return_change(n_product_value, n_money, arr_available_coins):
    change = {
        "value": n_money - n_product_value,
        "coins": []
    }

    coins_stack = Coins.sort_by_denomination(arr_available_coins)
    money_to_return = change["value"]

    while money_to_return > 0 and coins_stack:
        machine_coin = coins_stack.pop()

        denomination = machine_coin["denomination"]

        quantity = math.trunc(money_to_return / denomination)

        quantity_on_machine = machine_coin["quantity"]

        if quantity > 0:
            if quantity > quantity_on_machine:
                quantity = quantity_on_machine

            user_coin = {
                "quantity": quantity,
                "denomination": denomination
            }
            change["coins"].append(user_coin)
            money_to_return -= quantity * denomination

    return change


def to_sell(arr_products, arr_available_coins):
    str_product_tag = input("Enter product tag: ")

    product = Products.search_product_by_tag(arr_products, str_product_tag)

    if product == asyncio.windows_events.NULL:
        print(
            f"Error, the product with tag \"{str_product_tag}\" doesn't exist!")
        return

    n_money = int(input("Enter money: "))
    n_product_value = product["value"]

    if n_product_value > n_money:
        print("Error, the money is not enough!\n")
        return

    change = return_change(n_product_value, n_money, arr_available_coins)

    print(f"The change is {change['value']}\n")

    product["quantity"] -= 1

    if not Products.update_product(product):
        print("Unexpected error!")
        return

    coins = change["coins"]

    for coin in coins:
        quantity = coin["quantity"]

        if quantity == 1:
            message = f"1 coin of {coin['denomination']}"
        else:
            message = f"{coin['quantity']} coins of {coin['denomination']}"

        print(message)

    Coins.update_coins_quantity(coins)
