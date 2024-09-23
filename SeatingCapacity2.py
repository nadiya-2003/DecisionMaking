
a = int(input("Enter the seating capacity of L1: "))
b = int(input("Enter the seating capacity of L2: "))
c = int(input("Enter the seating capacity of L3: "))
n = int(input("Enter the number of students: "))
count = 0
if a >= n:
    count += 1
if b >= n:
    count += 1
if c >= n:
    count += 1
print(count)
