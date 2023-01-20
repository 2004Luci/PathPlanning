import numpy
import random
import math
import cv2
import matplotlib.pyplot as plt
import pandas as pd
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon

point=Point(300,200)
polygon1=Polygon([(250,70),(250,440),(440,440),(440,70)])
#polygon2=Polygon([(),()]
print(polygon1.contains(point))


XDIM=600
YDIM=600
STEP=10


class NODE(object):

    def __init__(self,point,upper):
        super(NODE, self).__init__()
        self.point=point
        self.upper=upper

def randomization(length,minimum,maximum):
    return [random.uniform(minimum,maximum) for i in range(length)]

#-----------------------------------------------------------------------

def distance(sp,gp):
    return (math.pow(gp[0]-sp[0],2)+ math.pow(gp[1]-sp[1],2))**0.5

L=['X','Y']        
sp=[]    #sp = start_pose
gp=[]     #gp = goal_pose
for i in range(len(L)):
    print('Enter',L[i],'coordinate for start point:-')
    a=int(input())
    sp.append(a)

for j in range(len(L)):
    print('Enter',L[j],'coordinate for goal point:-')
    b=int(input())
    gp.append(b)

print('Entered Coordinates:-')
print('Start Pose:',tuple(sp))
print('Goal Pose:',tuple(gp))

#-----------------------------------------------------------------------
rp=[0,0]
def step_from_to(sp,rp):      #rp= Random Point
    if distance(sp,rp)<STEP:
        return rp
    else:
        u_vector=[(rp[0]-sp[0])/distance(sp,rp),(rp[1]-sp[1])/distance(sp,rp)]
        return [sp[0]+(u_vector[0]*STEP),sp[1]+(u_vector[1]*STEP)]
print(step_from_to(sp,rp))

cv2.namedWindow("RRT Path Planning")

window=numpy.zeros((YDIM,XDIM,3),dtype='uint8')
cv2.circle(window, sp, 5, (0,255,0), -1)
cv2.circle(window, gp, 5, (0,0,255), -1)
cv2.rectangle(window,(250,70),(440,440),(0,255),-1)







        
        
    
