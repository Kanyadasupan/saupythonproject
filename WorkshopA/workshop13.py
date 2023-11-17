# จงเขียนโปรแกรม Python ตรวจสอบผลการเรียนของนักเรียนโดยป้อนจำนวนนักเรียน โดยป้อนจำนวนนักเรียนที่ตรวจสอบทางแป้นพิมพ์ และในการตรวจสอบนักเรียนแต่ละคนให้ป้อน รหัสนักเรียน และเกรดเฉลี่ยนักเรียน โดย หากเกรดเฉลี่ยไม่ถึง 2.00 ให้แสดงความทางหน้าจอว่า "สอบไม่ผ่าน" หากได้เกรดเฉลี่ยตั้งแต่ 2.00 ขึ้นไปให้แสดงข้อความทางหน้าจอว่า "สอบผ่าน"
# รับค่าจำนวนนักเรียน รหัสนักเรียน ชื่อนักเรียน เกรดเฉลี่ย
# ตรวจสอบผลการเรียน
# แสดงผล

def inputStudentInfo():
    studentId = input("รหัสนักเรียน: ")
    studentName = input("ชื่อนักเรียน: ")
    studentGrade = float(input("เกรดเฉลี่ยนักเรียน: "))
    return studentId, studentName, studentGrade

def checkStudentGrade(studentId, studentName, studentGrade):
    if studentGrade > 2.00:
        return f"นักเรียนรหัส {studentId} ชื่อ {studentName} ได้เกรดเฉลี่ย {studentGrade} สอบผ่าน"
    else:
        return f"นักเรียนรหัส {studentId} ชื่อ {studentName} ได้เกรดเฉลี่ย {studentGrade} สอบไม่ผ่าน"

def showStudentGrade():
    quantityStudents = int(input("ป้อนจำนวนนักเรียนที่ต้องการตรวจสอบ: "))

    for i in range(quantityStudents):
        studentId, studentName, studentGrade = inputStudentInfo()
        result = checkStudentGrade(studentId, studentName, studentGrade)
        print(result)

showStudentGrade()
