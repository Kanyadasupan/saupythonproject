# จงเขียนโปรแกรม Pythonของโปรแกรมคำนวณค่าคอมมิชชั่นของพนักงานขาย โดยป้อน รหัสพนักงาน ชื่อหนักงาน และจำนวนเงินซึ่งเป็ยอดขายของพนักงาน จากผู้ใช้ทางแป้นพิมพ์ และคำนวณค่าคอมมิชชั่น จากเงื่อนไข
# รับค่ารหัสพนักงาน ชื่อพนักงานและจำนวนเงิน
# คำนวณค่าคอมมิชชั่น
# 

def inputEmployee():
    idEmployee = int(input('รหัสพนักงาน : '))
    nameEmployee = input('ชื่อพนักงาน : ')
    salesEmployee = float(input('ยอดขายที่ทำได้ : '))
    return idEmployee,nameEmployee,salesEmployee

def checkEmployee(salesEmployee):
    if salesEmployee >= 1001 or salesEmployee == 2000:
        return salesEmployee * (1 / 100)
    elif salesEmployee >= 2001 or salesEmployee == 3000:
        return salesEmployee * (3 / 100)
    elif salesEmployee > 3000:
        return salesEmployee * (5 / 100)
    else:
        return salesEmployee * 0
    
def showEmployee(idEmployee,nameEmployee,commission):
    print(f'รหัสพนักงาน : {idEmployee} ชื่อพนักงาน : {nameEmployee} ค่าคอมมิชชั่น: {commission:.2f}')

idEmployee,nameEmployee,salesEmployee = inputEmployee()
commission = checkEmployee(salesEmployee)
showEmployee(idEmployee,nameEmployee,commission)