class DtiTest01 :
    pass

class DtiTest02 :
    # Data/attibute/property/field คือ ตัวแปลประเภทหนึ่ง
    infoA = ''
    infoB = 10

    # method คือ ฟังก์ชันประเภทหนึ่ง
    def showHi(self) :
        print("Hi")

    def showInfoAandB(self) :
        print(self.infoA)
        print(self.infoB)

# สร้าง object
objA = DtiTest02()
objB = DtiTest02()
sombat = DtiTest02()

objA.infoA = 'xxxx'
objB.infoB = 100
print(objA.infoB + objB.infoB)
sombat.showInfoAandB()
