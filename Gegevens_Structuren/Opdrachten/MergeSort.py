from heapq import merge
import random
val = input("Enter the amount of random numbers: ")
list = []
counter = 0

for i in range(0,int(val)):
    n = random.randint(1,100)
    list.append(n)

# def calculatehalf(arr):
#     return int(round(len(arr)/2))

# half = calculatehalf(list)

# part1 = list[:half]
# part2 = list[half:]

# def merge(arr, l,r):
#     return l.append(r)

# def mergesort(arr, l,r):
#     if len(l) == 2:
#         if l < r:
#             arr = l.append(r)
#         else:
#             arr = r.append(r)
#     else:
#         mergesort(arr, l, calculatehalf(l))
#         mergesort(arr,r, calculatehalf(r))
#         merge(arr, l,r)
counter = 0
def mergeSort(arr):
    global counter
    if len(arr) > 1:
        counter = counter +1
        r = len(arr)//2
        leftArr = arr[:r]
        rightArr = arr[r:]

        mergeSort(leftArr)
        mergeSort(rightArr)

        i = j = k = 0

       
        while i < len(leftArr) and j < len(rightArr):
            counter = counter +1
            if leftArr[i] < rightArr[j]:
                arr[k] = leftArr[i]
                i += 1
            else:
                arr[k] = rightArr[j]
                j += 1
            k += 1

       
        while i < len(leftArr):
            counter = counter +1
            arr[k] = leftArr[i]
            i += 1
            k += 1

        while j < len(rightArr):
            counter = counter +1
            arr[k] = rightArr[j]
            j += 1
            k += 1

mergeSort(list)
print(list)
print(counter)
# print(part1)
# print(part2)
# print(half)
# print(list[half])