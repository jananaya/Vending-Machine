import VendingMachine
import Products
import Coins

leave_program = False


def select_option(n_option):
    match n_option:
        case 1:
            print(Products.arr_products)
            return
        case 2:
            VendingMachine.to_sell(Products.arr_products, Coins.arr_coins)
            return
        case 3:
            global leave_program
            leave_program = True
            print("Leaving...")
            return
        case _:
            print("Error, option is not valid!\n")
            return


while not leave_program:
    str_options = "CHOICE ONE OPTION:\n\n1. To get list of products\n2. Buy product\n3. Exit\n>> "
    n_option = int(input(str_options))

    select_option(n_option)
