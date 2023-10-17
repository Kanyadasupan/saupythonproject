# โปรแกรมตรวจสอบน้ำหนักรถบรรทุกของด่านช่างน้ำหนักว่ารถบรรทุกนั้นมีน้ำหนักรถผ่านเกณฑ์หรือไม่ หากน้ำหนักเกิน1000kg ให้แสดงข้อความว่า "รถน้ำหนักไม่ผ่านเกณฑ์" แต่หากน้ำนักตั้งแต่ 1000 Kg ลงมาให้แสดงข้อความว่า "รถน้ำหนักผ่านเกณฑ์" โดยให้ป้อนทะเบียนรถบรรทุกและน้ำหนักรถบรรทุกทางแป้นพิมพ์

# วิเคราะห์
# มองหา feature การทำงานว่ามีอะไรบ้าง เพื่อจะไปสร้างเป็น function
# รับค่าทะเบียนรถ น้ำหนัก -> inputCarDetial
# ตรวจสอบน้ำหนักรถ และแสดงผล -> checkCarAndShowweight

def inputCarDetail() :
    carNo = input("ป้อนทะเบียนรถ : ")
    carWeight = float(input("ป้อนน้ำหนักรถ : "))
    return carNo, carWeight

def checkCarAndShowWeight(carNo, carWeight) :
    if carWeight > 1000 :
        print(f"{carNo} น้ำหนักไม่ผ่านเกณฑ์")
    else :
        print(f"{carNo} น้ำหนักรถผ่านเกณฑ์")

print("+++++++++++++++++++++++++")
print("T # T Truck Checker T # T")
print("+++++++++++++++++++++++++")
carNo, carWeight = inputCarDetail()
checkCarAndShowWeight(carNo, carWeight)
print("+++++++++++++++++++++++++")
