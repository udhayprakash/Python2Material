#!/usr/bin/python
"""
Purpose: Demonstration of Arithmetic Operations
"""

# compound operators
#  += -= *= /= %=

myNumber = 123
print 'myNumber = ', myNumber

myNumber = myNumber + 1
print 'myNumber = ', myNumber

# In cases, where the same variable is present both the sides, then compound operations are valid

myNumber += 1  # myNumber = myNumber + 1
print 'myNumber = ', myNumber

newNumber = 56
myNumber += newNumber + 1  # myNumber = myNumber + newNumber + 1
print 'myNumber = ', myNumber

myNumber -= 58  # myNumber = myNumber - 58
print 'myNumber = ', myNumber

myNumber *= 100  # myNumber = myNumber * 100
print 'myNumber = ', myNumber

myNumber /= 10  # myNumber = myNumber / 10
print 'myNumber = ', myNumber

myNumber %= 10  # myNumber = myNumber % 10
print 'myNumber = ', myNumber


# python dosnt support unary operations ; ++i, i++, --i, i--
# it should used as i += 1, i -=1




print '-----------------------------------------------'
print 'bitwise Operations'
# >> <<
myNewNumber = 4
print 'myNewNumber =', myNewNumber

myNewNumber <<= 1  # myNewNumber = myNewNumber << 1
print 'myNewNumber = ', myNewNumber
#     8 4 2 1
# 4   0 1 0 0  = 0 * 8 + 1 * 4 + 0 * 2 + 0 * 1 = 4
# <<  1 0 0 0

# 13  1 1 0 1
#  7  0 1 1 1
# 15  1 1 1 1

result = 14 >> 2
print '14 >> 2 = ', result
#        8 4 2 1
# 14     1 1 1 0
# >>2    0 0 1 1

result = 3 << 2
print '3 << 2 = ', result
#        8 4 2 1
# 3      0 0 1 1
# <<2    1 1 0 0  =>  12


calculated_result = 10 << 4
print '10 << 4', calculated_result
#           128    64    32    16    8   4   2   1
# 10                                 1   0   1   0
#                                1    0   1   0          1st shift
#                          1     0    1   0              2nd shift
#                    1     0     1    0                  3rd shift
#            1       0     1     0                       4th shift
