hours = input("Enter Hours:")
rate = input("Enter Rate: ")
fhrs = float(hours)
frate = float(rate)
if fhrs > 40:
    reg = fhrs * frate
    ovt = (fhrs - 40) * (frate * 0.5)
    pay = reg + ovt
else:
    pay = fhrs * frate
print('Pay:', pay)


    