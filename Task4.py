import random

number1 = random.randint(1, 1000)
number2 = random.randint(1, 1000)

print("your first number is", number1)
print("your second number is", number2)

try:
    answer = int(input("Enter the sum: "))
    if answer == number1 + number2:
        print("You got it right!")
    else:
        print("Wrong number")

except ValueError:
    print("That is not a number")