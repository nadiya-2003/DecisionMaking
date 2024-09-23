

x = int(input())
y = int(input())
z = int(input())
n = int(input())
if x >= n and (y < n or x >= y) and (z < n or x >= z):
    print("L1")
elif y >= n and (z < n or y >= z):
    print("L2")
elif z >= n:
    print("L3")
