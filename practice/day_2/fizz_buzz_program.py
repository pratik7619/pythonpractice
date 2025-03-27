'''
print a number form 1 to 10

if a number is divisible by 3, print Fuzz

if number is divisible by 5, print Buzz

if a number is divisible by both, print FizzBuzz
'''

for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FuzzBuzz")
    elif number % 3 == 0:
        print("Fuzz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
