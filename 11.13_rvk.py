import math

arr = int(input())
counter = 0
while arr != 0:
    arr = arr // 10
    counter += 1
print('Lenght of arr =', counter)



arr = int(input())
arr2 = arr
counter = 0
while arr >= 2:
    arr = math.sqrt(arr)
    counter += 1
print(arr,counter)



counter = 0
arr = int(input())
if arr < 1:
    print('Your number is negative or 0')
    break
else if arr < 2:
    print('1 is neither prime or non-prime')
    break
else:
    for j in range(2, arr)
        for i in range(2, arr//2):
                if (!(arr % i)) == 0:
                    counter += i