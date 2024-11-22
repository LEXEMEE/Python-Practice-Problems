print("Type \"triangle\" for print a triangle \nType \"reverse triangle\" to print a reversed triangle \nType \"square\" to print a Square \nType \"circle\" to print a Circle" )
var1 = input("Please enter what do you want to print: ")

if var1 != "circle":
    lenth = int(input("Please enter the lenth of your pattern: "))
else:
    lenth = int(input("Please enter the radius of the circle: "))



def trinagle(lenth):
    for i in range(lenth+1):
        for j in range(i):
            print("*",end=" ")
        print()

        
def square(lenth):
    for i in range(lenth+1):
        for j in range(lenth+1):
            print("*",end=" ")
        print()

def reversed_tringle(lenth):
    for i in range(lenth,0,-1):
        for j in range(i):
            print("*",end=" ")
        print()

def circle(lengh):
    pass

if var1 == "triangle":
    trinagle(lenth)
elif var1 == "reverse triangle":
    reversed_tringle(lenth)
elif var1== "square":
    square(lenth)
elif var1 == "circle":
    circle(lenth)
  


