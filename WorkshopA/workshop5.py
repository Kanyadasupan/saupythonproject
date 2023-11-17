# จงเขียนโปรแกรมPython คำนวนหาเงินเดือนสุทธิของพนักงาน แล้วแสดงผลทางหน้าจอ โดยรับค่ารหัสพนักงาน ชื่อพนักงาน และเงินเดือนปกติของพนักงานทางแป้นพิมพ์ ทั้งนี้เงินเดือนสุทธิของพนักงานนั้นจะต้องหักค่าภาษี และเบี้ยประกันสังคมออกจากเงินเดือนปกติเสียก่อน โดยที พนักงานต้องเสียภาษี 7% ของเงินเดือนปกติ และจ่ายค่าเบี้ยประกันสังคม 500 บาท สูตร เงินเดือนสุทธิ  =  เงินเดือนปกติ  -(เงินเดือนปกติ * 7 / 100) -500

# รับค่ารหัสพนักงาน ชื่อพนักงานและเงินเดือนปกติของพนักงาน
# คำนวนหาเงินเดือนสุทธิของพนักงาน
# แสดงผล

def inputEmployeeIDNameSalary() :
    Id = input("รหัสพนักงาน : ")
    Name = input("ชื่อพนักงาน : ")
    Salary = float(input("เงินเดือนปกติ : "))
    return Id, Name, Salary

def CalNetSalary(Id, Name, Salary) :
    NetSalary =  Salary  -(Salary * 7 / 100) - 500
    return NetSalary

def show (Id,Name,NetSalary) :
    print(f"รหัสพนักงาน {Id} ชื่อพนักงาน {Name} เงินเดือนสุทธิ {NetSalary:.2f} บาท")

Id , Name , Salary = inputEmployeeIDNameSalary()
NetSalary = CalNetSalary(Id , Name , Salary)
show(Id,Name,NetSalary)