targetBook = input()
libraryCapasity = int(input())

counter = 1

while counter <= libraryCapasity:
    book = input()
    if book == targetBook:
        print(f"You checked {counter-1} books and found it.")
        break
    
    if counter == libraryCapasity:
        print("The book you search is not here!")
        print(f"You checked {counter} books.")
        break
    counter +=1