inp = raw_input('Enter Hours: ')
hours = float(inp)
inp = raw_input('Enter Rate: ')
rate = float(inp)
if hours > 40:
    pay = hours * rate + (hours - 40) * rate * 0.5
else:
    pay = hours * rate
print 'Pay:', pay
