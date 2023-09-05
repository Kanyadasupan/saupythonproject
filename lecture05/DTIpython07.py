#โปรแกรมคำนวณหาพื้นที่วงกลม เส้นรอบวงกลม และปริมาตรทรงกลม จากรัศมีที่ป้อนโดยผู้ใช้ทางแป้นพิมพ์ และแสดงผลพื้นที่ เส้นรอบ และปริมาตรทางหน้าจอ

#ขอ 5 ฟังก์ชัo
import math

#inputRadius
def inputRadius():
    # r = input("ป้อนรัศมี : ")
    # return r
    # r = float(input("ป้อนรัศมี : "))
    # return
    # return input("ป้อนรัศมี : ")
    return float(input("ป้อนรัศมี : "))

#calAreaCircle
def calAreaCircle( r ) :
    #area = math.pi = r ** 2
    #area = math.pi = r * r
    #area = math.pi = math.pow(r,2)
    #return area
    return math.pi * r ** 2

#calRoundCircle
def calRoundCircle( r ):
    return 2 * math.pi * r

#calCubecirle
def calCubecirle( r ) :
    return 4/3 * math.pi * math.pow(r,3)

#showResul ขอทั้งหมดทศนิยม 4 ตำแหน่ง
#พื้นที่วงกลมเป็น ???? เส้นรอบวงเป็น ???? ปริมาตรวงกลมเป็น ????

def showResul( ) :
    r = inputRadius()
    print(f"พื้นที่วงกลม {calAreaCircle(r):.4f} เส้นรอบวง {calRoundCircle(r):.4f} ปริมาตรทรงกลม {calCubecirle(r):.4f} ")

showResul()