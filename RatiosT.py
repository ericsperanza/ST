# RatiosT.py
import openpyxl
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind
from scipy.stats import pearsonr
import numpy as np
import pandas as pd

# importo datos de excel y paso valores al array arnum
libro = openpyxl.load_workbook('HistRatios.xlsx')
hoja = libro.get_sheet_by_name('dw')
ar = pd.read_excel('HistRatios.xlsx','dw',header=0, index_col=None, na_values=['NA'])
arnum=ar.values
headers=list(ar)

# cuento cuantas muestras hay en BZ y N
sizeBZ=0
for a in arnum[:,0]:
	if a == 'BZ':
		sizeBZ+=1
sizeN=0
for a in arnum[:,0]:
	if a == 'N':
		sizeN+=1
print(sizeBZ, sizeN)

# creo el fondo de la figura
fig=plt.figure(facecolor='white', figsize=(10,6))
arnum2 = arnum[:,1:27].astype(float)
print(arnum2)
# agrego el boxplot
box1 = fig.add_axes([0.35, 0.60, 0.3, 0.35])
box1.boxplot([arnum2[0:24,21],arnum2[25:57,21]], vert = True)

plt.show()
