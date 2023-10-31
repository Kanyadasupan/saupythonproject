# Destructor

class DtiTest04 :
    data1 = 10

    def __init__(self, data2) :
        self.data2 = data2
        print('Hi........')

    def doTask1(self) :
        print('^_^')

    def dotask2(self, value) :
        print(value)

    # destructor
    def __del__(self) :
        print('Bye Bye.......')

def show() :
    print('Hey.........')
# .........................................................

sauA = DtiTest04(20)
sauB = DtiTest04(30)
sauC = DtiTest04(20)

sauC.dotask2('T_T') # T_T
sauC.doTask1() # ^_^
print(sauA.data1 + sauB.data1) # 20
                                              
