# List มีลำดับ
my_list = [10, 20, 10, "Hi" ,True, [20, "Hello"]]
print(my_list)
print(len(my_list))

# Tople มีลำดับ
my_tople = [10, 20, 10, "Hi" ,True, (20, "Hello")]
print(my_tople)
print(len(my_tople))
# set ไม่มีลำดับ
my_set = {10, 20,10,"Hi",True}
print(my_set)
print(len(my_set))

for data in my_set :
    print(data,end='/')

print("++++++++++++++++++++++++++")

list_fr_set = list( my_set )
print(list_fr_set)
list_fr_set[0] = "DTI"
my_set = set(list_fr_set)
print(my_set)
my_set.clear()
print(len(my_set))

my_set1 = {10,20,30,"Hi",True}
my_set2 = {10,"Hello","Hi",True}

my_set.add(999)
print(my_set1)
my_set1.remove("Hi")
print(my_set1)

print(my_set1.intersection(my_set2))
print(my_set1.union(my_set2))

# len , min , max
print(min(my_set))

