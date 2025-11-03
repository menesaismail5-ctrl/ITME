# ITME
classify_person=int(input("please enter your age_"))
if 0<=classify_person<=12:
        print("child")
        
elif 13<=classify_person<=17:
        print("you are a teenager")
elif 18<=classify_person<=64:
        print("you aare an adult")
elif 65<=classify_person<=250:
        print("you are a senior")
elif classify_person>250:
        print("you are dead my bro!!")
