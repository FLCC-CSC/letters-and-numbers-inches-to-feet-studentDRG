# FILE NAME - inchesToFeet.py
# DRG - Rerun for points 2025-02-18-2347
# NAME - 
# DATE - 
# DESCRIPTION

def main():
    convert()

def convert():
    inches = int(input('Enter the number of inches: '))
    feet = int(inches / 12)
    rem = inches % 12
    print(inches, 'inches is', feet, 'feet, and', rem, 'inches')

main()
