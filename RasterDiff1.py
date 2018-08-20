import numpy as np
from osgeo import gdal
import pandas as pd
import os
import itertools
import time
import scipy
from scipy import stats

t0=time.time()


rasterFile = "2012Rect"
    
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
print  tifDf.shape

tifComb = list(itertools.product(range(tifDf.shape[0]), range(tifDf.shape[1])))
print len(tifComb)

samples1 = []
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
    samples1.append(sample)
print len(samples1)



rasterFile = "2014Rect"
    
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
print  tifDf.shape

tifComb = list(itertools.product(range(tifDf.shape[0]), range(tifDf.shape[1])))
print len(tifComb)

samples2 = []
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
    samples2.append(sample)
print len(samples2)

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
        
print float(null)/float(dif)

t1 = time.time()

total = t1-t0
print total