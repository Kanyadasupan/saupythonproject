#function แบบที่ 2 - Have parameter/No return
#paramrters คือ เป็นตัวแปรประเภทหนึ่ง เอาไว้รับค่ามาใช้เฉพาะในฟังก์ชั่นนั้นๆ เท่านั้น

def funcA( x , y ) : 
    print(f'X is {x}')
    print(f'Y is {y}')
    print(f'sum {x} + {y} = {x+y}')

funcA(10,20) #call function ข้อมูลที่ส่งให้ parameter เรียกว่า argument อาร์กิวเมนต์
funcA(1,4)
print("DTI........")
funcA(5,5)