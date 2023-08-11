#!/usr/bin/python3

#i = 97
#while i < 123:
#    if i == 101:
#        continue
#    print(f"{i} = {chr(i)}")
#    i = i + 1

for i in [chr(i) for i in range(97, 123) if i !=101 if i != 113]:
    print('{}'.format(i), end='')
