kvm = float(input()) * 7.61

discount = kvm * 0.18
finalPrice = kvm - discount

print('The final price is: %.2f lv.' % round(finalPrice,2))
print('The discount is: %.2f lv.' % round(discount,2))