#SedRet.py
from __future__ import print_function
import openpyxl
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook
import matplotlib.dates as mdates
from scipy import interpolate 
from scipy import signal
from scipy.stats import ttest_ind
from scipy.stats import pearsonr
import numpy as np
import pandas as pd
import datetime

# importo datos de excel y paso valores al array arnum
libro = openpyxl.load_workbook('sedDegr.xlsx')
hoja = libro.get_sheet_by_name('WFL')
ar = pd.read_excel('sedDegr.xlsx','WFL', header=0, index_col=None, na_values=['NA'])
arnum=ar.values
hoja2 = libro.get_sheet_by_name('DW')
ar2 = pd.read_excel('sedDegr.xlsx','DW', header=0, index_col=None, na_values=['NA'])
arnum2=ar2.values
hoja3 = libro.get_sheet_by_name('sed')
ar3 = pd.read_excel('sedDegr.xlsx','sed', header=0, index_col=None, na_values=['NA'])
arnum3=ar3.values

# cuento cuantas muestras hay en BZ y N
sizeBZ=0
for a in arnum[:,0]:
	if a == 'BZ':
		sizeBZ+=1
sizeN=0
for a in arnum[:,0]:
	if a == 'N':
		sizeN+=1

years = 7
densidad = 2.65
#calculo g/cm2 de particles depositadas al anio
depBA = np.mean(arnum2[0:17,3])
print("BA:")
print("Deposition mass (g/cm2/year): %.2f"%depBA)
print("Sedimentation rate (cm/year): %.2f"%(depBA/densidad))
depN = np.mean(arnum2[18:42,3])
print("N:")
print("Deposition mass (g/cm2/year): %.2f"%depN)
print("Sedimentation rate (cm/year): %.2f"%(depN/densidad))

# paso fechas a numeros y hago un vector lineal de 200 units
date = arnum2[0:17,1]
ndate = np.empty((0,1))
for i in date:
	ndate = np.append(ndate,(mdates.date2num(i)))
newx = np.linspace(ndate.min(),ndate.max(), 2555)

# imprimo los % de retencion 
print("Retention in sediment (%)")
print("BA")
headers = []
for i in ar2.columns:
	headers.append(i) 

BA = np.empty((0,1))
for i in range(20):
	akima = interpolate.Akima1DInterpolator(ndate, arnum2[0:17,i+4])	
	area = 	((np.trapz(akima(newx), newx))/(years))
	ret = ((100*(((arnum3[0,i+4])/1000000)*depBA))/area)
	print(headers[i+4],area,ret)

plt.plot(newx,akima(newx))
plt.bar(newx,akima(newx))
print((sum(akima(newx)))/17)
plt.show()
#N = np.empty((0,1))

