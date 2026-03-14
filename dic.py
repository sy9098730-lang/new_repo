# Create a dictionary and print it.
dic={
    "Name":"Sourabh",
    "Age":22,
    "course":"python"
}
# print(dic)

# Access a value from a dictionary using a key.
print(dic["Name"])
# Add a new key–value pair to a dictionary
dic["city"]="indore"
print(dic)
dic["Age"]=24
print(dic)
# Remove an element from a dictionary.
dic={
    "Name":"Sourabh",
    "Age":22,
    "course":"python"
}
dic.pop("type","not found")
print(dic)
# Print all keys of a dictionary.
dic={
    "Name":"Sourabh",
    "Age":22,
    "course":"python"
}
print(dic.keys())
print(dic.values())
print(dic.items())
print(len(dic))

# Check whether a key exists in a dictionary or not.

dic={
    "Name":"Sourabh",
    "Age":22,
    "course":"python"
}
if "Sourabh" in dic.values():
    print("yes")
else:
    print("no")

# Iterate through a dictionary and print keys and values.
dic={
    "Name":"Sourabh",
    "Age":22,
    "course":"python"
}
for key,value in dic.items():
    print(key ,":",value)

# Merge two dictionaries.
dic={
    "name":"sourabh",
    "Age":24,

}

dic2={
    "city":"Indore"
}
dic.update(dic2)

print(dic)
# Count the frequency of elements in a list using a dictionary.
list=[2,3,4,5,2]
freq={}
for i in list:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1

print(freq)
# Find the maximum value in a dictionary.
dic={
    "Name":"Sourabh",
    "Age":22,
    "course":"pythone"
}
max=dic[0]
for i in dic:
    if i > max:
        max=i

print(max)
# Find the minimum value in a dictionary.
dic={
    4:44,
    3:45
}
min=list(dic.keys())[0]
for i in dic:
    if i < min:
        min=i

print(min)
# Sort a dictionary by keys.

dic={
    4:88,
    3:45,
    2:55
}
sort=dict(sorted(dic.keys()))
print(sort)
# Sort a dictionary by keys.
dic={
    4:90,
    3:45,
    2:55
}
sort=list(sorted(dic.values()))
print(sort)
# Create a dictionary from two lists (keys list and values list)
keys = [2,3,4,5]
values = [22,33,44,55]

dic={}
for i in range(len(keys)):
    dic[keys[i]]=values[i]

print(dic)
#  Find the sum of all values in a dictionary. 
dic={
    2:33,
    4:33,
    5:33,
    6:1
}
sum=0
for i in dic.values():
    sum+=i

print(sum)
# Create a dictionary using dictionary comprehension.
dic={x:x for x in range(5)}
print(dic)

# Remove duplicate values from a dictionary.




