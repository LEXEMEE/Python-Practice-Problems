import math
list1 = []  
max_value = -math.inf 
min_value = math.inf
max_point = 0
min_point = 0
var1 = int(input("Please enter the lenth of the List: "))
for count in range(var1): 
    new_list = int(input("Enter elements: ")) 
    if new_list >= max_value:
        max_value = new_list
        max_point = count + 1
    if new_list <= min_value:
        min_value = new_list
        min_point = count + 1
    list1.append(new_list)
print("List :",list1)
print("Smallest number is :",min_value,",was found at location :",min_point-1,"\nLargest number is :",max_value,",was found at location :",max_point-1)
 
    
    
