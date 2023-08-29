product_Name = input("ป้อนชื่อสินค้า : ")
product_price = float(input("ราคาสินค้า(ต้นทุน) : "))
selling_price = product_price + product_price * 10/100

Pdp = format(float(product_price),".2f")
sp = format(float(selling_price),".2f")

print(f"ราคาขายสินค้า",(product_Name),"ราคา",sp,"บาท")

