import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.pylab as pylab


"""
Function sets each cluster center to the average X and Y of the points in its cluster
"""
def updateClusterCenterPositions(dataset, clusterDF, column1, column2): #in jupyter this seems to fail
    #now for each cluster calculate a new X and Y based on the points in the cluster
    clusterDF.loc[1]["CX"] = dataset.loc[dataset['cluster'] == "C1"][column1].mean()
    clusterDF.loc[1]["CY"] = dataset.loc[dataset['cluster'] == "C1"][column2].mean()
    
    clusterDF.loc[2]["CX"] = dataset.loc[dataset['cluster'] == "C2"][column1].mean()
    clusterDF.loc[2]["CY"] = dataset.loc[dataset['cluster'] == "C2"][column2].mean()
    
    clusterDF.loc[3]["CX"] = dataset.loc[dataset['cluster'] == "C3"][column1].mean()
    clusterDF.loc[3]["CY"] = dataset.loc[dataset['cluster'] == "C3"][column2].mean()
    
    
"""
Function plots the data and clusters on a chart and colours them
"""
def plotClusters(dataset, clusterDF, column1, column2):
    #plot first cluster and cluster centre
    plt.scatter(dataset.loc[dataset['cluster'] == "C1"][column1], dataset.loc[dataset['cluster'] == "C1"][column2], color="red")
    plt.scatter(clusterDF.loc[clusterDF['Name'] == "C1"]['CX'], clusterDF.loc[clusterDF['Name'] == "C1"]["CY"], color='black', marker='+', s=100)
    #plot second cluster and cluster centre    
    plt.scatter(dataset.loc[dataset['cluster'] == "C2"][column1], dataset.loc[dataset['cluster'] == "C2"][column2], color="green")
    plt.scatter(clusterDF.loc[clusterDF['Name'] == "C2"]['CX'], clusterDF.loc[clusterDF['Name'] == "C2"]["CY"], color='black', marker='*', s=100)
    #plot third cluster and cluster centre    
    plt.scatter(dataset.loc[dataset['cluster'] == "C3"][column1], dataset.loc[dataset['cluster'] == "C3"][column2], color="blue")
    plt.scatter(clusterDF.loc[clusterDF['Name'] == "C3"]['CX'], clusterDF.loc[clusterDF['Name'] == "C3"]["CY"], color='black', marker='^', s=100)
   

"""
Sets the initial cluster centers to random points within the dataset
"""
def createRandomClusterCenters(dataset, range1, range2, clusters=3):
    #create a list to store the cluster centers
    clusterDF = pd.DataFrame(columns=["Name", "CX", "CY"])
    #manually create some clusters and store them in the list
    clusterDF.loc[1] = ["C1", dataset[range1].iloc[7], dataset[range2].iloc[5]]
    clusterDF.loc[2] = ["C2", dataset[range1].iloc[10], dataset[range2].iloc[15]]
    clusterDF.loc[3] = ["C3", dataset[range1].iloc[15], dataset[range2].iloc[20]]
    return clusterDF


"""
Runs whatever function is passed to it to assign each cluster a new center
"""
def assignToNewCluster(dataset, test):
    dataset['cluster'] = dataset.apply(lambda datapoint: test(datapoint), axis=1)

    
if __name__ == "__main__":
    print("do not run directly")