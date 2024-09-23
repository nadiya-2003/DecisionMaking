
student_type = input().strip()
tuition_fee = float(input())
additional_fee = float(input())
total_fee = 0
if student_type == "MSDS":
    total_fee = tuition_fee + additional_fee  # Tuition fee + Bus fee
elif student_type == "MSH":
    total_fee = tuition_fee + additional_fee  # Tuition fee + Hostel fee
elif student_type == "MGSDS":
    total_fee = (1.5 * tuition_fee) + additional_fee  # 
