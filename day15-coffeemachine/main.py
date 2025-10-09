from machine import Machine
from coffee import Espresso, Cappuccino, Latte

# INITIALIZING

cafmac = Machine()
espresso = Espresso()
latte = Latte()
cappuccino = Cappuccino()

COFFEE_TYPES = {"espresso": espresso,
                "latte": latte,
                "cappuccino": cappuccino}

# START THE MAIN HERE

print("-------------------- COMMANDS --------------------")
print("(espresso / latte / cappuccino) - Makes a coffee of your choice.")
print("(report) - Show the current levels of water, milk and coffee beans.")
print("(refill) - Refills the coffee machine.")
print("(balance) - Shows the current balance on the machine's safe.")
print("(exit) - Exits the program.")
print()

finished = False

while(not finished):
    print("-------------------- COFFEE MACHINE --------------------")
    command = input("Input a command: ").casefold()
    
    match command:
        case "report":
            cafmac.report()
        case "refill":
            cafmac.refill()
        case "balance":
            cafmac.show_balance()
        case coffee_type if coffee_type in COFFEE_TYPES:
            coffee_object = COFFEE_TYPES[coffee_type]
            
            if(cafmac.has_enough_resources(coffee_object.get_ingredients())):
                money = 0
                print(f"The {coffee_type} costs €{coffee_object.price() / 100}.")
                
                money = 0
                
                while(money < coffee_object.price()):
                    print(f"Your balance: €{money / 100}")
                    money += int(input("Insert money in cents: "))
                    
                if(money > coffee_object.price()):
                    print(f"You will receive €{(money - coffee_object.price()) / 100} in change.")
                
                cafmac.make_coffee(coffee_object)
        case "exit":
            print("Goodbye!")
            break
        case _:
            print("Not a valid command!")
    

