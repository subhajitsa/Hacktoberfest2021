def swapPositions(list, pos1, pos2):
     
    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list
 
# Driver function
List = [23, 65, 19, 90]
pos1, pos2  = 1, 3
 
a = 20
b = 30
print(a+b)
print(swapPositions(List, pos1-1, pos2-1))
