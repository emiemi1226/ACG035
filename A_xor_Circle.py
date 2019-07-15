# 両隣のラクダが被っている帽子に書かれた数のビットごとの排他的論理和が自身の被っている帽子に書かれた数と等しい

N = int(input())
A = list(map(int,input().split()))
tp = 0
for n in A:
    tp = tp ^ n
if (tp == 0):
    print("Yes")
else:
    print("No")
