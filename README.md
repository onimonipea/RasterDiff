# RasterDiff
Python program designed to detect percentage of statistically different groups between geotif files with the same extent and spatial resolution.

This tool is designed to be a more complete version of the 'Detect Change' raster tool provided by ArcGIS. The ESRI tool will compare spatially similar pixels and return a raster with visualized differences between pixel values. 'Detect Change' does not tell you any summary statistics of the changes detected or the statistical significance of these changes. Though less refined, this tool will return the percentage of contigous groups that are statistically different between two raster image datasets.

It is necessary that each tif file has the same extent and spatial resolution per pixel (this may require masking by a shared .shp file within ArcGIS or QGIS, with resampling of pixel sizes).

The program simply creates a list of the individual pixels of each raster, pairing each pixel with its spatially identical partner. A t-test is then performed with the queen contiguity pixels (9 pixels, in total) for each core pixel composing the compared samples. The repository also includes a version that tests queen contiguity +1 for each core pixel (25 pixels, in total).
I’m sure that this is not the fastest way to accomplish this task, as it proves to be processor heavy. A timing module is included for comparison between different levels of contiguity and raster image size.
