# 2.จงเขียนโปรแกรมPython ของโปรแกรมคำนวณหาค่าเฉลี่ยของคะแนนจากการสอบ 3 ครั้ง โดยรับค่า รหัสนักเรียน ชื่อนักเรียน และคะแนนสอบแต่ละครั้งรวม 3 ครั้งทางแป้นพิมพ์ แล้วแสดงผลค่าเฉลี่ยที คำนวณได้ทางหน้าจอ

# รับค่า รหัสนักศึกษา ชื่อนักเรียน และ คะแนนสอบ 3 ครั้ง
# คำนวนหาค่าเฉลี่ย
# แสดงผล

def inputCodeIDNameScore() :
    StudentID = input("รหัสนักศึกษา : ")
    StudentName = input("ชื่อนักศึกษา : ")
    FirstScore = float(input("คะแนนสอบครั้งที่ 1 : "))
    SecondScore = float(input("คะแนนสอบครั้งที่ 2 : "))
    ThirdScore = float(input("คะแนนสอบครั้งที่ 3 : "))
    return StudentID, StudentName, FirstScore, SecondScore, ThirdScore

def CalAverrage(FirstScore , SecondScore , ThirdScore) :
    Averrages = (FirstScore + SecondScore + ThirdScore) / 3
    return Averrages

def Show(StudentID, StudentName, Averrages) :
    print(f"รหัสนักศึกษา {StudentID} ชื่อนักศึกษา {StudentName}  ค่าเฉลี่ย {Averrages:.2f}")

StudentID,StudentName,FirstScore,SecondScore,ThirdScore = inputCodeIDNameScore()
Averrages = CalAverrage(FirstScore , SecondScore , ThirdScore)
Show(StudentID, StudentName, Averrages)
