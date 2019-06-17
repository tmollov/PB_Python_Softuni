arr = ["number too small","one","two","three","four","five", "six","seven","eight","nine","number too big"]

number = int(input())

if  number < 1 :
    print(arr[0])
elif number > 9 :
    print(arr[10])
else :
    print(arr[number])