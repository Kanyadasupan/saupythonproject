#Function 2 : have parameter/no return
#parameter คื ตัวแปร (variable) ประเภทหนึ่ง
def funcA(x,y) :
    print("AAA")
    z = x+y
    print(f'{x} + {y} = {z}')
    #ไม่มีคำสั่ง return

def funcB(x,y,z) :
    print("{:.2f} {:.4f} {:.5f}".format(x,y,z))

funcA(10,20) #ข้อมูลที่ส่งให้ parameter เรียก argument
funcA(5,10)
funcB(1,5,10)

