n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))
even_arr =[]
odd_arr = []
for i in range(n):
    if i%2 == 0:
        even_arr.append(arr[i])
    else:
        odd_arr.append(arr[i])
even_arr = sorted(even_arr)
odd_arr = sorted(odd_arr)
print(even_arr) 
print(odd_arr)               
print(even_arr[len(even_arr)-2] + odd_arr[len(odd_arr)-2])