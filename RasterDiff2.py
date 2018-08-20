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
        q1 = tifDf.iloc[r-2][c-2]
        q2 = tifDf.iloc[r-2][c-1]
        q3 = tifDf.iloc[r-2][c]
        q4 = tifDf.iloc[r-2][c+1]
        q5 = tifDf.iloc[r-2][c+2]
        q6 = tifDf.iloc[r-1][c-2]
        q7 = tifDf.iloc[r-1][c-1]
        q8 = tifDf.iloc[r-1][c]
        q9 = tifDf.iloc[r-1][c+1]
        q10 = tifDf.iloc[r-1][c+2]
        q11 = tifDf.iloc[r][c-2]
        q12 = tifDf.iloc[r][c-1]
        core = tifDf.iloc[r][c]
        q14 = tifDf.iloc[r][c+1]
        q15 = tifDf.iloc[r][c+2]
        q16 = tifDf.iloc[r+1][c-2]
        q17 = tifDf.iloc[r+1][c-1]
        q18 = tifDf.iloc[r+1][c]
        q19 = tifDf.iloc[r+1][c+1]
        q20 = tifDf.iloc[r+1][c+2]
        q21 = tifDf.iloc[r+2][c-2]
        q22 = tifDf.iloc[r+2][c-1]
        q23 = tifDf.iloc[r+2][c]
        q24 = tifDf.iloc[r+2][c+1]
        q25 = tifDf.iloc[r+2][c+2]
    except:
        pass
    # Combine cells into sample list
    sample = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10,q11,q12,core,q14,q15,q16,q17,q18,q19,q20,q21,q22,q23,q24,q25]
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
        q1 = tifDf.iloc[r-2][c-2]
        q2 = tifDf.iloc[r-2][c-1]
        q3 = tifDf.iloc[r-2][c]
        q4 = tifDf.iloc[r-2][c+1]
        q5 = tifDf.iloc[r-2][c+2]
        q6 = tifDf.iloc[r-1][c-2]
        q7 = tifDf.iloc[r-1][c-1]
        q8 = tifDf.iloc[r-1][c]
        q9 = tifDf.iloc[r-1][c+1]
        q10 = tifDf.iloc[r-1][c+2]
        q11 = tifDf.iloc[r][c-2]
        q12 = tifDf.iloc[r][c-1]
        core = tifDf.iloc[r][c]
        q14 = tifDf.iloc[r][c+1]
        q15 = tifDf.iloc[r][c+2]
        q16 = tifDf.iloc[r+1][c-2]
        q17 = tifDf.iloc[r+1][c-1]
        q18 = tifDf.iloc[r+1][c]
        q19 = tifDf.iloc[r+1][c+1]
        q20 = tifDf.iloc[r+1][c+2]
        q21 = tifDf.iloc[r+2][c-2]
        q22 = tifDf.iloc[r+2][c-1]
        q23 = tifDf.iloc[r+2][c]
        q24 = tifDf.iloc[r+2][c+1]
        q25 = tifDf.iloc[r+2][c+2]
    except:
        pass
    # Combine cells into sample list
    sample = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10,q11,q12,core,q14,q15,q16,q17,q18,q19,q20,q21,q22,q23,q24,q25]
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

if dif == 0:  
    print "Null 100%"
else:      
    print float(null)/float(dif)
    
t1 = time.time()

total = t1-t0
print total