# 4.จงเขียนโปรแกรมPython ของโปรแกรมแก้สมการ y = 2x^2 + 2x + 1 เมื่อ x คือค่าที่รับทางแป้นพิมพ์ และแสดงผลจากการแก้สมการy ที ได้ทางหน้าจอ

# รับค่า x
# แก้สมการy 
# แสดงผล

def inputEquation() :
    X = float(input("ค่า x : "))
    return X

def CalEquation(X) :
    y = 2*(X**2) + (2*X)+1
    return y

def show(X,y) :
    print(f"x = {X:.2f} ดังนั้นสมการ y = 2x^2 + 2x + 1 = {y:.2f}")

x = inputEquation()
y = CalEquation(x)
show (x,y)


