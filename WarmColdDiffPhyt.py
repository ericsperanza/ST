# WarmColdDiffPhyt.py
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
libro = openpyxl.load_workbook('compWC.xlsx')
hoja = libro.get_sheet_by_name('h3')
ar = pd.read_excel('compWC.xlsx','h3', header=0, index_col=None, na_values=['NA'])
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
WBZ = np.empty((0,14))
CBZ = np.empty((0,14))
for row in range(sizeBZ):
	if arnum[row,1] == 'calido':
		WBZ = np.append(WBZ,[arnum[row,2:16]], axis=0)
	else:
		CBZ= np.append(CBZ,[arnum[row,2:16]], axis=0)	
WN = np.empty((0,14))
CN = np.empty((0,14))
for row in range(sizeBZ,(sizeBZ+sizeN)):
	if arnum[row,1] == 'calido':
		WN = np.append(WN,[arnum[row,2:16]],axis=0)
	else:
		CN = np.append(CN,[arnum[row,2:16]],axis=0)

# paso el coprostanol de BZ a mg/g para no usar valores tan altos
rows, cols = WBZ.shape
for a in range(rows):
	WBZ[a,1] = WBZ[a,1]/1000
print (WBZ[:,1])
rows, cols = CBZ.shape
for a in range(rows):
	CBZ[a,1] = CBZ[a,1]/1000
print (CBZ[:,1])

# imprimo las medias y desvios para cada estacion y variable
print ("Warm vs. Cold\nBZ:")
print ("Flux: %.2f %s %.2f vs. %.2f %s %.2f"%((np.mean(WBZ[:,0])),u"\u00b1",(np.std(WBZ[:,0],dtype=float,ddof=1)),(np.mean(CBZ[:,0])),u"\u00b1",(np.std(CBZ[:,0],dtype=float,ddof=1))))
print ("Coprostanol: %.2f %s %.2f vs. %.2f %s %.2f"%((np.mean(WBZ[:,1])),u"\u00b1",(np.std(WBZ[:,1],dtype=float,ddof=1)),(np.mean(CBZ[:,1])),u"\u00b1",(np.std(CBZ[:,1],dtype=float,ddof=1))))
print ("Total ST: %.2f %s %.2f vs. %.2f %s %.2f"%((np.mean(WBZ[:,2])),u"\u00b1",(np.std(WBZ[:,2],dtype=float,ddof=1)),(np.mean(CBZ[:,2])),u"\u00b1",(np.std(CBZ[:,2],dtype=float,ddof=1))))
print ("N:")
print ("Flux: %.2f %s %.2f vs. %.2f %s %.2f"%((np.mean(WN[:,0])),u"\u00b1",(np.std(WN[:,0],dtype=float,ddof=1)),(np.mean(CN[:,0])),u"\u00b1",(np.std(CN[:,0],dtype=float,ddof=1))))
print ("Coprostanol: %.2f %s %.2f vs. %.2f %s %.2f"%((np.mean(WN[:,1])),u"\u00b1",(np.std(WN[:,1],dtype=float,ddof=1)),(np.mean(CN[:,1])),u"\u00b1",(np.std(CN[:,1],dtype=float,ddof=1))))
print ("Total ST: %.2f %s %.2f vs. %.2f %s %.2f"%((np.mean(WN[:,2])),u"\u00b1",(np.std(WN[:,2],dtype=float,ddof=1)),(np.mean(CN[:,2])),u"\u00b1",(np.std(CN[:,2],dtype=float,ddof=1))))

c = -2
for i in ar.columns:
	print (c,i)
	c+=1

x = input ("variable a plotear: ")

# creo el fondo de la figura
fig=plt.figure(facecolor='white', figsize=(9,14))
csfont = {'fontname':'Liberation Sans'}

# agrego la serie temporal
time1 = fig.add_axes([0.1, 0.58, 0.8, 0.4])
date = arnum[0:17,16]
flux = arnum[0:17,2]
ndate = np.empty((0,1))
for i in date:
	ndate = np.append(ndate, (mdates.date2num(i)))
newx = np.linspace(ndate.min(), ndate.max(), 200)
dd = mdates.num2date(newx)
akima1 = interpolate.Akima1DInterpolator(ndate, flux)
time1.plot(newx, akima1(newx), 'black', linewidth=3)
time1.plot(date, flux, 'o', color = 'black', markersize=10, markeredgecolor = 'black')
time1.xaxis.set_major_locator(mdates.MonthLocator(interval = 4))
time1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
plt.ylim(0,350)
plt.yticks(np.arange(0,351,100), size = 16, **csfont)
time1.set_ylabel('Vertical flux (g.$\mathregular{cm^{-2}.day^{-1}}$)', size = 22, position = (1,0), **csfont)
fig.autofmt_xdate(rotation = 90)
time1.tick_params(axis='x', which='major', labelsize=14)
time1.set_xlim([datetime.date(2007,12,1),datetime.date(2014,3,7)])

# ploteo x en timeserie
time2 = time1.twinx()
xBZ = arnum[0:17,(x+2)]
"""# paso el copro a mg/g en el array copr
for a in range (0,17):
	copr[a] = copr[a]/1000"""
akima2 = interpolate.Akima1DInterpolator(ndate, xBZ)
time2.plot(newx, akima2(newx), 'black', color = 'g',linewidth=3 )
time2.plot(date, xBZ, 'o', color = 'white', markersize=10,markeredgecolor = 'black')
plt.ylim(0,2200)
plt.yticks(np.arange(0,2001,500), size = 16, **csfont)
time2.set_ylabel('Phytosterols ($\mathregular{ug.g^{-1}}$)', size = 22, position =(1,0), **csfont)
plt.xticks(size = 16, **csfont)
time2.set_xlim([datetime.date(2007,12,1),datetime.date(2014,3,7)])
plt.setp(time1.get_xticklabels(),visible=False)

# agrego el boxplot
box1 = fig.add_axes([0.145, 0.79, 0.18, 0.18])
# elndarray tiene dtype=object y no sirve xa hacer bplot directo
WBZ = WBZ.astype(float)
CBZ = CBZ.astype(float)
# ploteo flujo
bprop = dict(linewidth = 1, color = 'black')
wprop = dict(linewidth = 1, linestyle = '-', color = 'black')
mprop = dict(linestyle = '-', linewidth = 1, color = 'white')
pprop = dict(marker = 'o', markeredgecolor = 'white', markerfacecolor = 'white', markersize = 5)
cap = dict(linewidth = 1)
box1.boxplot([WBZ[:,0],CBZ[:,0]], vert=True, positions = (0.9,1.9), notch=False, patch_artist = True, showmeans = True, showfliers = False, boxprops = bprop, whiskerprops = wprop, medianprops = mprop, meanprops = pprop, capprops = cap)
plt.ylim(0,255)
plt.yticks(np.arange(0,255,125), size = 13, **csfont)
#box1.set_ylabel('Flux', size = 22)

# ploteo x
bprop2 = dict(linewidth = 1)
wprop2 = dict(linewidth = 1, linestyle = '-', color = 'black')
mprop2 = dict(linestyle = '-', linewidth = 1, color = 'black')
pprop2 = dict(marker = 'o', markeredgecolor = 'black', markerfacecolor = 'black', markersize=5)
cap2 = dict(linewidth = 1)
box2 = box1.twinx()
box2.boxplot([WBZ[:,x], CBZ[:,x]], notch=None, vert = True, positions = (0.9,2.2),   patch_artist = True, showmeans = True, showfliers = False,boxprops = bprop2, whiskerprops = wprop, medianprops = mprop2, meanprops = pprop2, capprops = cap2)
plt.ylim(0,1500)
plt.yticks(np.arange(0,1501,500), size = 13, **csfont)
#box2.set_ylabel('Copr', size = 22)
plt.xticks(np.arange(4), ('','Warm','Cold',''), size =14, **csfont)
plt.setp(box1.get_xticklabels(), visible = 'True', fontsize = 16)

"""
Plot N
"""

# agrego la serie temporal N
time3 = fig.add_axes([0.1, 0.15, 0.8, 0.4])
dateN = arnum[18:42,16]
fluxN = arnum[18:42,2]
ndateN = np.empty((0,1))
for i in dateN:
	ndateN = np.append(ndateN, (mdates.date2num(i)))
newxN = np.linspace(ndateN.min(), ndateN.max(), 200)
ddN = mdates.num2date(newxN)
akima3 = interpolate.Akima1DInterpolator(ndateN, fluxN)
time3.plot(newxN, akima3(newxN), 'black', linewidth=3)
time3.plot(dateN, fluxN, 'o', color = 'black', markersize=10)
time3.xaxis.set_major_locator(mdates.MonthLocator(interval = 4))
time3.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
plt.ylim(0,20)
plt.yticks(np.arange(0,21,10), size = 16, **csfont)
#time3.set_ylabel('Vertical flux (g.$\mathregular{cm^{-2}.day^{-1}}$)', size = 22, **csfont)
fig.autofmt_xdate(rotation = 90)
time3.tick_params(axis='x', which='major', labelsize=14)
plt.xticks(size = 16, rotation='vertical', **csfont)
time3.set_xlim([datetime.date(2007,12,1),datetime.date(2014,3,7)])

# ploteo el xN en timeserie
time4 = time3.twinx()
xN = arnum[18:42,(x+2)]
akima4 = interpolate.Akima1DInterpolator(ndateN, xN)
time4.plot(newxN, akima4(newxN), 'black', color = 'g', linewidth=3)
time4.plot(dateN, xN, 'o', color = 'white', markersize=10, markeredgecolor = 'black')
plt.ylim(0,150)
plt.yticks(np.arange(0,151,50), size = 16, **csfont)
#time4.set_ylabel('Coprostanol (ug.$\mathregular{g^{-1}}$)', size = 22, **csfont)
time4.set_xlim([datetime.date(2007,12,1),datetime.date(2014,3,7)])

# agrego el boxplot
box3 = fig.add_axes([0.141, 0.356, 0.18, 0.18])
# ploteo flujo
box3.boxplot([WN[:,0],CN[:,0]], vert=True, positions = (0.9,1.9), notch=False, patch_artist = True, showmeans = True, showfliers = False, boxprops = bprop, whiskerprops = wprop, medianprops = mprop, meanprops = pprop, capprops = cap)
plt.ylim(0,10)
plt.yticks(np.arange(0,10.1,5), size = 13, **csfont)

# ploteo xN
box4 = box3.twinx()
box4.boxplot([WN[:,x], CN[:,x]], notch=None, vert = True, positions = (0.9,2.2),   patch_artist = True, showmeans = True, showfliers = False,boxprops = bprop2, whiskerprops = wprop, medianprops = mprop2, meanprops = pprop2, capprops = cap2)
plt.ylim(0,100)
plt.yticks(np.arange(0,101,50), size = 13, **csfont)
plt.xticks(np.arange(4), ('','Warm','Cold',''), size =16, **csfont)
plt.setp(box3.get_xticklabels(), visible = 'True', fontsize = 16)
print(time4.get_xlim())
print("t-test BZ (flux, copr, total)")
for a in range(14):
	print(a, ttest_ind(WBZ[:,a],CBZ[:,a]))
print("Pearson for Flux-Copr:")
print(pearsonr(flux,xBZ))
print("t-test N (flux, copr, total)")
for a in range(14):
	print(a, ttest_ind(WN[:,a],CN[:,a]))
print("Pearson for Flux-Copr:")
print(pearsonr(fluxN,xN))


plt.show()


