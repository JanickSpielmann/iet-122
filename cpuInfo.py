#!/usr/bin/python3.5

cpuinfo = open('/proc/cpuinfo', 'r')

print(cpuinfo)

liste = cpuinfo.readlines()

print(liste)