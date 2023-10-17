# 1.จงเขียนโปรแกรมPython คำนวณหาราคาขายสินค้า โดยรับชื่อสินค้า และราคาสินค้า(ต้นทุน) ทางแป้นพิมพ์ แล้วคำนวณหาราคาขายของสินค้า โดยราคาขายสินค้าจะคิดเพิ่มจากราคาสินค้า (ต้นทุน) ร้อยละ 10 สูตร ราคาขายสินค้า  =  ราคาสินค้า(ต้นทุน)  + (ราคาสินค้า(ต้นทุน) * 10 / 100)

# รับค่าชื่อสินค้า ราคาสินค้า(ต้นทุน)
# คำนวณหาราคาขายสินนค้าและแสดงผล

def inputProductSellingPrice() :
    ProductName = input("ชื่อสินค้า : ")
    ProductCostPrice = float(input("ราคาสินค้า(ต้นทุน) : "))
    return ProductName , ProductCostPrice

def CalSellingPriceProduct(ProductName , ProductCostPrice) :
    SellingPriceProduct = ProductCostPrice + ProductCostPrice * 10 / 100
    print(f"ชื่อสินค้า {ProductName} ราคาสินค้า {ProductCostPrice:.2f} บาท ราคาขายสินค้า {SellingPriceProduct:.2f} บาท")

ProductName , ProductCostPrice = inputProductSellingPrice()
CalSellingPriceProduct(ProductName , ProductCostPrice)

