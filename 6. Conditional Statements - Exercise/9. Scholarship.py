import math

income = float(input())
studentProgress = float(input())
minimumWorkSalary = float(input())

socialSchoolarship = 0
excellentResult = 0

if income < minimumWorkSalary :
    socialSchoolarship = minimumWorkSalary * 0.35

if studentProgress >= 5.5 :
        excellentResult = studentProgress * 25

if income > minimumWorkSalary and studentProgress < 5.5 :
    print("You cannot get a scholarship!")
elif income < minimumWorkSalary and studentProgress < 4.5 :
    print("You cannot get a scholarship!")
elif income < minimumWorkSalary and studentProgress >= 4.5 and studentProgress <= 5.5 :
   print("You get a Social scholarship %.0f BGN" % socialSchoolarship)
elif income < minimumWorkSalary and studentProgress >= 4.5 and socialSchoolarship > excellentResult :
   print("You get a Social scholarship %.0f BGN" %socialSchoolarship)
elif income < minimumWorkSalary and studentProgress >= 5.5 and excellentResult > socialSchoolarship :
   print("You get a scholarship for excellent results %.0f BGN" % excellentResult)
elif income >= minimumWorkSalary and studentProgress >= 5.5 :
    print("You get a scholarship for excellent results %.0f BGN" % math.floor(excellentResult))
