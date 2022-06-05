import VendingMachine
import Products
import Coins


def select_option(n_option):
    match n_option:
        case 1:
            print(Products.arr_products)
            return
        case 2:
            VendingMachine.to_sell(Products.arr_products, Coins.arr_coins)
            return
        case _:
            print("Error, option is not valid!\n")
            return


while True:
    strOptions = "CHOICE ONE OPTION:\n\n1. To get list of products\n2. Buy product\n>> "
    nOption = int(input(strOptions))

    select_option(nOption)
