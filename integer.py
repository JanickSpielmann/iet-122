#!/usr/bin/python3.5

from math import sqrt

#String ausgeben
print("-----------------------------------")
print("Hello Python")
print("-----------------------------------")

print("Integers:")
print("Pythagoras")
a = 5 
b = 6
quadratsumme = a**2 + b**2
c = float (sqrt(quadratsumme))
print("a=5, b=6 c= "+ str(c))

print("Division mit / und // Operator")
print(str(100-36/10)+" / Operator")
print(str(100-36//10)+" // Operator")

c = True
d = 10

if (c): 
    print("c is true")

if (d is not 5):
    print("d is not 5")

for x in range(5,20):
    print(str(x))

if(d is 5 or 6 or 10):
    print("true")

if(c and not (d is 10)):
    print("yeah and words")