import math
pi = 3.1415
for i in range(0, 360 ,15):
    print (i,"---", round (math.sin(i*(pi/180)),4), round(math.cos(i*(pi/180)),4))
    

