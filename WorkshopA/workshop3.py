# 3.จงเขียนโปรแกรมPython ของโปรแกรมคำนวณภาษี ณ ที จ่ายของสินค้า โดยรับชื่อสินค้า และราคาสินค้า ทางแป้นพิมพ์และแสดงผลภาษีที่คำนวณได้ทางหน้าจอ ทั้งนี้ภาษีคิดที ร้อยละ 7 ของราคาสินค้า

# รับค่าชื่อสินค้าและราคาสินค้า
# คำนวนหาภาษี
# แสดงผล

def inputProductNameAndProductPrice() :
    ProductName = input("ชื่อสินค้า : ")
    ProductPrice = float(input("ราคาสินค้า : "))
    return ProductName, ProductPrice

def calTax(ProductName, ProducePrice) :
    Tax = ProducePrice * ( 7 / 100 )
    return Tax

def show(ProductName,ProducePrice,Tax) :
    print(f"ชื่อสินค้า {ProductName} ราคาสินค้า {ProducePrice:.2f} บาท ภาษี {Tax:.2f} บาท")

ProductName , ProductPrice = inputProductNameAndProductPrice()
Tax = calTax(ProductName , ProductPrice)
show(ProductName,ProductPrice,Tax)
