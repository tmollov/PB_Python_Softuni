count = int(input())

tons = 0
microbus = 0
truck = 0
train = 0

for i in range(count):
    num = int(input())
    if num < 4:
        microbus += num
    elif num >= 4 and num < 12:
        truck += num
    elif num >= 12 :
        train += num
    tons += num

averagePrice = ((microbus * 200) + (truck * 175) + (train * 120)) / tons
print(f'{averagePrice:.2f}')
print(f'{((microbus/tons)*100):.2f}%')
print(f'{((truck/tons)*100):.2f}%')
print(f'{((train/tons)*100):.2f}%')