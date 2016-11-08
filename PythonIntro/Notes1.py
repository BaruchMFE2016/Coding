print 'Yankee rule!'
print 'But not in Boston!'
print 'Yankee rule,', 'but not in Boston'

print 5//3  # The integer division, it gives the largest integer of the division operator
print 5**2  # 25, the power operator

pi = 3
radius = 11
area = pi*(radius**2)
print area
radius = 14
print 'the new radius is:', radius

x, y = 2, 3
print x, y

x, y = y, x
print 'the new x, y would be:', x, y

print 'a'
print 3*4
print 3*'a'
print 3+4
print 'a' + 'a'
# while if you type "print a" there will be an error message
# and if you type "print a*a" there will also be an error message
print '4' < 3
print len('abc')
print 'abc'[0]
print 'abc'[-1]
print 'abcdefg'[2:len('abcdefg')]  # output: cdefg
print 'abcdefg'[2:len('abcdefg')-1]  # output: cdef
print 'abcdefg'[2:len('abcdefg')+100]  # output: cdefg

name = raw_input('Enter your name: ')
print 'Are you really', name, '?'
print 'Are you really ' + name + '?'

n = raw_input('Enter an int: ')
print type(n)

print int('3') * 4  # type conversions



