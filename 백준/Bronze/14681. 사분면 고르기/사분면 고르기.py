x = int(input())
y = int(input())

if((-1000 <= x <= 1000 )&( -1000 <= y <= 1000)):
    if( x > 0 and y > 0 ):
        print(1)
    elif(x < 0 and y > 0):
        print(2)
    elif(x < 0 and y < 0):
        print(3)
    elif(x > 0 and y < 0):
        print(4)