# RasterDiff
Python program designed to detect percentage of statistically different groups between geotif files with the same extent and spatial resolution.

## Purpose
This tool is designed to be a more complete version of the 'Detect Change' raster tool provided by ArcGIS. The ESRI tool will compare spatially similar pixels and return a raster with visualized differences between pixel values. 'Detect Change' does not tell you any summary statistics of the changes detected or the statistical significance of these changes. Though less refined, this tool will return the percentage of contigous groups that are statistically different between two raster image datasets.


## Method
It is necessary that each tif file has the same extent and spatial resolution per pixel (this may require masking by a shared .shp file within ArcGIS or QGIS, with resampling of pixel sizes).

The program simply creates a list of the individual pixels of each raster, pairing each pixel with its spatially identical partner. A t-test is then performed with the queen contiguity pixels (9 pixels, in total) for each core pixel composing the compared samples. The repository also includes a version that tests queen contiguity +1 for each core pixel (25 pixels, in total).
I’m sure that this is not the fastest way to accomplish this task, as it proves to be processor heavy. A timing module is included for comparison between different levels of contiguity and raster image size.


## Files
RasterDiff1.py is a procedural method of statistical change detection with queen contiguity.

RasterDiff2.py is a procedural method of statistical change detection with queen contiguity +1.

RasterDiff.py is created to work within a command prompt accepting the raster .tif names as sys.argv[1] and sys.argv[2]

For queen contiguity +1 in RasterDiff.py, simlpy edit the 'groups' function to include the contiguity arguments from RasterDiff2.py.


Sample data is provided in 2012Phosph.tif and 2014Phosph.tif for temporal statistical change detection.


## Virtual Environment
Modules imported (necessary in virtual environment):

numpy

gdal

pandas

os

itertools

time

scipy

stats

sys
