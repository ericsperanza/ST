# Scatter1.py

import openpyxl
import matplotlib.pyplot as plt
import matplotlib.ticker as tick
from matplotlib import rcParams
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

# cuento cuantas muestras hay en BZ y N
sizeBZ = 0 
sizeN = 0
for a in arnum[:,0]:
	if a == 'BZ':
		sizeBZ += 1
	else:
		sizeN += 1
# separo datos warm from cold
WBZ = np.empty((0,14))
CBZ = np.empty((0,14))
for i in range(sizeBZ):
	if arnum[i,1] == 'calido':
		WBZ=np.append(WBZ,[arnum[i,2:16]], axis = 0)
	else:
		CBZ=np.append(CBZ,[arnum[i,2:16]], axis = 0)
WN = np.empty((0,14))
CN = np.empty((0,14))
for i in range (sizeBZ,(sizeBZ + sizeN)):
	if arnum[i,1] == 'calido':
		WN = np.append(WN,[arnum[i,2:16]],axis = 0)
	else:
		CN = np.append(CN,[arnum[i,2:16]],axis = 0)

rcParams['ytick.minor.size'] = 0
rcParams['ytick.minor.width'] = 0
# creo el fondo de la figura
fig=plt.figure(facecolor='white', figsize=(7,5))
csfont = {'fontname':'Liberation Sans'}

flux = arnum[:,2]
disch = arnum[:,15]


#plot todos transparente
scat1 = fig.add_axes([0.15,0.15,0.8,0.8])

#best fit for todos
flux = flux.astype(float)
disch = disch.astype(float)

lnflux = [np.log(s) for s in flux]
q = np.polyfit(disch,lnflux,1)
def func(x, a, b):
	return (np.exp(a))*(np.exp(b*x))
x = np.linspace(0,50,100)
scat1.semilogy(x, func(x, q[1],q[0]),'-',color='black', linewidth = 2)
#plot BA 
scat1.semilogy(WBZ[:,13],WBZ[:,0],'o',color='k',markersize=9, markeredgecolor = 'k')
scat1.semilogy(CBZ[:,13],CBZ[:,0],'o',color='white',markersize=9, markeredgecolor = 'k')
#plot N
scat1.semilogy(WN[:,13],WN[:,0],'s',color='grey',markersize=9, markeredgecolor = 'grey')
scat1.semilogy(CN[:,13],CN[:,0],'s',color='White',markersize=9, markeredgecolor = 'grey')
#labels and limits
plt.ylim(0,400)
plt.yticks(size=16,**csfont)
scat1.set_xticks([1,10,100])
plt.xlim(0,50)
plt.xticks(np.arange(0,51,25),size=16,**csfont)
scat1.get_yaxis().set_major_formatter(tick.ScalarFormatter())

scat1.set_ylabel('Total particle flux (mg.$\mathregular{cm^{-2}.day^{-1}}$)',size=22,**csfont)
scat1.set_xlabel('River discharge ($\mathregular{10^{3}m^{3}.s^{-1}}$)',size=22,**csfont)
scat1.spines['right'].set_visible(False)
scat1.yaxis.set_ticks_position('left')
scat1.spines['top'].set_visible(False)
scat1.xaxis.set_ticks_position('bottom')


print ('%2.6f exp( %2.6f * x) ' % (np.exp(q[1]),q[0]))
print("Pearson for Disch-Flux (r,p-value):", pearsonr(disch,flux))
print("Warm vs. Cold Difference (t-test)\nBA:")
print("%.2f %s %.2f vs %.2f %s %.2f"%( (np.mean(WBZ[:,0])), u"\u00b1", (np.std(WBZ[:,0],dtype=float,ddof=1)), (np.mean(CBZ[:,0])), u"\u00b1", (np.std(CBZ[:,0],dtype=float,ddof=1)))).encode('utf-8')

print(ttest_ind(WBZ[:,0],CBZ[:,0]))
print("N:\n%.2f %s %.2f vs %.2f %s %.2f"%( (np.mean(WN[:,0])), u"\u00b1", (np.std(WN[:,0],dtype=float,ddof=1)), (np.mean(CN[:,0])), u"\u00b1", (np.std(CN[:,0],dtype=float,ddof=1)))).encode('utf-8')
print(ttest_ind(WN[:,0],CN[:,0]))

plt.show()
