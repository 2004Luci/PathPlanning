import matplotlib.pyplot as plt
import numpy as np
import math
import pandas as pd
import geopandas
import random

from matplotlib.pyplot import rcParams
np.set_printoptions(precision=3, suppress=True)
rcParams['font.family']='sans-serif'
rcParams['font.sans-serif']=['ALGERIAN']
plt.rcParams['font.size']=14

plt.show()

class NODE():

    def __init__(self,locationX, locationY):
        self.locationX=locationX
        self.locationY=locationY
        self.children=[]
        self.parent=None


class RRTAlgorithm():

    def __init__(self,start,goal,numIterations,grid,stepSize):
        self.randomTree=NODE(start[0],start[1])
        self.goal=NODE(goal[0],goal[1])
        self.nearestNode=None
        self.iterations=min(numIterations,200)
        self.grid=grid
        self.rho=stepSize
        self.path_distance=0
        self.nearestDist=10000
        self.numWaypoints=0
        self.Waypoints=[]

    def addChild(self,locationX,locationY):
        if locationX==self.goal.locationX:
            self.nearestNode.children.append(self.goal)
            self.goal.parent=self.nearestNode
        else:
            temp_Node=NODE(locationX,locationY)
            self.nearestNode.children.append(temp_Node)
            temp_Node.parent=self.nearestNode
            
            

    def sample_point(self):
        x=random.randint(1,grid.shape[1])
        y=random.randint(1,grid.shape[0])
        p=np.array([x,y])
        return p
        

    def steer_to_point(self,locationStart,locationEnd):
        pass

    def is_in_obstacle(self,locationStart,locationEnd):
        pass

    def unit_vector(self,locationStart,locationEnd):
        pass

    def findNearest(self,root,point):
        pass

    def distance(self, node1,point):
        pass

    def goalFound(self,point):
        pass

    def resetNearestValues(self):
        pass

    def retraceRRTPath(self,goal):
        pass


grid=np.load()
start=np.array([100.0,100.0])
goal=np.array([700.0,250.0])
numIterations=200
stepSize=50
goalRegion=plt.Circle((goal[0],goal[1]),stepSize,color='r',fill=False)


fig=plt.figure("RRT Path Planning")
plt.imshow(grid,cmap='binary')
plt.plot(start[0],start[1],'ro')
plt.plot(goal[0],goal[1],'bo')
ax=fig.gca()
ax.add_patch(goalRegion)
plt.xlabel('X-axis $(m)$')
plt.ylabel('Y-axis $(m)$')


























    

    

    











    

    
        



















        
        
        
        
