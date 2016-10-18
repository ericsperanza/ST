# WarmColdDiff.py
from __future__ import print_function
import openpyxl
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook
import matplotlib.dates as mdates
from scipy import interpolate 
from scipy import signal
import numpy as np
import pandas as pd

# importo datos de excel y paso valores al array arnum
libro = openpyxl.load_workbook('compWC.xlsx')
hoja = libro.get_sheet_by_name('h1')
ar = pd.read_excel('compWC.xlsx','h1', header=0, index_col=None, na_values=['NA'])
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
WBZ = np.empty((0,3))
CBZ = np.empty((0,3))
for row in range(sizeBZ):
	if arnum[row,1] == 'calido':
		WBZ = np.append(WBZ,[arnum[row,2:5]], axis=0)
	else:
		CBZ= np.append(CBZ,[arnum[row,2:5]], axis=0)	
WN = np.empty((0,3))
CN = np.empty((0,3))
for row in range(sizeBZ,(sizeBZ+sizeN)):
	if arnum[row,1] == 'calido':
		WN = np.append(WN,[arnum[row,2:5]],axis=0)
	else:
		CN = np.append(CN,[arnum[row,2:5]],axis=0)

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

# creo el fondo de la figura
fig=plt.figure(facecolor='white', figsize=(7,9))

# agrego el primer subplot (puntos con desvios)
ax1=fig.add_subplot(3,1,1)

# ploteo el flujo 
y = [(np.mean(WBZ[:,0])),(np.mean(CBZ[:,0]))]
yerr = [(np.std(WBZ[:,0],dtype=float,ddof=1)),(np.std(CBZ[:,0],dtype=float,ddof=1))]
x = [0.9,1.9]
plt.ylim(0,210)
plt.yticks(np.arange(0,210,50), size=16)
ax1.errorbar(x,y,yerr, fmt ='o',color='black',ms=15,elinewidth=3,capthick=3, capsize = 6)
ax1.set_ylabel('Flux', size = 22)

# agrego ejes x e y gemelos para plotear coprostanol
ax2 = ax1.twinx()
x2=[1.1,2.1]
y2 = [(np.mean(WBZ[:,1])),(np.mean(CBZ[:,1]))]
y2err = [(np.std(WBZ[:,1],dtype = float, ddof = 1)),(np.std(CBZ[:,1], dtype = float, ddof = 1))]
ax2.errorbar(x2, y2, y2err, fmt = 'o', color = 'white', ms = 15, elinewidth = 3, ecolor = 'black', capthick = 3, capsize = 6)
plt.ylim(-1,13)
plt.yticks(np.arange(0,13,6), size = 16)
ax2.set_ylabel('Copr', size = 22)
plt.xlim(0,3)
plt.xticks(np.arange(4),('','Warm','Cold',''), size=22)
plt.setp(ax1.get_xticklabels(which='major'), visible = 'True', fontsize=22)
#ax1.tick_params(axis = 'x', direction='out', length=6, width=2, colors='r', labelbottom = 'on', labelsize = 'large', labelcolor = 'black')
#ax2.axes.get_xaxis().set_visible(False)

# agrego el segundo subplot (boxplot)
box1=fig.add_subplot(3,1,2)
#box1 = fig.add_axes([0.5, 0.5, 0.5, 0.5])
# elndarray tiene dtype=object y no sirve xa hacer bplot directo
WBZ = WBZ.astype(float)
CBZ = CBZ.astype(float)
# ploteo flujo
bprop = dict(linewidth = 1, color = 'black')
wprop = dict(linewidth = 4, linestyle = '-', color = 'black')
mprop = dict(linestyle = '-', linewidth = 2, color = 'white')
pprop = dict(marker = 'o', markeredgecolor = 'white', markerfacecolor = 'white')
cap = dict(linewidth = 4)
box1.boxplot([WBZ[:,0],CBZ[:,0]], vert=True, positions = (0.9,1.9), notch=False, patch_artist = True, showmeans = True, showfliers = False, boxprops = bprop, whiskerprops = wprop, medianprops = mprop, meanprops = pprop, capprops = cap)
plt.ylim(0,255)
plt.yticks(np.arange(0,255,50), size = 16)
box1.set_ylabel('Flux', size = 22)

# ploteo coprostanol
bprop2 = dict(linewidth = 2)
wprop2 = dict(linewidth = 4, linestyle = '-', color = 'black')
mprop2 = dict(linestyle = '-', linewidth = 2, color = 'black')
pprop2 = dict(marker = 'o', markeredgecolor = 'black', markerfacecolor = 'black')
cap2 = dict(linewidth = 4)
box2 = box1.twinx()
box2.boxplot([WBZ[:,1], CBZ[:,1]], notch=None, vert = True, positions = (0.9,2.2),   patch_artist = True, showmeans = True, showfliers = False,boxprops = bprop2, whiskerprops = wprop, medianprops = mprop2, meanprops = pprop2, capprops = cap2)
plt.ylim(0,18)
plt.yticks(np.arange(0,18,8), size = 16)
box2.set_ylabel('Copr', size = 22)
plt.xticks(np.arange(4), ('','Warm','Cold',''))
plt.setp(box2.get_xticklabels(), visible = 'True', size = 22)

# agrego el tercer subplot (serie temporal)
time1 = fig.add_subplot(3,1,3)
date = arnum[0:24,5]
flux = arnum[0:24,2]
ndate = np.empty((0,1))
for i in date:
	ndate = np.append(ndate, (mdates.date2num(i)))
#rep = interpolate.splrep(ndate, flux, s=0)
newx = np.linspace(ndate.min(), ndate.max(), 200)
#newy = interpolate.splev(newx,rep)
dd = mdates.num2date(newx)
time1.plot(date, flux, 'o', color = 'black')
time1.xaxis.set_major_locator(mdates.MonthLocator(interval = 6))
time1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
#time1.plot(dd, newy)
akima1 = interpolate.Akima1DInterpolator(ndate, flux)
time1.plot(newx, akima1(newx), 'black')
plt.ylim(0,350)
plt.yticks(np.arange(0,351,100), size = 16)
time1.set_ylabel('Flux', size = 22)
fig.autofmt_xdate(rotation = 90)


# ploteo el copr en timeserie
time2 = time1.twinx()
copr = arnum[0:24,3]
# paso el copro a mg/g en el array copr
for a in range (0,24):
	copr[a] = copr[a]/1000
print (copr)
# next 4 lines due to porblems arising when using .spline
"""copr = copr.astype(float)
copro = np.empty((0,1))
for i in copr:
	copro = np.append(copro, i)"""
# para usar, poner newy2 en el .plot
#rep2 = interpolate.splrep(ndate, copr, s = 0, k = 1)
#newy2 = interpolate.splev(newx, rep2)
# soline es vieja, ver http://docs.scipy.org/doc/scipy/reference/interpolate.html
# newy3 = interpolate.spline(ndate, copro, ndate, order = 0)
#ysg = signal.savgol_filter(newy2, 15, 7, mode = 'wrap')
time2.plot(date, copr, 'o', color = 'white', markeredgecolor = 'black')
#time2.plot(dd,newy2, color = 'red')
#time2.plot(dd, ysg, color = 'red')
# ver (http://stackoverflow.com/questions/37214786/emulating-excels-scatter-with-smooth-curve-spline-function-in-matplotlib-for)
akima2 = interpolate.Akima1DInterpolator(ndate, copr)
time2.plot(newx, akima2(newx), 'black', linestyle='--')
plt.ylim(0,20)
plt.yticks(np.arange(0,21,8), size = 16)
time2.set_ylabel('Copr', size = 22)

plt.show()
