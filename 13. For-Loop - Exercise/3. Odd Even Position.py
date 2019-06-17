count = int(input())

oddElements = []
evenElements = []

for i in range(1, count + 1):
    if i % 2 == 0:
        evenElements.append(float(input()))
    else:
        oddElements.append(float(input()))

if oddElements.__len__() > 0:
    print(
        f"OddSum={sum(oddElements):.2f},\nOddMin={min(oddElements):.2f},\nOddMax={max(oddElements):.2f},"
    )
else:
    print(f"OddSum=0.00,\nOddMin=No,\nOddMax=No,")
if evenElements.__len__() > 0:
    print(
        f"EvenSum={sum(evenElements):.2f},\nEvenMin={min(evenElements):.2f},\nEvenMax={max(evenElements):.2f}"
    )
else:
    print(f"EvenSum=0.00,\nEvenMin=No,\nEvenMax=No")
