# จงเขียนโปรแกรม Python ของโปรแแกรมแสดงข้อความต้อนรับนักศึกษา โดยรับชั้นปีทางแป้นพิมพ์แล้วแสดงข้อควมต้อนรับ
# รับค่าชั้นปีทางแป้นพิมพ์
# แสดงผล

def inputStudentYear():
    studentYear = int(input('ชั้นปี : '))
    return studentYear

def checkStudentYear(studentYear):
    if studentYear == 1:
        return 'Welcome Freshman'
    elif studentYear == 2:
        return 'Welcome Sophomore'
    elif studentYear == 3:
        return 'Welcome Junior'
    elif studentYear == 4:
        return 'Welcome Senior'

def showStudentYear(year,studentYear):
    print(f'ชั้นปี : {year} : {studentYear}')

studentYear = inputStudentYear()
checkYear = checkStudentYear(studentYear)
showStudentYear(studentYear,checkYear)