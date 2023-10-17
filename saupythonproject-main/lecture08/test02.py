# List มีลำดับ
my_list = [10, 20, 10, "Hi" ,True, [20, "Hello"]]

# Tople มีลำดับ
my_tople = [10, 20, 10, "Hi" ,True, (20, "Hello")]

# set ไม่มีลำดับ
my_set = {10, 20,10,"Hi",True}
                    # key คือ associative คือ ตัวชี้ที่อ้างอิงไปยัง value
                    # value : คือ ค่าข้อมูลที่สามารถเอาไปใช้งาน
# Dictionary --->>>>  Key : Value / Key -> String-Number / Varle-> Everting
my_dict = {"name":"สมชาย","age":20,555:999, "flag":True}
print(my_dict["name"])
print(my_dict["age"] + my_dict[555])
my_dict["name"] = "สมหญิง"
my_dict["major"] = "DTI"
print(my_dict)
my_dict.pop('name')
my_dict.pop(555)
print(my_dict)
my_dict.popitem()

for data in my_dict :
    print(data, end=' ')
 
print()

for data in my_dict.keys() :
    print(data, end=' ')

print()

for data in my_dict.values() :
    print(data, end=' ')

my_dict1 = {"a":10,"b":20,"c":30}
my_dict2 = my_dict1
my_dict3 = my_dict1.copy()

print()
print(my_dict2)
print(my_dict3)
my_dict2["a"] = 999
my_dict3["a"] = 888
print("++++++++++++++++++++++")
print(my_dict1)
print(my_dict2)
print(my_dict3)
