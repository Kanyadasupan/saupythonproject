#Function 1 : no parameter/no return
def funcA( ) : 
    print("AAA")
    #ไม่ควรเรียกฟังก์ชันกันไปมา
    print("BBB")
    #ไม่มีคำสั่ง return


def funcB( ) :
    print("111")
    funcA( ) #ไม่ควรเรียกฟังก์ชันกันไปมา
    

funcA( )
funcA( )
funcB( )
funcB( )
