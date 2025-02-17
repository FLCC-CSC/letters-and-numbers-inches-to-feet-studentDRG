# FILE NAME - inchesToFeet.py

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
