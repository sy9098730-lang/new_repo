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
dic={
    4:44,
    6:44,
    5:33,
    7:45
}
dic2={}
seen=[]
for k,v  in dic.items():
    if v not in seen:
        dic2[k]=v

print(dic2)
# Invert a dictionary (swap keys and values).
dic={
    1:2,
    2:3,
    3:6
}
new_dic={}
for k,v in dic.items():
    new_dic[v]=k

print(new_dic)
# Find the key with the highest value in a dictionary.
dic={
    1:2,
    2:9,
    3:6
}
max=0
for k,v in dic.items():
    if v>max:
        max=k

print(max) 

dic = {
    1:2,
    2:9,
    3:6
}

max_value = 0
max_key = None

for k,v in dic.items():
    if v > max_value:
        max_value = v
        max_key = k

print(max_key)
# Count how many times each character appears in a string using a dictionary.
str="sosssssssurabhyadavsourabh"
dic={}
for i in str:
    if i in dic:
        dic[i]+=1

    else :
        dic[i]=1

print(dic)

text = "sssssssourabhyadavsourabh"

dic = {}

for i in text:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

print(dic)
# Group words by their first letter using a dictionary.
    
words = ["apple","ant","ball","bat","cat","car"]

dic = {}

for w in words:
    first = w[0]

    if first not  in dic:
        dic[first] = [w]
    else:
        dic[first].append(w)

print(dic) 



words = ["apple","ant","ball","bat","cat","car"]
dic={}
for w in words:
    first=w[0]

    if first not in dic:
        dic[first]=[w]

    else:
        dic[first].append(w)
    

print(dic)



