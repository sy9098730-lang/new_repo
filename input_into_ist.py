# # # n = int(input())
# # # li = []

# # # for i in range(n):
# # #     row = []
# # #     for j in range(n):   # so each row increases
# # #         val = input()
# # #         row.append(val)
# # #     li.append(row)

# # # print("--------------------")
# # # for i in range(len(li)):
# # #     for j in range(len(li[i])):
# # #         print(li[i][j], end=" ")
# # #     print()













# # num=int(input("Enter your number"))
# # li=[]

# # for i in range(num):
# #     row=[]
# #     for j in range(num):
# #         val=input()
# #         row.append(val)
# #     li.append(row)

# # print("_____________________")

# # for i in range(len(li)):
# #     for j in  range(len(li[i])):
# #         print(li[i][j], end=" ")
   
# #     print()

# num=int(input())
# li=[]
# for i in range(num):
#     row=[]
#     for i in range(num):
#         val=input()
#         row.append(val)
#     li.append(row)

# print("-----------------")
# for i in range(len(li)):
#     for j in range(len(li[i])):
#         print(li[i][j],end="")
#     print()
   
# # Find the missing number in a list of 1 to n
# li=[1,2,3,4,5,6,7,8]
# miss=2
# for i in li:
#     if miss in li:
#         print("no")
#         break
#     else:
#         print("yes")
#         break
n = int(input("enter the number: "))
last = n % 10
first = n
while first >= 10:
    first // 10
s = first + last
print(s)


