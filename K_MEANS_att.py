from numpy import genfromtxt
from scipy import linalg
import matplotlib.pyplot as plt
import random
import math
import collections

#check wheather old and new centroids are same or not
def converged(centre_xx,centre_yy,new_centre_xx,new_centre_yy):
    compare = lambda x, y: collections.Counter(x) == collections.Counter(y)
    if compare(centre_xx,new_centre_xx) and compare(centre_yy,new_centre_yy):
        return True
    else:
        return False
        
#get the x part of the centroid        
def findCentroid_x(cluster,x,y):
    x_point=0
    #y_point=0
    for i in range(len(cluster)):
        p=0
        p=cluster[i]
        x_point= x_point + x[p]
        #y_point= y_point + y[p]
    x_point=x_point/len(cluster)
    #y_point=y_point/len(cluster)
    return x_point
    
#get the y part of the centroid
def findCentroid_y(cluster,x,y):
    #x_point=0
    y_point=0
    for i in range(len(cluster)):
        p=0
        p=cluster[i]
        #x_point= x_point + x[p]
        y_point= y_point + y[p]
    #x_point=x_point/len(cluster)
    y_point=y_point/len(cluster)
    return y_point
    
#get the distance between two points
def getDistance(centre_x1,centre_y1,x1,y1):
    distances = 0
    distances = pow((centre_x1 - x1), 2) + pow((centre_y1 - y1), 2)
    return math.sqrt(distances)
    
def kmeans(k,x,y):
    c_index=0
    centre_x=[]
    centre_y=[]
    
    new_centre_x=[]
    new_centre_y=[]
    #Rendomly assign the centroids
    #for i in range(k):
     #   c_index=random.randint(0, 149)
        #print c_index
        #print x[c_index]
    centre_x.append(x[1])
    centre_y.append(y[1])
    centre_x.append(x[11])
    centre_y.append(y[11])
    centre_x.append(x[21])
    centre_y.append(y[21])    
    iter=0
    #if old centroid and new centroid are not equal assign points to the nearest centroid cluster.
    while not(converged(centre_x,centre_y,new_centre_x,new_centre_y)):  
        iter+=1
        cluster0=[]
        cluster1=[]
        cluster2=[] 
        #print new_centre_x
        if new_centre_x:
            for i in range(k):
                centre_x[i]=new_centre_x[i]
                centre_y[i]=new_centre_y[i]
            new_centre_x=[]
            new_centre_y=[]
        #get distance of all points to all centroids and assign the minimum distance points to centroid. 
        for j in range(len(x)):
            distance=[]
            for i in range(k):      
                distance.append(getDistance(centre_x[i],centre_y[i],x[j],y[j]))  
            if distance.index(min(distance))==0:
                cluster0.append(j)
            elif distance.index(min(distance))==1:
                cluster1.append(j)
            else:
                cluster2.append(j)
        #find new cetroid after assigning them to nearest centroid points.
        new_centre_x.append(findCentroid_x(cluster0,x,y))
        new_centre_y.append(findCentroid_y(cluster0,x,y))
        new_centre_x.append(findCentroid_x(cluster1,x,y))
        new_centre_y.append(findCentroid_y(cluster1,x,y))
        new_centre_x.append(findCentroid_x(cluster2,x,y))
        new_centre_y.append(findCentroid_y(cluster2,x,y))
    print "Number of iterations needed starting with 0 = "+str(iter)  
    return cluster0,cluster1,cluster2,new_centre_x,new_centre_y
    
def main():
    #Read the data from the data file
    array_data =genfromtxt("D:\\UTA\\5334\\Proj 2\\att.csv",delimiter=",")
    U,s,Vt = linalg.svd(array_data,full_matrices=False)
    x=[]
    y=[]
    data_class=[]
    c0=[]#Cluster 1 list
    c1=[]#Cluster 2 list
    c2=[]#Cluster 3 list
    cen1=[]
    cen2=[]
    count=0
    #print array_data[0][1]
    #get the data of first two columns of U in x and y respectively
    for i in range(len(array_data)):
        data_class.append(array_data[i][644])
        x.append(U[i][0])
        y.append(U[i][1])

    k=3
    #call KMEANS function
    c0,c1,c2,cen1,cen2=kmeans(k,x,y)
    #plot the data with class 1 with RED "+" sign, class 2 with BLUE "*" sign, class 3 with BLUE "." sign
    for i in range(len(array_data)):
        if i in c0:
            plt.scatter(x[i], y[i], marker='+',c='r')
            if data_class[i]==1:
                count+=1
        elif i in c1:
            plt.scatter(x[i], y[i], marker='*',c='b')
            if data_class[i]==2:
                count+=1
        else:
            plt.scatter(x[i], y[i], marker='.',c='b')
            if data_class[i]==3:
                count+=1
    print "Accuracy = " +str((count/float(len(array_data))*100.0))+"%"

    #plot centroids with Yellow SQUARE in the graph
    plt.scatter(cen1[0],cen2[0],marker='s',c='y')
    plt.scatter(cen1[1],cen2[1],marker='s',c='y')
    plt.scatter(cen1[2],cen2[2],marker='s',c='y')
    
    plt.axis([-0.23, -0.14, -0.32, 0.18])
    plt.show()   
        
    
main()
    