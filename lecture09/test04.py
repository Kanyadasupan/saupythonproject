# คุณสมบัติเด่น Encapsulation (ห่อหุ้ม)
class DtiTest05 :
    # data
    infoA = 10 #ไม่ได้ห่อหุ้ม
    __infoB = 20 # ห่อหุ้ม

    def __init__(self, infoC, infoD) :
        self.infoC = infoC          # ไม่ได้ Encap
        self.__infoD = infoD        # Encap ดูจาก__???? -> เป็นการกำหนด access_modifier เป็น privace

    # เมื่อใดก็ตาม Encap จะต้องมีเมทตอด 2 ตัวนี้เสมอ คือ get , set ของ data ตัวนั้น
    def setInfoB(self, infoB) : # กำหนดค่าให้กับ data
        self.__infoB = infoB

    def getInfoB(self) : # เอาค่า data ไปใช้
        return self.__infoB
    
    def setInfoB(self, infoD) :
        self.__infoD = infoD

    def getInfoB(self) :
        return self.__infoD
    
    def showInfo(self) :
        print(self.infoA, end='')
        print(self.__infoBinfoB, end='')
        print(self.infoC, end='')
        print(self.__infoD)
        print('.......................')


ob1 = DtiTest05(30, 40)
ob2 = DtiTest05(30, 100)
ob1.showInfo() # 10 20 30 40 
ob1.infoA = 555
# ob1.__infoB = 999 # ไม่เปลี่ยนค่าเพราะ มันถูก Encap
ob1.setInfoB(999)
ob1.showInfo() # 555 999 30 40
# print(ob1.__infoB + ob1.__infoD) มันถูก Encap ถ้าจะเอาค่าที่เก็บมาใช้งานต้องมาเมธอด get
print(ob1.getInfoB() + ob1.getInfoD())


