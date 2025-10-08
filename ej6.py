#!/bin/env python3

num=0
for i in range(1,11):
    if i%2==0:
        num+=i
    else:
        continue
print(num)
