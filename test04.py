people = int(input("จำนวนคน : "))
money = float(input("จำนวนเงิน : "))
divided = float(money / people)
d = format(float(divided), ".2f")

print("หารกันคนละ" , d , "บาท")
print("หารกันคนละ" + " " + str(d) + " " + "บาท")
print("หารกันคนละ {:.2f} บาท".format(divided))
print(f"หารกันคนละ {divided:.2f} บาท ")


