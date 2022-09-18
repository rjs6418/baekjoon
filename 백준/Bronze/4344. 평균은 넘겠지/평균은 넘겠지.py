n = int(input())

for i in range(n):
    scinfo = list(map(int, input().split()))
    sn = scinfo[0]
    score = scinfo[1:]
    ratio = (len(list(filter(lambda x : x > sum(score)/sn, score)))/sn)*100
    print(f"{round(ratio,3):.3f}%")