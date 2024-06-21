import math
m, n = map(int, input().split())
A = [0] * (n+1)

for i in range(2,n+1):
    A[i] = i

sqrtN = int(math.sqrt(n)) # 제곱근까지 수행

for i in range(2, sqrtN):
    if(A[i]==0): continue # 0이라는건 그 부분은 이미 수행했다는 것
    for j in range (i+i, n+1, i): #
        A[j] = 0

for i in range(m, n+1):
    if A[i]!=0:
        print(A[i])
