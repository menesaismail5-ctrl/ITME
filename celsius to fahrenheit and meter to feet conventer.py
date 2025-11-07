def meter_to_feet(meters):
    feet = meters * 3.28084
    print(meters, "meters is equal to", feet, "feet.")

def celsius_to_fahrenheit(degree):
    fahrenheit = degree * 9/5 + 32
    print(degree, "Celsius is equal to", fahrenheit, "Fahrenheit.")


print("WELCOME to the Conversion Program!")
print("What would you like to convert?")
print("1. Meters to Feet")
print("2. Celsius to Fahrenheit")

choice = input("Enter 1 or 2: ")

if choice == "1":
    meter = float(input("Enter length in meters: "))
    if meter < 0:
        print("Length can't be negative. Please enter a positive number.")
    elif meter == 0:
        print("0 meter is always 0 feet.")
    else:
        meter_to_feet(meter)

elif choice == "2":
    celsius = float(input("Enter temperature in Celsius: "))
    if celsius < 0:
        print("Ohhh, don't forget to wear warm clothes.")
    elif celsius == 0:
        print("If Celsius is zero, then Fahrenheit is 32 degrees#.")
    else:
        celsius_to_fahrenheit(celsius)

else:
    print("Invalid choice! Please run the program again and enter 1 or 2.")
