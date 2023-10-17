# คำสั่ง if-else-if

scor = int(input("ป้อนคะแนน : "))

if scor >= 80 :
    print("ได้เกรด A")
elif scor >= 70 and scor < 80 :
    print("ได้เกรด B")
elif scor >= 60 and scor < 70 :
    print("ได้เกรด C")
elif scor >= 50 and scor < 60 :
    print("ได้เกรด D")
# elif scor < 50 : หรือ 
else :
    print("ได้เกรด F")

print("______________")
print("created by DTI-SAU")