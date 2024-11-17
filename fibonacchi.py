a= 0
b = 1
limit = int(input("Please enter the last value of Fibonacchi series: "))
print(a,b,end=" ")
temp = 0
while True:
    temp = a + b
    a=b
    b=temp
    if temp<=limit:
        print(temp,end=" ")
    else:
        break