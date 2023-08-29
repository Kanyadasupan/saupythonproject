width = float(input("ป้อนความกว้าง : "))
long = float(input("ป้อนความยาว : "))
high = float(input("ป้อนความสูง : "))

front_back = float(width * long * 2 )
left_rigth = float(width * high * 2 )
top_bottom = float(width * width * 2 ) 
total_area = float(front_back + left_rigth + top_bottom ) / 5
a = round(total_area)

print("พื้นที่ทั้งหมด",a,"Cm2")




