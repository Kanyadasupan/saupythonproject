# 2.จงเขียนโปรแกรมPython ของโปรแกรมคำนวณหาค่าเฉลี่ยของคะแนนจากการสอบ 3 ครั้ง โดยรับค่า รหัสนักเรียน ชื่อนักเรียน และคะแนนสอบแต่ละครั้งรวม 3 ครั้งทางแป้นพิมพ์ แล้วแสดงผลค่าเฉลี่ยที คำนวณได้ทางหน้าจอ

# รับค่า รหัสนักศึกษา ชื่อนักเรียน และ คะแนนสอบ 3 ครั้ง
# คำนวนหาค่าเฉลี่ยและแสดงผล

def inputCodeIDNameScore() :
    StudentID = input("รหัสนักศึกษา : ")
    StudentName = input("ชื่อนักศึกษา : ")
    FirstScore = float(input("คะแนนสอบครั้งที่ 1 : "))
    SecondScore = float(input("คะแนนสอบครั้งที่ 2 : "))
    ThirdScore = float(input("คะแนนสอบครั้งที่ 3 : "))
    return StudentID, StudentName, FirstScore, SecondScore, ThirdScore

def CalAverrage(StudentID, StudentName, FirstScore , SecondScore , ThirdScore) :
    Averrage = (FirstScore + SecondScore + ThirdScore) / 3
    print(f"รหัสนักศึกษา {StudentID} ชื่อนักศึกษา {StudentName} คะแนนครั้งที่ 1 {FirstScore:.2f} คะแนน คะแนนครั้งที่ 2 {SecondScore:.2f} คะแนน คะแนนครั้งที่ 3 {ThirdScore:.2f} คะแนน ค่าเฉลี่ย {Averrage:.2f}")

StudentID , StudenName , FirstScore , SecondScor , ThirdScore = inputCodeIDNameScore()
CalAverrage(StudentID, StudenName, FirstScore , SecondScor , ThirdScore)

