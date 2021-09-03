
"""
Created on Wed Sep  1 16:07:35 2021

@author: John Waldo (jw922)
@author: Adam Wolfson (amw337)

HW0

Assumptions: 
    Assuming that the iris data and names are in the current
    directory. If not, please update the main function with
    the proper path.

"""

from matplotlib import pyplot as plt
import math



def getFeaturePairs(data, feature1, feature2):
    '''
    Pulls the two features of interest.
    
    Parameters
    ----------
    Data : Matrix
        Matrix of data.
    feature1 : Int
        Index of first feature
    feature2: Int
        Index of second feature
    

    Returns
    -------
    firstFeatures : All datapoints of first feature
    secondFeatures : All datapoints of second feature
    '''

    firstFeatures = data[feature1]
    secondFeatures = data[feature2]
    

    return [firstFeatures, secondFeatures]


def getPlotDimensions(featureCount):
    '''
    Get optimal dimensions of subplots

    Parameters
    ----------
    featureCount : Int
        The total number of features.

    Returns
    -------
    plotRows : The optimal number of rows
    plotCols : The optimal number of cols

    '''

    totalPlots = (featureCount - 1)*featureCount/2
    
    rootSize = math.sqrt(totalPlots)
    
    lowerBound = math.floor(rootSize)
    upperBound = math.ceil(rootSize)
    
    if lowerBound*upperBound >= totalPlots:
        plotRows = lowerBound
        plotCols = upperBound
    else:
        plotRows = upperBound
        plotCols = upperBound

    
    
    return [plotRows, plotCols]



class IrisPlotter(object):
    """
    Class that handles visualization of iris data
    """

    def __init__(self, datasource, namesource):

        self.datasource = datasource
        self.namesource = namesource

    def main(self):
        ''' 
        Main function for this class.
        Manages pulling, parsing, and plotting the data
        '''

        irisData = self.pullData(self.datasource)
        
        # irisNames = pullNames(self.namesource)
        # HARD CODED NAMES:
        irisNames = ['sepal length', 'sepal width', 'petal length', 'petal width']
        

        self.plotPairwiseData(irisData, irisNames)

    def pullData(self,source):
        '''
        Load the raw data from the given path
        as a dictionary ordered by Iris type
        
        Parameters
        ----------
        source : String
            Path to data file
        
        Returns
        -------
        irisData : Dictionary
            Dictionary with iris type as key.
            Values are the feature data for
            instances of the given type.
        '''
    
        irisData = {}
        
        for line in open(source):
            details = line[:-2].split(",")
            if len(details) > 1:
                flower = details[-1]
                data = details[:-1]
                
                if flower not in irisData:
                    irisData[flower] = []
    
                    for d in range(len(data)):
                        irisData[flower].append([])
                        
                for d in range(len(data)):
                    irisData[flower][d].append(float(data[d]))
    
        return irisData

    def plotPairwiseData(self, data, featNames):
        
        '''
        Plots the feature data in pairs.
        
        Parameters
        ----------
        data : Dictionary
            Dictionary with iris type as key.
            Values are the feature data for instances of the given type.
            
        featNames : List
            List of feature names
            
        Returns
        -------
        None
        
        '''
        
        flowers = list(data.keys())        

        totalFeatures = len(data[flowers[0]])


        [rows, cols] = getPlotDimensions(totalFeatures)

        fig, axes = plt.subplots(rows, cols)
        

        for feat in range(len(flowers)):
            flower = flowers[feat]

            plotNumber = [0,0]
            
            for f1 in range(totalFeatures):
                for f2 in range(f1):
                    [firstFeatures, secondFeatures] = getFeaturePairs(data[flower], f1, f2)
    
                    axes[plotNumber[0],plotNumber[1]].scatter(firstFeatures,
                                                              secondFeatures,
                                                              label = flower)
      
                    
                    axes[plotNumber[0],plotNumber[1]].set_xlabel(featNames[f1])
                    axes[plotNumber[0],plotNumber[1]].set_ylabel(featNames[f2])
    
    
                    plotNumber[1] += 1
    
                    if plotNumber[1] >= cols:
                        plotNumber[0] += 1
                        plotNumber[1] = 0
                        
        fig.suptitle("Iris Data")
        fig.tight_layout()
        plt.legend(bbox_to_anchor=(0, -0.35, 1, 0), mode="expand", borderaxespad=0)

        plt.show()


if __name__ == "__main__":
    source = './iris.data'
    names = './iris.names'
    irisObj = IrisPlotter(source, names)
    irisObj.main()