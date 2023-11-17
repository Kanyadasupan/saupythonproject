# จงเขียนโปรแกรม python คำนวณค่าใช้จ่ายในการซื้อแพ็กเกจท่องเที่ยวของกรุ๊ปทัวร์ ทั้งนี้รูปแบบการใช้งานโปรแกรมจะต้องป้อนชื่อหัวหน้ากรุ๊ปทัวร์ เบอร์โทรศัพท์ติดต่อกลับของหัวหน้ากรุ๊ปทัวร์ และจำนวนคนที่จะไปทัวร์ทางแป้นพิมพ์ โดยในการคิดคำนวณค่าใช้จ่ายในการซื้อแพ็กเกจท่องเที่ยวของกรุ๊ปทัวร์ มีหลักเกณฑ์ในการคิดคำนวณ
# รับค่า ชื่อหัวหน้ากรุ๊ปทัวร์ เบอร์ติดต่อกลัชองหัวหน้ากรุ๊ปทัวร์ จำนวนคนที่ไปทัวร์
# คำนวณค่าใช้จ่ายในการซื้อแพ็กเกจท่องเที่ยว
# แสดงผล

def inputGroupTour():
    nameLeader = input("ชื่อหัวหน้ากรุ๊ป : ")
    groupLeaderContact  = input("เบอร์โทรศัพท์ติดต่อหัวหน้ากรุ๊ปทัวร์ : ")
    countGroupTour = int(input("จำนวนคนที่ไปทัวร์: "))
    return nameLeader, groupLeaderContact, countGroupTour

def checkGroupTour(countGroupTour) :
    if countGroupTour == 1 or countGroupTour ==2 :
        package = countGroupTour * 300
    elif countGroupTour == 3 or countGroupTour <= 5 :
        package = countGroupTour * 250
    elif countGroupTour == 6 or countGroupTour <=10 :
        package = countGroupTour * 210
    else :
        package = countGroupTour * 150
        
    avg = package/countGroupTour
    return package,avg

def showGroupTour(nameLeader, groupLeaderContact, countGroupTour,package,avg):
    print(f"ชื่อหัวหน้ากรุ๊ป : {nameLeader} เบอร์โทรศัพท์ติดต่อ : {groupLeaderContact} จำนวนคนที่ไปทัวร์ : {countGroupTour} แพ็คเก็จ {package} บาท ค่าเฉลี่ย {avg} ต่อคน")

nameLeader, groupLeaderContact, countGroupTour = inputGroupTour()
package,avg = checkGroupTour(countGroupTour)
showGroupTour(nameLeader, groupLeaderContact, countGroupTour,package,avg)