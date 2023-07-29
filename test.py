order = [1,2,3,1,2,3,4,1,2,3,1]
max_e = 2
ans = []
for o in order:
    print(f"{ans}\n")
    print(ans.count(o))
    if ans.count(o) < max_e: ans.append(o)