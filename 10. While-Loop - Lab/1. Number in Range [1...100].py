errorMessage = "Invalid number!"

number = int(input())

while number < 1 or number > 100:
    print(errorMessage)
    number = int(input())

print(f"The number is: {number}")