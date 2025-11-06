def celsius_to_fahrenheit(degree):
        fahrenheit= degree * 9/5 + 32
        print(degree,"celsius os equal to",fahrenheit,"Fahrenheit")

celsius=float(input("Enter temprature in celsius:"))
if celsius < 0:
        print("what are you doing here! go wear warmm cloth.")
elif celsius==0:
        print("If celsius is zero, then Fahrenheit is 32 degrees.")
else:
        celsius_to_fahrenheit(celsius)
        