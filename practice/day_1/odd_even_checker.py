num = int(input("Enter a number \n"))

isEven = num % 2 == 0

if isEven:
    print(f"Entered num {num} is even")
else:
    print(f"Entered num {num} is odd")