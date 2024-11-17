var1 = int(input("Please enter a number: "))
i = 2
prime = True
while i<=(var1/2):
    if var1%i==0:
        prime = False
        break
    i+=1

if prime== True:
    print(f"{var1} is a prime number")
else:
    print(f"{var1} is not a prime number")