# Create a tuple with 5 elements and print it.
tuple=(2,3,4,5,8,4)
print(tuple)
# Access the third element of a tuple.
tuple=(2,3,4,5,8,4)
print(tuple.index(4))
# Check if an element 10 exists in a tuple.
tuple=(2,3,4,5,8,4)
for i in tuple:
    if 2 in tuple:
        print("yes")
        break

# Print all elements of a tuple using a loop
tuple=(2,3,4,,5,8,4)
for i in range(len(tuple)):
    print(tuple)
    break
# Write a program to count how many times an element appears in a tuple
tuple=(2,3,3,4,5,8,4)
count=0
for i in tuple:
    if i==3:
        count+=i
    else:
        count=1

print(count)



 
 
