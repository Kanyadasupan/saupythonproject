# slicing data in List and Tuple
    #   0   1       2       3       4           5
var1 = [10, 20, "Hello" , True, [111,"wow"],"sumsum"]

var2 = (10, 20, "Hello" , True, (111,"wow"),"sumsum")

# 20, "Hello" ,True
print( var1[1:4] )
# True,(111,"wow")
print( var2[3:5])
# 10 , 20 ,"Hello"
print(var1[:3])
# "Hello",True, [111,"wow"] ,"sumsum"
print( var1[2:])
