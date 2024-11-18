octal = input("Please enter a Octal number number: ")
integer,fraction = octal.split(".")
decimal = 0
p_power = 0
#For the integer part of the binary number 
for i in range(len(integer)-1,-1,-1):
    decimal+= (int(integer[i]))* 8**(p_power)
    p_power+=1
#for the fractional part of the binary number
n_power = -1
for i in range(len(fraction)):
    decimal+= (int(fraction[i]))* 8**(n_power)
    n_power-=1

print(f"{decimal} is the the decimal value of the given {octal} Number")
