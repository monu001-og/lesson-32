num=int(input("Enter number to check :"))

if num>50:
    print("Number is greater than 50")
    if num%2==0:
         print("Number is an even number")
    else:
         print("And is is odd")
else:
    print("Number is less than 50")
