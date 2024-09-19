# Bonifacio, Andrew Dominic G.
# BSCPE 2-3 | September 19, 2024

    # EXERCISE 1 | TEMPERATURE CONVERTER
def temperature_converter():
    while True:
        temperature = input("\nPlease enter a temperature: ")
        conversion = input("\nCelsius To Fahrenheit (Type C) or Fahrenheit to Celsius (Type F): ").upper()

        if conversion == "C":
            print("The temperature in Fahrenheit is: ", (float(temperature) * 9/5 + 32))
        elif conversion == "F":
            print("The temperature in Celsisus is: ", (float(temperature) - 32 )*(5/9))
        else:
            print("Invalid Input")

        if input("\nWould you like to try again? (y/n): ") == "y":
            continue
        else:
            break

#  -------------------------------------------------------------------------------------------------------

    # EXERCISE 2 OHM's LAW CALCULATOR
def Ohms_law():
    while True:
        ohm_calculate = input("\nWhat do you want to calculate? (Resistance, Voltage, Current): ").lower()

        if ohm_calculate == "voltage":
            current = input("\nPlease enter the Current: ")
            resistance = input("\nPlease enter the Resistance: ")
            print("The voltage is", float(current)*float(resistance) )

        elif ohm_calculate == "resistance":
            voltage = input("\nPlease enter the Voltage: ")
            current = input("\nPlease enter the Current: ")
            if current == '0':
                current = input("\nUndefined, enter another current value: ")

            print("The resistance is: ", float(voltage)/float(current))

        elif ohm_calculate == "current":
            voltage = input("\nPlease enter the Voltage: ")
            resistance = input("\nPlease enter the Resistance: ")
            if resistance == '0':
                resistance = input("\nUndefined, enter another resistance value: ")

            print("The current is: ", float(voltage)/float(resistance))
        else:
            print("Invalid Input")

        if input("\nWould you like to try again? (y/n)?:") == "y":
            continue
        else:
            break

# --------------------------------------------------------------------------------------------------------

    # EXERCISE 3 DIAMOND SHAPE

def print_diamond():
    while True:
        n = int(input("\nPlease provide an odd integer: "))
        if n%2 == 0:
            n = int(input("\nPlease provide an odd integer:"))
            for i in range(1, n, 2):
                print(" "*(n//2-i//2), "*"*i)
            for i in range(n, 0, -2):
                print(" "*(n//2-i//2), "*"*i)
        else:
            for i in range(1, n, 2):
                print(" "*(n//2-i//2), "*"*i)
            for i in range(n, 0, -2):
                print(" "*(n//2-i//2), "*"*i)

        if input("\nWould you like to try again? (y/n)?: ") == 'y':
            continue
        else:
            break



# --------------------------------------------------------------------------------------------------------

            # CALLING THE FUNCTIONS WHEN CHECKING

while True:
    exercise = input("\nWhich exercise do you want to check (1,2,3): ")
    if exercise == '1':
        temperature_converter()
    elif exercise == '2':
        Ohms_law()
    elif exercise == '3':
        print_diamond()
    if input("\nContinue checking? (y/n): ") == 'y':
        continue
    else:
        break
