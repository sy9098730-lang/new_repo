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