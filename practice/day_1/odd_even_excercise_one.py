num = int(input("Enter a number \n"))

if num > 0:
    if num % 2 == 0:
        num = num * 3
    print(f"Entered num = {num}")
else:
    print(f'num is negative {num}')


