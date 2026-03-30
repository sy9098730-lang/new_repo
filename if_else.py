# # Check if a number is even or odd.
# num=int(input("Enter :"))
# if num%2==0:
#     print("even")
# else:
#     print("odd")

# # Check if a number is positive, negative, or zero.
# num=int(input("Enter your number"))
# if num>0:
#     print("p")
# elif num<0:
#     print("n")
# else:
#     print("Z")

# Check if a year is a leap year.
# num=int(input("Enter :"))
# if num%4==0 and num%100 !=0 or num%400==0:
#     print("l")
# else:
#     print("not")

# Check if a number is a 3-digit number or not.
# num=int(input("Enter : "))
# count=0

# while num>0:
#      count+=1
#      num//=10
       
# print(count)

# Check whether a character is
# # uppercase, lowercase, digit, or special character
# a=input()
# if "A" <= a <="Z" :
#     print("u")
# elif "a" <=a <="z":
#     print("L") 
# elif "0"<= a <="9":
#       print("n")
num = int(input("Enter your number: "))

rev = 0
q = num

while num > 0:
    rem = num % 10
    rev = rev * 10 + rem
    num = num // 10

if rev == q:
    print("Palindrome")
else:
    print("Not Palindrome")