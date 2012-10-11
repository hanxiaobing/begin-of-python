#i = 0
#numbers = []

#while i<6:
#    print ("At the top i is %d" % i)
#    numbers.append(i)
#
#    i +=1
#    print ("Numbers now:" ,numbers)
#    print ("At the bottom i is %d"%i)


print ("The numbers:")
def adding(n):
    i =0
    numbers=[]
    while i<n:
        print ("At the top i is %d" % i)
        numbers.append(i)

        i +=1
        print ("Numbers now:" ,numbers)
        print ("At the bottom i is %d"%i)        
    return numbers
#注意函数内部变量与全局变量的区别
numbers=adding(14)
print(numbers)
for num in numbers:
    print ( num)
