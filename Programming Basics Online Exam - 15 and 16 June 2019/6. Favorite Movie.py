movie = ""
movieSum = 0

movies = 0
while True :
    name = input()
    if name == "STOP":
        break
    currentLen = 0
    movieLen = name.__len__()
    for i in name:
        char = ord(i)
        if char in range(65,91):
            currentLen += char - movieLen
        elif char in range(97,123):
            currentLen += char - (movieLen * 2)
        else :
            currentLen += char
    if currentLen > movieSum:
        movie = name
        movieSum = currentLen

    movies += 1
    if movies == 7:
        print("The limit is reached.")
        break

print(f"The best movie for you is {movie} with {movieSum} ASCII sum.")