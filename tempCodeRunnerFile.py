list=[2,3,4,5,2]
freq={}
for i in list:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1

print(freq)