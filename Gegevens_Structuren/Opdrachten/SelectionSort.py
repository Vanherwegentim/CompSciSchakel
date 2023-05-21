# import random
# val = input("Enter the amount of random numbers: ")
# randomlist = []
# counter = 0

# for i in range(0,int(val)):
#     n = random.randint(1,9)
#     randomlist.append(n)


# def getSmallestValue (list):
#     global counter
#     value = list[0]
#     for i in range(0,len(list)):
#         counter = counter + 1
#         if value > list[i]:
#             value = list[i]
#     return value

# sortedlist = []
# for index in range(0,int(val)):
#     min_value = getSmallestValue(randomlist)
#     randomlist.remove(min_value)
#     sortedlist.append(min_value)

        

# print(sortedlist)
# print(counter)

import random
# val = input("Enter the amount of random numbers: ")
A = [9,8,7,6,5,4,3,2,1]
counter = 0

# for i in range(0,int(val)):
#     n = random.randint(1,9)
#     A.append(n)
import sys
print(A)
  
# Traverse through all array elements
for i in range(len(A)):
      
    # Find the minimum element in remaining 
    # unsorted array
    min_idx = i
    for j in range(i+1, len(A)):
        counter = counter + 1
        if A[min_idx] > A[j]:
            min_idx = j
              
    # Swap the found minimum element with 
    # the first element        
    A[i], A[min_idx] = A[min_idx], A[i]
  
# Driver code to test above
print ("Sorted array")
for i in range(len(A)):
    print("%d" %A[i],end=" ") 
print(counter)