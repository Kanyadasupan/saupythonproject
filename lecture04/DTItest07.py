employee_code = input("รหัสพนักงาน : ")
employee_name = input("ชื่อพนักงาน : ")
normal_salary = float(input("เงินเดือนปกติของพนักงาน : ")) 
net_salary = normal_salary - (normal_salary * 7/100) - 500

nms = format(float(normal_salary),".2f")
nets = format(float(net_salary),".2f")

print(f"พนักงาน",(employee_name),"เงินเดือนสุทธิ",nets,"บาท")
    