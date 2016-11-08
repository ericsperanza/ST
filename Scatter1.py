# Scatter1.py
from __future__ import print_function
import openpyxl
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind
from scipy.stats import pearsonr
from scipy.optimize import curve_fit
import numpy as np
import pandas as pd

# importo datos de excel y paso valores al array arnum
libro = openpyxl.load_workbook('compWC.xlsx')
hoja = libro.get_sheet_by_name('h3')
ar = pd.read_excel('compWC.xlsx','h3', header=0, index_col=None, na_values=['NA'])
arnum=ar.values

# creo el fondo de la figura
fig=plt.figure(facecolor='white', figsize=(9,7))
csfont = {'fontname':'Liberation Sans'}

flux = arnum[:,2]
disch = arnum[:,15]

#plot todos transparente
scat1 = fig.add_axes([0.1,0.1,0.8,0.8])
scat1.plot(disch,flux,'o',markersize=0)
#plot BA 
scat1.plot(arnum[0:17,15],arnum[0:17,2],'o',color='red',markersize=8, markeredgecolor = 'r')
#plot N
scat1.plot(arnum[18:42,15],arnum[18:42,2],'o',color='g',markersize=8, markeredgecolor = 'g')
#labels and limits
plt.ylim(0,350)
plt.yticks(np.arange(0,351,50),size=16,**csfont)
plt.xlim(0,50)
plt.xticks(np.arange(0,51,25),size=16,**csfont)
scat1.set_ylabel('Total particle flux (g.$\mathregular{cm^{-2}.day^{-1}}$)',size=22,**csfont)
scat1.set_xlabel('River discharge ($\mathregular{m^{3}.s}$)',size=22,**csfont)
scat1.spines['right'].set_visible(False)
scat1.yaxis.set_ticks_position('left')
scat1.spines['top'].set_visible(False)
scat1.xaxis.set_ticks_position('bottom')

flux = flux.astype(float)
disch = disch.astype(float)
#best fit for todos
lnflux = [np.log(s) for s in flux]
q = np.polyfit(disch,lnflux,1)

def func(x, a, b):
	#no logro el curve_fit me de los a y b correctos, los saco de calc
	#return 2.3381344*(np.exp(0.130045*x))
	return (np.exp(a))*(np.exp(b*x))
x = np.linspace(0,50,100)
scat1.plot(x, func(x, q[1],q[0]),'-',color='black')

print ('%2.6f exp( %2.6f * x) ' % (np.exp(q[1]),q[0]))
print("Pearson for Disch-Flux (r,p-value):", pearsonr(disch,flux))

plt.show()
