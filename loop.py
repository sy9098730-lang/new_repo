# Print numbers from 1 to 10 using a loop.
# Print numbers from 10 to 1 (reverse order).
# Print all even numbers from 1 to 20.
# Print all odd numbers from 1 to 20.
# Print the multiplication table of a given number.
 
# for i in range(1,11):
#     print(i)
# for i in range(11,1,-1):
#     print(i)

# for i in range(1,21):
#     if i%2==0:
#         print(i)

# Find the sum of numbers from 1 to n.
# Find the factorial of a number.
# Count the number of digits in a number.
# Reverse a number using a loop.
# Find the sum of digits of a number.

# num=int(input("Enter :"))
# sum=0
# for i in range(num+1):
#     sum+=i
# print(sum)

# num=int(input("Enter :"))
# mul=1
# for i in range(1,num+1):
#     mul=mul*i

# print(mul)

# Check whether a number is palindrome or not.
# Print Fibonacci series up to n terms.
# Check whether a number is prime or not.
# Find the largest element in a list using loop.
# Count how many vowels are in a string.

num=int(input())
rem=0
tem=num
for i in range(num+1):
    digit=num%10
    rev=rem*10+digit
    num=num//10

if rev==tem:
    print("palindrom")
else:
    print("no")
    
num = int(input())
rev = 0
tem = num

while num>0:   # digits ke hisaab se loop
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10

if rev == tem:
    print("palindrome")
else:
    print("no")


num = int(input())
rev = 0
tem = num

while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10

if rev == tem:
    print("palindrome")
else:
    print("no")


# Check whether a number is palindrome or not.
num=int(input("Enter your number"))
rev=0
q=num

while num>0:
    rem=num%10
    rev=rev*10+rem
    num=num//10

if rev==q:
    print("palindrom")
else:
    print("not palindrom")

# Print Fibonacci series up to n terms.
# num=int(input("Enter your number"))
# a=0
# b=1
# sum=0
# for i in range(num):
#     sum+=a
#     print(a, end="")
#     a,b=b,a+b
    
# print(sum)

# Check whether a number is prime or not.
# num=int(input("Enter your number :"))

# if num<=1:
#     print("not prime")
# else:
#     for i in range(2,num):
#         if num%2==0:
#             print("not prime")
#             break
#     else:
#             print("prime")
# Find the largest element in a list using loop.
# num=int(input("Enter your number"))
# li=[]

# for i in range(num):
#     n=int(input("Enter your number"))
#     li.append(n)

# larg=li[0]

# for i in li:
#     if i>larg:
#         larg=i

# print(larg)

# Count how many vowels are in a string.
s="aei"
count=0
for ch in s:
    if ch in "aioueAEIOU":
        count+=1

print(count)

t = (1,1,2,2,3,4,5)
visited = []

for i in t:
    if i not in visited:
        count = 0
        for j in t:
            if i == j:
                count += 1
        print(i, ":", count)
        visited.append(i)


     