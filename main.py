from data import MENU, resources

isTurnOn = True
amount_Money = 0


def charge_money(p_option):
    penny_amount = float(input("Insert Penny amount: "))
    nickel_amount = float(input("Insert Nickel amount: "))
    dime_amount = float(input("Insert Dime amount: "))
    quarter_amount = float(input("Insert Quarter amount"))
    total_count = penny_amount*.01 + nickel_amount*.05 + dime_amount*.1 + quarter_amount*.25
    change = total_count-MENU[p_option]["cost"]

    if total_count > MENU[p_option]["cost"]:
        print(f"Your change is: ${change}")
    elif MENU[p_option]["cost"] > total_count:
        print("Money is not enough :(")
        return False
    else:
        print("Perfect!")
    return True


def charge_resources(p_option):
    if not p_option == "espresso":
        resources["milk"] = resources["milk"] - MENU[p_option]["ingredients"]["milk"]
        resources["water"] = resources["water"] - MENU[p_option]["ingredients"]["water"]
        resources["coffee"] = resources["coffee"] - MENU[p_option]["ingredients"]["coffee"]


def show_report():
    for item in resources:
        print(item + ": " + str(resources[item]))


while isTurnOn:
    option = input("What do you want to buy? (espresso/latte/cappuccino)")
    if option == "report":
        show_report()
    else:
        if not resources["water"] > MENU[option]["ingredients"]["water"] or not resources["coffee"] > MENU[option]["ingredients"]["coffee"]:
            print("Not enough resources")
        else:
            if not option == "espresso" and resources["milk"] > MENU[option]["ingredients"]["milk"]:
                if charge_money(option):
                    charge_resources(option)
            elif option == "espresso":
                if charge_money(option):
                    charge_resources(option)
            else:
                print("Not enough resources")
