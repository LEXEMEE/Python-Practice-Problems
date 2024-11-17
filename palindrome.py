var1 = input("Please enter a number to check wheather that is prime or not : ")
var2 = ""
for i in range(len(var1)-1,-1,-1):
    var2+=var1[i]

if var1 == var2:
    print("Palindrome")
else:
    print("Not a palindrome")
