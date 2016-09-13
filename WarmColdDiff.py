# WarmColdDiff.py
import openpyxl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
libro = openpyxl.load_workbook('compWC.xlsx')
hoja = libro.get_sheet_by_name('h1')
ar = pd.read_excel('compWC.xlsx','h1', header=0, index_col=None, na_values=['NA'])
arnum=ar.values

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

WN = np.empty((0,3))
CN = np.empty((0,3))
for row in range(sizeBZ,(sizeBZ+sizeN)):
	if arnum[row,1] == 'calido':
		WN = np.append(WN,[arnum[row,2:5]],axis=0)
	else:
		CN = np.append(CN,[arnum[row,2:5]],axis=0)

print ("Warm vs. Cold\nBZ:")
print ("Flux: %.2f %s %.2f vs. %.2f %s %.2f"%((np.mean(WBZ[:,0])),u"\u00b1",(np.std(WBZ[:,0],dtype=float,ddof=1)),(np.mean(CBZ[:,0])),u"\u00b1",(np.std(CBZ[:,0],dtype=float,ddof=1))))
print ("Coprostanol: %.2f %s %.2f vs. %.2f %s %.2f"%((np.mean(WBZ[:,1])),u"\u00b1",(np.std(WBZ[:,1],dtype=float,ddof=1)),(np.mean(CBZ[:,1])),u"\u00b1",(np.std(CBZ[:,1],dtype=float,ddof=1))))
print ("Total ST: %.2f %s %.2f vs. %.2f %s %.2f"%((np.mean(WBZ[:,2])),u"\u00b1",(np.std(WBZ[:,2],dtype=float,ddof=1)),(np.mean(CBZ[:,2])),u"\u00b1",(np.std(CBZ[:,2],dtype=float,ddof=1))))
print ("N:")
print ("Flux: %.2f %s %.2f vs. %.2f %s %.2f"%((np.mean(WN[:,0])),u"\u00b1",(np.std(WN[:,0],dtype=float,ddof=1)),(np.mean(CN[:,0])),u"\u00b1",(np.std(CN[:,0],dtype=float,ddof=1))))
print ("Coprostanol: %.2f %s %.2f vs. %.2f %s %.2f"%((np.mean(WN[:,1])),u"\u00b1",(np.std(WN[:,1],dtype=float,ddof=1)),(np.mean(CN[:,1])),u"\u00b1",(np.std(CN[:,1],dtype=float,ddof=1))))
print ("Total ST: %.2f %s %.2f vs. %.2f %s %.2f"%((np.mean(WN[:,2])),u"\u00b1",(np.std(WN[:,2],dtype=float,ddof=1)),(np.mean(CN[:,2])),u"\u00b1",(np.std(CN[:,2],dtype=float,ddof=1))))

fig=plt.figure(facecolor='white', figsize=(7,9))
ax1=fig.add_subplot(2,1,1)

y = [(np.mean(WBZ[:,0])),(np.mean(CBZ[:,0]))]
yerr = [(np.std(WBZ[:,0],dtype=float,ddof=1)),(np.std(CBZ[:,0],dtype=float,ddof=1))]
x = [1,2]
plt.ylim(0,55)
plt.yticks(np.arange(0,55,25), size=16)
ax1.errorbar(x,y,yerr, fmt ='o',color='black',ms=20,elinewidth=3,capthick=4)
ax1.set_ylabel('Flux', size = 22)

ax2 = ax1.twinx()
x2=[1.3,2.3]
# el coprostanol esta dividido x 1000 para tener menos cifras en el eje
y2 = [(np.mean(WBZ[:,1]))/1000,(np.mean(CBZ[:,1]))/1000]
y2err = [(np.std(WBZ[:,1],dtype = float, ddof = 1))/1000,(np.std(CBZ[:,1], dtype = float, ddof = 1))/1000]
ax2.errorbar(x2, y2, y2err, fmt = 'o', color = 'white', ms = 20, elinewidth = 3, ecolor = 'black', capthick = 4)
plt.ylim(-5,16)
plt.yticks(np.arange(0,16,5), size = 16)
ax2.set_ylabel('Copr', size = 22)
plt.xlim(0,3)
plt.xticks( np.arange(4), ('','Warm','Cold',''), fontsize=22)
plt.setp(ax1.get_xticklabels(), fontsize=22)
plt.show()
