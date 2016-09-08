# WarmColdDiff.py
import openpyxl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
libro = openpyxl.load_workbook('compWC.xlsx')
hoja = libro.get_sheet_by_name('h1')
ar = pd.read_excel('compWC.xlsx','h1', header=0, index_col=None, na_values=['NA'])
arnum=ar.values
print(arnum[:,1])
print ar
sizeBZ=0
for a in arnum[:,0]:
	if a == 'BZ':
		sizeBZ+=1
sizeN=0
for a in arnum[:,0]:
	if a == 'N':
		sizeN+=1
WBZ = np.empty((0,3))
CBZ = np.empty((0,3))
for row in range(sizeBZ):
	if arnum[row,1] == 'calido':
		WBZ = np.append(WBZ,[arnum[row,2:5]], axis=0)
	else:
		CBZ= np.append(CBZ,[arnum[row,2:5]], axis=0)	
print CBZ
print WBZ
WN = np.empty((0,3))
CN = np.empty((0,3))
for row in range(sizeBZ,(sizeBZ+sizeN)):
	if arnum[row,1] == 'calido':
		WN = np.append(WN,[arnum[row,2:5]],axis=0)
	else:
		CN = np.append(CN,[arnum[row,2:5]],axis=0)
print WN
print CN
print np.mean(WBZ, axis=0)

