# # # def rev(s):
# # #     r=''
# # #     for i in s:
# # #         r=i+r
# # #     return r
# # # s= input()
# # # print(rev(s))
# # s='%'
# # print(ord(s))
# # def passed(s):
# #         # code here
# #         i = len(s)//2
# #         if len(s)%2==0:
# #             s1=s[0:i]
# #             s2=s[i:]
# #         else:
# #             s1=s[0:i]
# #             s2=s[i+1:]
# #         print(s1)
# #         print(s2)
# #         s1a,s1b=0,0
# #         for i in range(len(s1)):
# #             s1a+=ord(s1[i])
# #             # print(ord(s1[i]))
# #             s1b+=ord(s2[i])
# #             # print(ord(s2[i]))
# #         print(s1a)
# #         print(s1b)
# #         if s1a==s1b:
# #             return 'YES'
# #         else:
# #             return 'NO'
# # s='bvas'
# # print(passed(s))
# # a=[1,2,3]
# # b=str(a)
# # print(str(b))
# def passed(s):
#         # code here
#         i = len(s)//2
#         if len(s)%2==0:
#             s1=s[0:i]
#             s2=s[i:]
#         else:
#             s1=s[0:i]
#             s2=s[i+1:]
#         a1=sorted(list(s1))
#         a2=sorted(list(s2))
#         b1=''
#         b2=''
#         for i in range(len(s1)):
#             b1+=s1[i]
#             b2+=s2[i]
#         print(b1)
#         print(b2)
#         if b1==b2:
#             return 'YES'
#         else:
#             return 'NO'
# s='bvas'
# print(passed(s))
print(ord('b'))