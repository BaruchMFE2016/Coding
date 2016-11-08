# Asks the user to input 10 integers, and then prints the largest odd number that was entered
# If no odd numbers, print a message
from _testcapi import INT_MIN
count = 0
count_odd = 0
last_odd = INT_MIN
while count <= 4:
    x = raw_input('Enter the number: ')
    print 'the', count+1, 'number you put in is: ', x
    if int(x) % 2 != 0:
        count_odd += 1
        if int(x) > int(last_odd):
            last_odd = x
        else:
            last_odd = last_odd
    count += 1

if count_odd == 0:
    print 'there is no odd number you put in'
else:
    print 'The largest odd number is: ', last_odd













