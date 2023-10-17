emp_name = input("ป้อนชื่อพนักงาน : ")
sale_price = float(input("ป้อนยอดขาย : "))
print ("-------------------")
#ฟังก์ชั่นแปลง string เป็น Number -> int (),foat( )
commission = sale_price * 10/100

Sp = format(float(sale_price),".2f")
Cm = format(float(commission),".2f")
print(f"คุณ {emp_name} ยอดขาย {sale_price:.2f} บาท ได้ค่าคอม {commission:.2f} บาท")
print() #ใช้ ,
print(f"คุณ",(emp_name),"ยอดขาย",Sp,"บาท ได้ค่าคอม",Cm,"บาท")
print() #ใช้ +
print("คุณ"+str(emp_name)+"ยอดขาย"+str(Sp)+"บาท ได้ค่าคอม"+str(Cm)+"บาท")
print() #ใช้ format
print("คุณ {} ยอดขาย {:.2f} บาท ได้ค่าคอม {:.2f} บาท ".format,(emp_name,sale_price,commission))

