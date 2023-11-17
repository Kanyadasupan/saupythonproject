# 1.จงเขียนโปรแกรมPython คำนวณหาราคาขายสินค้า โดยรับชื่อสินค้า และราคาสินค้า(ต้นทุน) ทางแป้นพิมพ์ แล้วคำนวณหาราคาขายของสินค้า โดยราคาขายสินค้าจะคิดเพิ่มจากราคาสินค้า (ต้นทุน) ร้อยละ 10 สูตร ราคาขายสินค้า  =  ราคาสินค้า(ต้นทุน)  + (ราคาสินค้า(ต้นทุน) * 10 / 100)

# รับค่าชื่อสินค้า ราคาสินค้า(ต้นทุน)
# คำนวณหาราคาขายสินค้า
# แสดงผล

def inputPriceAndProduct():
    product = input('ชื่อสินค้า : ')
    price = float(input('ราคาสินค้า : '))
    return product,price

def calPriceProduct(price):
    return price + (price *10/100)
     
def showPriceProduct(product,priceProduct):
    print(f'ชื่อสินค้า {product} ราคาขายสินค้า {priceProduct} ')

product,price = inputPriceAndProduct()
priceProduct = calPriceProduct(price)
showPriceProduct(product,priceProduct)


