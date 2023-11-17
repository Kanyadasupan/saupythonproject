# จงเขียนโปรแกรมPython ของโปรแกรมคำนวณอัตราดอกเบี้ยเงินกู้ โดยรับชื่อผู้กู้ และจำนวนเงินกู้ทางแป้นพิมพ์ และแสดงผลอัตราดอกเบี้ยเงินกู้ที คำนวณได้ทางหน้าจอ ทั้งนี้อัตราดอกเบี้ยคิดจากยอดเงินกู้ หากเงินกู้ตั้งแต่ 1000บาทขึ้นไป คิดอัตราดอกเบี้ยที ร้อยละ 2.5 ของเงินกู้ หากไม่ถึงคิดอัตราดอกเบี้ยที ร้อยละ 5.5 ของเงินกู้

# รับค่าชื่อผู้กู้ และจำนวนเงินกู้
# คำนวนอัตรดอกเบี้ยเงินกู้
# แสดงผล

def inputNameAndMoney() :
    Name = input("ชื่อผู้กู้ : ")
    Money = float(input("จำนวนเงินกู้ : "))
    return Name,Money

def CalInterestRate(Money) :
    if Money > 1000 :
        return Money * (2.5/100)
    else :
        return Money * (5.5/100)
    
def show(Name,Money) :
    print(f"ชื่อผู้กู้ : {Name} อัตราดอกเบี้ยเงินกู้ที่คำนวณได้ : {Money}")

Name,Money = inputNameAndMoney
show(Name,CalInterestRate(Money))



    
    