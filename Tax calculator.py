x=int(input("enter your salary:"))
tax=0
y=0
if 0<=x<=2000:
        print("your tax is 0 birr")
        print("y")
elif 2000<x<=4000:
        print("yout tax is",x*0.15,"birr")
        print("y")
elif 4000<x<=7000:
        print("your tax is",x*0.20,"birr")
        print("y")
elif 7000<x<=10000:
        print("your tax is",x*0.25,"birr")
        print("y")
elif 10000<x<=14000:
        print("your tax is",x*0.30,"birr")
        print("y")
else:
        print("your tax is",x*0.35,"birr")
if x>=0:
        y=x-tax
        print("your net income is",y,"birr")

