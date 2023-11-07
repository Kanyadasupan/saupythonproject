# เขียนข้อมูลลงไฟล์
# เปิดไฟล์เพื่อเขียนข้อมูลลงไฟล์
f_dti = open('myfile01.txt','a', encoding='utf-8') # เปิดไฟล์เพื่อเขียนข้อมูลลงไฟล์

f_dti.write('cccccc')
f_dti.write('DDDDDD\n')


f_dti.close()

print('บันทึกข้อมูลลงไฟล์เรียบร้อยแล้ว')