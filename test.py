import math

n = int(input("Enter number: "))
n_copy = n

ans = 0
cnt = int(math.log10(n)) + 1 # important
while n > 0:
    temp = n % 10
    ans = temp ** cnt + ans
    n = n // 10

if (n_copy == ans):
    print("YES")
else:
    print("NO")
