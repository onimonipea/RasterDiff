import numpy as np
from osgeo import gdal
import pandas as pd
import os
import itertools
import time
import scipy
from scipy import stats
import sys

t0=time.time()

# rasterFile = raw_input("Enter raster file name: ")

def importData(rasterFile):
    # Creates object with geotif file
    tif = gdal.Open('%s.tif' % rasterFile)
    # Creates NumPy array from gotif pixel values
    tifArray = np.array(tif.GetRasterBand(1).ReadAsArray())
    # Creates a 'temporary' .csv file to hold NumPy array
    np.savetxt("%s.csv" % rasterFile, tifArray, delimiter=",")
    # Open .csv as pandas dataframe
    tifDf = pd.read_csv("%s.csv" % rasterFile)
    # Delete 'temporary' .csv file
    os.remove('%s.csv' % rasterFile)
    return tifDf
    
# Creates combinations of every x and y coordinate of the df.
def combinations(tifDf):
    tifComb = list(itertools.product(range(tifDf.shape[0]), range(tifDf.shape[1])))
    return tifComb
    
    
# Groups together contiguous pixels (9 per group)
def groups(tifComb, tifDf):
    samples = []
    for x in tifComb:
        r = x[0]
        c = x[1]
        try:
            # Cells, left > right, top > bottom
            q1 = tifDf.iloc[r-1][c-1]
            q2 = tifDf.iloc[r-1][c]
            q3 = tifDf.iloc[r-1][c+1]
            q4 = tifDf.iloc[r][c-1]
            core = tifDf.iloc[r][c]
            q5 = tifDf.iloc[r][c+1]
            q6 = tifDf.iloc[r+1][c-1]
            q7 = tifDf.iloc[r+1][c]
            q8 = tifDf.iloc[r+1][c+1]
        except:
            pass
        # Combine cells into sample list
        sample = [q1, q2, q3, q4, core, q5, q6, q7, q8]
        # Remove blank values from each sample list
        sample = filter(lambda a: a !=-3.4028230607370961e+38, sample)    
        # Create list of sample lists
        samples.append(sample)
    return samples
    
    
# Run a t-test on each group, against the corresponding group in the other samples list
def tTest(samples1, samples2):
    dif = 0
    null = 0
    for x in range(len(samples1)):
        a = samples1[x]
        b = samples2[x]
        t, p = scipy.stats.ttest_ind(a, b)
    
        if p < 0.05:
            dif += 1
        else:
            null += 1
        
    return float(null)/float(dif)


tifDf = importData(sys.argv[1])
tifComb = combinations(tifDf)
samples1 = groups(tifComb, tifDf)

tifDf = importData(sys.argv[2])
tifComb = combinations(tifDf)
samples2 = groups(tifComb, tifDf)

percent = tTest(samples1, samples2)

print percent

t1 = time.time()

total = t1-t0

print total