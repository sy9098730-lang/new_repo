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