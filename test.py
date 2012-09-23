# import math
for n in range(100,1000):
    if n%10==9:
        if n%9==8:
            if n%8==7:
                print ( n )
    n=n+1
next

m = 1
while m%7!= 6 or m%5!= 4 or m%4!= 3:
        m=m+1
else :
    print (m)

class Bird(object):
    have_feather = True
    way_of_reproduction = 'egg'
    def move(self, dx, dy):
        position = [0,0]
        position[0] = position[0] + dx
        position[1] = position[1] + dy
        return position

summer = Bird()
print ('after move:',summer.move(5,8))
