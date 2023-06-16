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