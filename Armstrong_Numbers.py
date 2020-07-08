while True:
    number=input("Please enter number!!!(press q if you want to exit)\n")
    if number=="q":
        break
    if number.isdigit():
        num_len=len(number)
        total=0
        for i in range(len(number)):
            total=total +int(number[i])**num_len
        if total==int(number):
            print(int(number),"is an Armstrong number!")
        else:
            print(int(number),"is not an Armstrong number")
    else :      
        print("It is an invalid entry. Don't use non-numeric, float, or negative values!")