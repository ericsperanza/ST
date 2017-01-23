# WCDiffPerc.py
import openpyxl
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind
from scipy.stats import pearsonr
import numpy as np
import pandas as pd
import datetime

# importo datos de excel y paso valores al array arnum
libro = openpyxl.load_workbook('compWC.xlsx')
hoja = libro.get_sheet_by_name('h7')
ar = pd.read_excel('compWC.xlsx','h7', header=0, index_col=None, na_values=['NA'])
arnum=ar.values

# cuento cuantas muestras hay en BZ y N
sizeBZ=0
for a in arnum[:,0]:
	if a == 'BZ':
		sizeBZ+=1
sizeN=0
for a in arnum[:,0]:
	if a == 'N':
		sizeN+=1

# separo los datos calidos y frios para BZ y N (WBZ,CBZ, WN, CN)
WBZ = np.empty((0,20))
CBZ = np.empty((0,20))
for row in range(sizeBZ):
	if arnum[row,1] == 'calido':
		WBZ = np.append(WBZ,[arnum[row,2:22]], axis=0)
	else:
		CBZ= np.append(CBZ,[arnum[row,2:22]], axis=0)	
WN = np.empty((0,20))
CN = np.empty((0,20))
for row in range(sizeBZ,(sizeBZ+sizeN)):
	if arnum[row,1] == 'calido':
		WN = np.append(WN,[arnum[row,2:22]],axis=0)
	else:
		CN = np.append(CN,[arnum[row,2:22]],axis=0)
headers = []
for i in ar.columns:
	headers.append(i)

print("BA:")
print("Warm vs. Cold; p-value; r with flux")
for i in range (1,20):
	print("%s: %.2f %s %.2f vs %.2f %s %.2f; t-test: %.4f; r: %.2f, %.4f"%(headers[i+2],(np.mean(WBZ[:,i])),u"\u00b1",(np.std(WBZ[:,i],dtype=float,ddof=1)),(np.mean(CBZ[:,i])),u"\u00b1",(np.std(CBZ[:,i],dtype=float,ddof=1)),(ttest_ind(WBZ[:,i],CBZ[:,i]))[1],(pearsonr(arnum[0:24,2],arnum[0:24,i+2]))[0],(pearsonr(arnum[0:24,2],arnum[0:24,i+2]))[1] ) ).encode('utf-8')
	
print("N:")
print("Warm vs. Cold; p-value; r with flux")
for i in range (1,20):
	print("%s: %.2f %s %.2f vs %.2f %s %.2f; t-test: %.4f; r: %.2f, %.4f"%(headers[i+2],(np.mean(WN[:,i])),u"\u00b1",(np.std(WN[:,i],dtype=float,ddof=1)),(np.mean(CN[:,i])),u"\u00b1",(np.std(CN[:,i],dtype=float,ddof=1)),(ttest_ind(WN[:,i],CN[:,i]))[1],(pearsonr(arnum[25:57,2],arnum[25:57,i+2]))[0],(pearsonr(arnum[25:57,2],arnum[25:57,i+2]))[1] ) ).encode('utf-8')
	
	
	




