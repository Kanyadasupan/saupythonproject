# DTIworkshop01.py
# โปรแกรมคำนวณหาพื้นที่สามเหลี่ยม โดยรับค่าฐาน และสูงทางแป้นพิมพ์ และแสดงผลพื้นที่สามเหลี่ยมที่คำนวณได้ทางหน้าจอ

# การวิเคราะห์
# มองหา feature ทางทำงานว่ามีอะไรบ้าง เพื่อ จะไปสร้างเป็น function
# 1.รับค่า ฐาน สูง
# 2.คำนวณพื้นที่ และแสดงผลออกมา

def inputBaseHigh() :
    base = float(input("ป้อนฐาน : "))
    high = float(input("ป้อนสูง :"))
    return base, high

def calAndShowTriangleArea(base, high) :
    area = base * high / 2
    print(f"สามเหลี่ยมฐาน {base:.2f} สูง {high:.2f} มีพื้นที่ {area:.2f}")

print("+++++++++++++++++++++++")
print(" T 3 T calculate Triangle Area T 3 T ")
print("+++++++++++++++++++++++")
base, high = inputBaseHigh()
print("+++++++++++++++++++++++")
calAndShowTriangleArea(base, high)
print("+++++++++++++++++++++++")
