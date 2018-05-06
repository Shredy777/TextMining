import re

x = '23/6/31'
y = 'false'
t = [s for s in x if s.isdigit()]
t2 = [s for s in y if s.isdigit()]

if t:
    print('true for x')

if t2:
    print('true for y')
