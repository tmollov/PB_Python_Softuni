tabs = int(input())
salary = int(input())

for i in range(tabs):
    site = input().lower()

    if site == "facebook":
        salary -= 150
    elif site == "instagram":
        salary -= 100
    elif site == "reddit":
        salary -= 50

    if salary <= 0:
        print("You have lost your salary.")
        exit()
print(salary)
