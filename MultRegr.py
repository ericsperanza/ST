#MultRegr.py
from __future__ import print_function
import openpyxl
import matplotlib.pyplot as plt
import matplotlib.ticker as tick
from matplotlib import rcParams
from scipy.stats import ttest_ind
from scipy.stats import pearsonr
from scipy.optimize import curve_fit
from sklearn.feature_selection import f_regression
import numpy as np
import pandas as pd

# importo datos de excel y paso valores al array arnum
libro = openpyxl.load_workbook('compWC.xlsx')
hoja = libro.get_sheet_by_name('h5')
ar = pd.read_excel('compWC.xlsx','h5', header=0, index_col=None, na_values=['NA'])
arnum=ar.values

sizeBZ = 0
sizeN = 0

for i in arnum[:,0]:
	if i == 'BZ':
		sizeBZ +=1
	else:
		sizeN +=1
print('BZ:')
print (ar.columns[2],ar.columns[3],ar.columns[4],ar.columns[5])

xBZ = arnum[0:sizeBZ,2:6].astype(float)
yBZ = arnum[0:sizeBZ,1].astype(float)
FsBZ,valsBZ = f_regression(xBZ, yBZ, center=True)

print(FsBZ)
print(valsBZ)

print ('N:')
xN = arnum[sizeBZ:(sizeBZ+sizeN),2:6].astype(float)
yN = arnum[sizeBZ:(sizeBZ+sizeN),1].astype(float)

FsN,valsN = f_regression(xN, yN, center=True)

print(FsN)
print(valsN)

# END
