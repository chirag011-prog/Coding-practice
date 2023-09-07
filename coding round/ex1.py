def cal(r, unit, arr, n):
    total_food = r*unit
    foodtillnow = 0
    house = 0
    for house in range(n):
        foodtillnow = foodtillnow + arr[house]
        if foodtillnow >= total_food:
            break
    if total_food > foodtillnow:
        return 0
    return house+1
r = int(input())
unit = int( input())
n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))
print(cal(r, unit, arr, n))