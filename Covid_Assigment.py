# Are you a cigarette addict older than 75 years old? Variable → age
# Do you have a severe chronic disease? Variable → chronic
# Is your immune system too weak? Variable → immune

age = bool(input("age can be assigned only True or If false, just press enter \t"))
chronic = bool(input("chronics can be assigned only True or If false, just press enter\t"))
immune = bool(input("immune can be assigned only True or If false, just press enter\t"))
risk = age and (chronic or immune)
if risk == True :
    print("You are in risky group")
else :
    print("You are not in risky group")