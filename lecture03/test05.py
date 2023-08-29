celsius = float(input("อุณหภูมิ C: "))
fahrenheit = 9/5* celsius + 32

c = format(float(celsius), ".2f")
f = format(float(fahrenheit), ".2f")

print("อุณหภูมิ", c , "celsius" , "แปลงอุณหภูมิ" , f , "fahrenheit")
print("อุณหภูมิ" + " " + c + " " + "celsius" + " " + "แปลงอุณหภูมิ" + " " + f + " " + "fahrenheit")
print("อุณหภูมิ {:.2f} celsius แปลงอุณหภูมิ {:.2f} fahrenheit ".format(celsius,fahrenheit))
print(f"อุณหภูมิ {celsius:.2f} celsius แปลงอุณหภูมิ {fahrenheit:.2f} fahrenheit")





