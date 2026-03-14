dic={
    1:2,
    2:3,
    3:6
}
new_dic={}
for k,v in dic.items():
    new_dic[v]=k

print(new_dic)