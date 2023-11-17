# จงเขียนโปรแกรม Python ของโปรแกรม Game Binggo โดยให้ผู้ใช้ป้อนตัวเลขที่ต้องการทายทางแป้นพิมพ์แล้วให้โปรแกรมตรวจสอบว่าตรงกับที่โปรแกรมกำหนดไว้หรือไม่ในที่นี้คือ 25 หากไม่แสดงข้อความว่า "Not Correct!!!" ทางหน้าจอ หากตรงให้แสดงข้อความว่า "Correct,You are the winner"
# รับค่าตัวเลข
# ตรวจสอบตัวเลข
# แสดงผล

def inputNumber():
    number = int(input('ป้อนตัวเลข : '))
    return number

def checkNumber(number):
    if number == 25:
        print('Correct,You are the winner')
    else:
        print('Not Correct !!!!')    
            
def show(answer):
    return answer

numScore = inputNumber()
answer = checkNumber(numScore)
show(answer)
