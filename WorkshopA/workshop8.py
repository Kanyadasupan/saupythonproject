# จงเขียนโปรแกรม Python ของโปรแกรทตรวจสอบค่า PH ของน้ำปะปาจากจังหวัดต่างๆโดยรับชื่อจังหวัด และค่า PH ทางแป้นพิมพ์ และแสดงผลทางหน้าจอโดยหาค่า PH เป็น 7-8 แสดงข้อความ "Result is Nomal" หากค่า PH มากกว่า 8 ให้แสดงข้อความ "Result is Acid" หากค่า PH น้อยกว่า 7 ให้แสดงข้อความ "Result is Alkali"
# รับค่าชื่อจังหวัดและค่าPH
# ตรวจสอบค่า PH 
# แสดงผล

def inputPh():
    province = input('จังหวัด : ')
    ph = int(input('ค่า PH : '))
    return province,ph

def checkPh(ph):
    if ph == 7 or ph == 8:
        return 'Result is Normal'
    elif ph > 8:
        return  'Result is Acid'
    else:
        return 'Result is Alkali'

def showPh(province,ph):
    print(f'จังหวัด : {province} ค่า PH : {ph}')

province,ph = inputPh()
showPh(province,checkPh(ph))