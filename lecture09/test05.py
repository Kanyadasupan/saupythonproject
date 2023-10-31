#  คุณสมบัติ Inherritance สืบทอด คือ การที่คลาสหนึ่ง สืบทอดอีกคลาสหนึ่ง *** (re-use)
# สืบทอด มีแม่(Super class) มีลูก(Sub class)
# แม่มีอะไร ลูกมีด้วย เมื่อมีการสืบทอด (Inherritance)

# คุณสมบัติเด่า Polymorephism (พ้องรูป:พฤติกรรมเดียวแต่วิธีการต่างกัน) คือ การที่คลาสลูก เอาเมธอดคลาสแม่มาเขียนใหม่

class Sau01 :
    infoA = 10

    def showHi() :
        print('Hi.........')

class Sau02(Sau01) : #Inherritance
    infoB = 20

    def showHey() :
        print('Hey........')

    # Overiding method : Polymorephism
    def showHi() :
        print('Hi Hi Hi.........')

ob1 = Sau01()
ob2 = Sau02()
ob2.showHi()

