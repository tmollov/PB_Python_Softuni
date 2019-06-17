s500 = {
    "sofia": 0.05,
    "varna": 0.045,
    "plovdiv": 0.055
}

s1000 = {
    "sofia": 0.07,
    "varna": 0.075,
    "plovdiv": 0.08
}

s10000 = {
    "sofia": 0.08,
    "varna": 0.1,
    "plovdiv": 0.12
}

sMax = {
    "sofia": 0.12,
    "varna": 0.13,
    "plovdiv": 0.145
}

city = input().lower()
sellings = float(input())

if city in ["sofia","varna","plovdiv"] and sellings >= 0:
    if 0 <= sellings <= 500 :
        print(f"{s500[city] * sellings:.2f}")
    elif 500 <= sellings <= 1000 :
        print(f"{s1000[city] * sellings:.2f}")
    elif 1000 <= sellings <= 10000 :
        print(f"{s10000[city] * sellings:.2f}")
    elif sellings >= 10000 :
        print(f"{sMax[city] * sellings:.2f}")
else:
    print("error")