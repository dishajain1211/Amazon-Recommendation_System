import numpy as numpy
import scipy as scipy
from sklearn import cluster
import matplotlib.pyplot as plt

from sklearn.cluster import DBSCAN
from sklearn import metrics
from sklearn.datasets.samples_generator import make_blobs
from sklearn.preprocessing import StandardScaler
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.metrics import adjusted_rand_score
import numpy
from sklearn.cluster import DBSCAN
from sklearn.decomposition import TruncatedSVD
import itertools
import matplotlib.pyplot as plt




def set2List(NumpyArray):
    list = []
    for item in NumpyArray:
        list.append(item.tolist())
    return list


def GenerateData(Data):
    Data = TruncatedSVD(n_components=2).fit_transform(Data)
    print(Data.shape)
    noise=scipy.rand(50,2)*20 -3

    Noisy_Data=numpy.concatenate((Data,noise))
    size=20


    fig = plt.figure()
    ax1=fig.add_subplot(2,1,1) #row, column, figure number
    ax2 = fig.add_subplot(212)

    ax1.scatter(Data[:,0],Data[:,1], alpha =  0.5 )
    #ax1.scatter(noise[:,0],noise[:,1],color='red' ,alpha =  0.5)
    #ax2.scatter(noise[:,0],noise[:,1],color='red' ,alpha =  0.5)


    Epsilon=1
    MinumumPoints=20
    result , distance =DBSCAN(Data,Epsilon,MinumumPoints)

    #printed numbers are cluster numbers
    print (result)
    for i in range(len(result)):
        ax2.scatter(Noisy_Data[i][0],Noisy_Data[i][1],color='yellow' ,alpha =  0.5)
        
    plt.show()
    return(distance)



def DBSCAN(Dataset, Epsilon,MinumumPoints,DistanceMethod = 'euclidean'):
##    Dataset is a mxn matrix, m is number of item and n is the dimension of data
    m,n=Dataset.shape
    Visited=numpy.zeros(m,'int')
    Type=numpy.zeros(m)
    ClustersList=[]
    Cluster=[]
    PointClusterNumber=numpy.zeros(m)
    PointClusterNumberIndex=1
    PointNeighbors=[]
    DistanceMatrix = scipy.spatial.distance.squareform(scipy.spatial.distance.pdist(Dataset, DistanceMethod))
    for i in range(m):
        if Visited[i]==0:
            Visited[i]=1
            PointNeighbors=numpy.where(DistanceMatrix[i]<Epsilon)[0]
            if len(PointNeighbors)<MinumumPoints:
                Type[i]=-1
            else:
                for k in range(len(Cluster)):
                    Cluster.pop()
                Cluster.append(i)
                PointClusterNumber[i]=PointClusterNumberIndex
                
                
                PointNeighbors=set2List(PointNeighbors)    
                ExpandClsuter(Dataset[i], PointNeighbors,Cluster,MinumumPoints,Epsilon,Visited,DistanceMatrix,PointClusterNumber,PointClusterNumberIndex  )
                Cluster.append(PointNeighbors[:])
                ClustersList.append(Cluster[:])
                PointClusterNumberIndex=PointClusterNumberIndex+1

    #print(DistanceMatrix)

    return (PointClusterNumber ,DistanceMatrix)



def ExpandClsuter(PointToExapnd, PointNeighbors,Cluster,MinumumPoints,Epsilon,Visited,DistanceMatrix,PointClusterNumber,PointClusterNumberIndex  ):
    Neighbors=[]

    for i in PointNeighbors:
        if Visited[i]==0:
            Visited[i]=1
            Neighbors=numpy.where(DistanceMatrix[i]<Epsilon)[0]
            if len(Neighbors)>=MinumumPoints:
            ##  Neighbors merge with PointNeighbors
                for j in Neighbors:
                    try:
                        PointNeighbors.index(j)
                    except ValueError:
                        PointNeighbors.append(j)
                    
        if PointClusterNumber[i]==0:
            Cluster.append(i)
            PointClusterNumber[i]=PointClusterNumberIndex
    return
