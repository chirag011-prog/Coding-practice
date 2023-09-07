# n=int(input())
# a=[]
# sum =0
# for i in range(n):
#    print(i,"i")
#    a.append(int(input()))
#    print(a,"a")
#    sum+=i
#    print(sum,"sum")

# def retu_arr(n):
#     a=[]
#     for i in range(n):
#         a.append(int(input()))
#     return a
# print(retu_arr(4))
def bubble_sort():
    for i in range(n-1,0,-1):
        for j in range(i):
            if a[j]>a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    return a
n=int(input())
a=[]
for i in range(n):
    a.append(int(input()))
print(bubble_sort())

