# -*- coding: utf-8 -*-

# ABC086A - Product

def main():
    b, c = map(int, input().split())
    print(deer(b, c))

def deer(b, c):
    if b * c % 2 == 0:
        return "Even"
    else:
        return "Odd"

main()
