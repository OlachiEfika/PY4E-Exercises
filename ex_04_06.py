def computepay(hours, rate):
    if hours > 40:
        reg = hours * rate
        ovt = (hours - 40) * (rate * 0.5)
        pay = reg + ovt
    else:
        pay = hours * rate
    return pay

hours = input("Enter Hours:")
rate = input("Enter Rate: ")
fhrs = float(hours)
frate = float(rate)

gp = computepay(fhrs, frate)

print('Pay', gp)