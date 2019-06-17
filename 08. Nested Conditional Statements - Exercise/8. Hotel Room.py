mayOctober = {
   1 : 50,
   2: 65
}

juneSeptember = {
    1 : 75.2,
    2 : 68.7
}

julyAugust = {
    1 : 76,
    2 : 77
}

month = input().lower()
stay = int(input())

apartmentPrice = 0
studioPrice = 0

if stay > 14 and month in ["may","october"]:
    apartmentPrice = mayOctober[2] * 0.9
    studioPrice = mayOctober[1] * 0.70
elif stay > 7 and month in ["may","october"] :
    apartmentPrice = mayOctober[2] 
    studioPrice = mayOctober[1] *0.95
elif stay > 14 and month in ["june","september"] :
    apartmentPrice = juneSeptember[2] * 0.9
    studioPrice = juneSeptember[1] * 0.80
elif stay > 14:
    if month in ["may","october"]:
        apartmentPrice = mayOctober[2] * 0.9
        studioPrice = mayOctober[1]
    if month in ["june","september"]:
        apartmentPrice = juneSeptember[2] * 0.9
        studioPrice = juneSeptember[1]
    if month in ["july","august"]:
        apartmentPrice = julyAugust[2] * 0.9
        studioPrice = julyAugust[1]
else :
    if month in ["may","october"]:
        apartmentPrice = mayOctober[2]
        studioPrice = mayOctober[1]
    if month in ["june","september"]:
        apartmentPrice = juneSeptember[2]
        studioPrice = juneSeptember[1]
    if month in ["july","august"]:
        apartmentPrice = julyAugust[2]
        studioPrice = julyAugust[1]

print(f"Apartment: {apartmentPrice * stay:.2f} lv.")
print(f"Studio: {studioPrice * stay:.2f} lv.")