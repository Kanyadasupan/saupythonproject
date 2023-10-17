#คำณวนเงินที่จะแชร์กัน ป้อนเงิน ป้อนคน และ แสดงเงิน ที่จะแชร์กันทางหน้าจอ
#โดยให้เขียนเป็นฟังก์ชัน ขอ 2 ฟังก์ชัน

#cast/conversion
#รับค่าข้อมูล
def inputMoneyPerson( ) :
    money = float( input("ป้อนเงิน : "))
    person = int( input("ป้อนจำนวนคน : "))
    return money,person

#คำนวณ แล้วแสดงผลออกมา
def calAndShow( money, person ) :
    #เงิน ขอทศนิยม 2 ตำแหน่ง แชร์กันชอเป็นเลขจำนวนเต็มปัดขึ้น
    print(f"จำนวนเงิน {money:.2f} บาท คน {person} คน แชร์กันคนละ {round(money/person)} บาท") 
    print("จำนวนเงิน" , "%.2f" % money, "บาท" "คน" ,person, "คน" "แชร์กันคนละ" ,round(money/person), "บาท")
    print("จำนวนเงิน" + " "+ str("%.2f" % money) +" " + "บาท" + "คน" + " " + str(person) + " " + "คน" + "แชร์กันคนละ" +" " + str(round(money/person)) + " " + "บาท")
    print("จำนวนเงิน {:.2f} บาท คน {} คน แชร์กันคนนละ {}".format( money,person,round(money/person)))
    print("จำนวนเงิน %s บาท คน %s คน แชร์กันคนละ %s บาท" % ("%.2f" % money, person,round(money/person)))


money, person = inputMoneyPerson( )

calAndShow(money, person)

