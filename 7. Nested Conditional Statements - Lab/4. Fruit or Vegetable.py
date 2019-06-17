product = input()

fruits = ["banana", "apple", "kiwi", "cherry", "lemon" , "grapes"]
vegetable = ["tomato","cucumber", "pepper", "carrot"]

if product in fruits :
    print("fruit")
elif product in vegetable: 
    print("vegetable")
else :
    print("unknown")