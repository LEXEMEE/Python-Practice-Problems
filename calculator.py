var1= int(input("Please Enter a Number: "))
operator = input("Please Enter a Operator: ")
var2= int(input("Please Enter a Number: "))
if operator=="+":
    print(f"The summation is :{var1+var2}")
elif operator=="-":
    print(f"The substration is {var1-var2}")
elif operator=="*":
    print(f"The product is {var1*var2}")
elif operator=="/":
    print(f"The quotient is {var1/var2}")
elif operator=="%":
    print(f"The remainder is {var1%var2}")
else:
    print("Invalid input")
