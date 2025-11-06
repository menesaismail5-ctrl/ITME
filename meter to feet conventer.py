def meter_to_feet(meters):
        feet = meter*3.28084
        print(meter, "meter is equal to",feet,"feet")
print("Welcom to meter to feet conventer")

meter = float(input("Enter Length in meter:"))

if meter<0:
        print("I think you are wrong,length can't be negative.please enetr a positive number.")
elif meter==0:
        print("0 meter means also 0 feet")
elif meter>0:
        meter_to_feet(meter)
        

        
        
        


                                                                                                                                                                 