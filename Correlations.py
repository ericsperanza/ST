# Correlations.py
import openpyxl
from scipy.stats import pearsonr
import pandas as pd
import numpy as np
#import statsmodels.api as sm
import matplotlib.dates as mdates
from sklearn import linear_model

# importo datos de excel y paso valores al array arnum
libro = openpyxl.load_workbook('compWC.xlsx')
hoja = libro.get_sheet_by_name('Corr_Matrix')
ar = pd.read_excel('compWC.xlsx','Corr_Matrix', header=0, index_col=None, na_values=['NA'])
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

print (len(arnum[0]))

#matrix = np.corrcoef(arnum[:,1:15])

c=0

for i in ar.columns:
	print (c,i)
	c+=1
x,y = input ("variables a testear (separadas por coma, s/espacios) ")

print ("Correlacion (R2, p-value)")
print ("Todos: ",pearsonr(arnum[:,x],arnum[:,y]))
print ("BA: ",pearsonr(arnum[0:17,x],arnum[0:17,y]))
print ("N: ",pearsonr(arnum[18:42,x],arnum[18:42,y]))

date = arnum[:,15]
numdate = np.empty((0,1))
for i in date:
	numdate = np.append(numdate,(mdates.date2num(i)))
print(numdate)
"""
modelx = sm.GLS(arnum[:,x],numdate)
resx = modelx.fit()
print(resx.resid)
"""
numdate=numdate.reshape(-1,1)
print(numdate)
modelx = linear_model.LinearRegression()
modelx.fit(numdate,arnum[:,x])

print(modelx.residues_)




