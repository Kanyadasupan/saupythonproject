#คำสั่ง return ที่ไม่มีอะไรต่อท้าย หมายถึง เป็นการบ่งบอกว่าการทำงานนั้นๆ ว่าเสร็จแล้ว
def example1() :
    print(111)
    print(222)
    return
    print(3333)
    print(4444)
    return

# Default parameter
def dtiTest( x, y, z, a):
    print(f"{x} + {y} + {z} + {a} = {x+y+z+a}")


dtiTest(5, 100)

dtiTest(9, 8, 10)
