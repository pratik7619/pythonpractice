print("Welcome")

bill = float(input("what was total bill?"))
tip = int(input("Total % of bill for tip like 10, 15, 20..."))
people = int(input("Total number of people"))

actual_bill_after_tip = bill + ((bill * tip)/100)

split_value = actual_bill_after_tip / people

print(f"Total Share = {round(split_value, 2)}")