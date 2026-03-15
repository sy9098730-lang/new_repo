words = ["apple","ant","ball","bat","cat","car"]
dic={}
for w in words:
    first=w[0]

    if first not in dic:
        dic[first]=[w]

    else:
        dic[first].append(w)
    

     

print(dic)