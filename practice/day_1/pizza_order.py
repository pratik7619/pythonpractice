print("Welcome to Domino\'s Pizza \n\n")

size = input("What size of Pizza you want? S, M or L \n")

SMALL = "Small"
MEDIUM = "Medium"
LARGE = "Large"

pizzaPrice = 0
pizzaLabel = ""

if size == "s" or size == "S":
    pizzaPrice = 15
    pizzaLabel = SMALL
elif size == "m" or size == "M":
    pizzaPrice = 20
    pizzaLabel = MEDIUM
else:
    pizzaPrice = 25
    pizzaLabel = LARGE

needExtraPepperoni = input(f'Do you need extra pepperoni for {pizzaLabel} pizza? \n')

if needExtraPepperoni == "y" or needExtraPepperoni == "Y":
    if pizzaLabel == SMALL:
        pizzaPrice += 3
    elif pizzaLabel == MEDIUM:
        pizzaPrice += 5
    else:
        pizzaPrice += 7

needExtraCheese = input(f'Do you need extra cheese for {pizzaLabel} pizza? \n')
if needExtraCheese == "y" or needExtraCheese == "Y":
    pizzaPrice += 1

print("\n\n")
print("===========================")
print(f"Pizza Size = {pizzaLabel}")
print(f"Total Price = {pizzaPrice}")
print("===========================")
