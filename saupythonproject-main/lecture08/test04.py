class Test04 :
    # data/property member
    data1 = 10

    # constuctor
    def __init__(self,data2,data3):
        print("Hi.....")
        self.data2 = data2
        self.data3 = data3

    # method member
    def showSumData(self):
        print(self.data1 + self.data2 + self.data3)
        self.showWow()

    def showWow(self):
        print("Wow Wow Wow.....")

objectA = Test04(20,30)
objectB = Test04(10,20)
objectC = Test04(20,100)
objectD = Test04(20,30)
