
a = int(input())
b = int(input())
c = int(input())
allocated_lab = input()
min_capacity = float('inf')
min_lab = ""
if allocated_lab != "L1":
    if a < min_capacity:
        min_capacity = a
        min_lab = "L1"
        
if allocated_lab != "L2":
    if b < min_capacity:
        min_capacity = b
        min_lab = "L2"
        
if allocated_lab != "L3":
    if c < min_capacity:
        min_capacity = c
        min_lab = "L3"
print(min_lab)
