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
