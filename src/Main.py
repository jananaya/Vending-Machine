import VendingMachine
import Products
import Coins


def selectOption(nOption):
    match nOption:
        case 1:
            print(Products.arrProducts)
            return
        case 2:
            VendingMachine.toSell(Products.arrProducts, Coins.arrCoins)
            return
        case _:
            print("Error, option is not valid!\n")
            return


while (True):
    strOptions = "CHOICE ONE OPTION:\n\n1. To get list of products\n2. Buy product\n>> "
    nOption = int(input(strOptions))

    selectOption(nOption)
