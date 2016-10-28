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
fig=plt.figure(facecolor='white', figsize=(12,6))
arnum2 = arnum[:,1:27].astype(float)
csfont = {'fontname':'Liberation Sans'}

# agrego el boxplot
box1 = fig.add_axes([0.05, 0.10, 0.7, 0.8])
bprop1 = dict(linewidth = 2, edgecolor = 'red')
wprop1 = dict(linewidth = 2, linestyle = '-', color = 'red')
mprop1 = dict(linestyle = '-',linewidth = 2, color = 'red')
pprop1 = dict(marker = 'o', markeredgecolor = 'red', markerfacecolor = 'red')
cap1 = dict(linewidth = 2, color = 'r')
box1.boxplot([arnum2[0:24,22],arnum2[0:24,21],arnum2[0:24,23],arnum2[0:24,24]], vert = True, positions = (2,5,8,11), notch = False, patch_artist = True, showmeans = True, showfliers = False, boxprops = bprop1, whiskerprops = wprop1, medianprops = mprop1, meanprops = pprop1, capprops = cap1)
bprop2 = dict(linewidth = 2, edgecolor = 'g')
wprop2 = dict(linewidth = 2, linestyle = '-', color = 'g')
mprop2 = dict(linestyle = '-',linewidth = 2, color = 'g')
pprop2 = dict(marker = 'o', markeredgecolor = 'g', markerfacecolor = 'g')
cap2 = dict(linewidth = 2, color = 'g')
box1.boxplot([arnum2[25:57,22],arnum2[25:57,21],arnum2[25:57,23],arnum2[25:57,24]], vert = True, positions = (1,4,7,10), notch = False, patch_artist = True, showmeans = True, showfliers = False, boxprops = bprop2, whiskerprops = wprop2, medianprops = mprop2, meanprops = pprop2, capprops = cap2)
# borro ejes, ticks y labels
box1.spines['top'].set_visible(False)
box1.spines['bottom'].set_visible(False)
box1.spines['right'].set_visible(False)
box1.tick_params(length=0, which='both')
box1.axes.get_xaxis().set_visible(False)
# agrego vertical lines
plt.vlines(3,0,1,linestyle = '--')
plt.vlines(6,0,1,linestyle = '--')
plt.vlines(9,0,1,linestyle = '--')
# formateo ejes y ticks
plt.ylim(0,1)
plt.yticks(np.arange(0,1.1,0.5), size = 16, **csfont)
plt.xlim(0,12)

box2 = fig.add_axes([0.77, 0.10, 0.21, 0.8])
box2.boxplot([arnum2[25:57,25]], vert = True, positions = ([0.3]), notch = False, patch_artist = True, showmeans = True, showfliers = False, boxprops = bprop2, whiskerprops = wprop2, medianprops = mprop2, meanprops = pprop2, capprops = cap2)
box2.boxplot([arnum2[0:24,25]], vert = True, positions = ([0.6]), notch = False, patch_artist = True, showmeans = True, showfliers = False, boxprops = bprop1, whiskerprops = wprop1, medianprops = mprop1, meanprops = pprop1, capprops = cap1)
# borro ejes, ticks y labels
box2.spines['top'].set_visible(False)
box2.spines['bottom'].set_visible(False)
box2.spines['right'].set_visible(False)
box2.tick_params(length=0, which='both')
box2.axes.get_xaxis().set_visible(False)
# formateo ejes y ticks
plt.ylim(0,0.2)
plt.yticks(np.arange(0,0.21,0.1), size = 16, **csfont)
plt.xlim(0,1)

# agrego titles
box1.text(0.65,1.03,r'Fecal/Phyto', fontsize = 18, **csfont)
box1.text(3.5,1.03,r'Cop/epiCop', fontsize = 18, **csfont)
box1.text(6.5,1.03,r'Cop/ethylCop', fontsize = 18, **csfont)
box1.text(9.5,1.03,r'Sito/ethylCop', fontsize = 18, **csfont)
box1.text(13.0,1.03,r'Chnol/Chrol', fontsize = 18, **csfont)

print("Fecal/Phyto: ", ttest_ind(arnum2[0:24,22],arnum2[25:57,22]))
print("Cop/Epi: ", ttest_ind(arnum2[0:24,21],arnum2[25:57,21]))
print("Cop/eCop: ", ttest_ind(arnum2[0:24,23],arnum2[25:57,23]))
print("Sito/eCop: ", ttest_ind(arnum2[0:24,24],arnum2[25:57,24]))
print("Chnol/Chrol: ", ttest_ind(arnum2[0:24,25],arnum2[25:57,25]))

plt.show()
