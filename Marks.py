
marks = int(input())
if marks > 100:
    print("Invalid Input")
elif marks == 100:
    print("S")
elif 90 <= marks < 100:
    print("A")
elif 80 <= marks < 90:
    print("B")
elif 70 <= marks < 80:
    print("C")
elif 60 <= marks < 70:
    print("D")
elif 50 <= marks < 60:
    print("E")
else:
    print("F")
