# RatiosTS.py
import openpyxl
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind
from scipy.stats import pearsonr
import numpy as np
import pandas as pd

# importo datos de excel y paso valores al array arnum
libro = openpyxl.load_workbook('HistRatios.xlsx')
hoja = libro.get_sheet_by_name('ratios')
ar = pd.read_excel('HistRatios.xlsx','ratios',header=0, index_col=None, na_values=['NA'])
arnum=ar.values
headers=list(ar)

# cuento cuantas muestras hay en trampas y sedimentos de BZ y N
sizeTBA=0
for a in arnum[:,0]:
	if a == 'TBA':
		sizeTBA+=1
sizeTN=0
for a in arnum[:,0]:
	if a == 'TN':
		sizeTN+=1
sizeSBA=0
for a in arnum[:,0]:
	if a == 'SBA':
		sizeSBA+=1
sizeSN=0
for a in arnum[:,0]:
	if a == 'SN':
		sizeSN+=1

print(sizeTBA, sizeTN, sizeSBA, sizeSN)

# creo el fondo de la figura
fig=plt.figure(facecolor='white', figsize=(12,6))
arnum2 = arnum[:,1:6].astype(float)
csfont = {'fontname':'Liberation Sans'}

# agrego el boxplot
box1 = fig.add_axes([0.05, 0.10, 0.72, 0.8])
bprop1 = dict(linewidth = 2, edgecolor = 'k', facecolor = 'k')
wprop1 = dict(linewidth = 2, linestyle = '-', color = 'k')
mprop1 = dict(linestyle = '-',linewidth = 2, color = 'w')
pprop1 = dict(marker = 'o', markeredgecolor = 'w', markerfacecolor = 'w')
cap1 = dict(linewidth = 2, color = 'k')
box1.boxplot([arnum2[0:24,1],arnum2[0:24,0],arnum2[0:24,2],arnum2[0:24,3]], vert = True, positions = (3,8,13,18), notch = False, patch_artist = True, showmeans = True, showfliers = False, boxprops = bprop1, whiskerprops = wprop1, medianprops = mprop1, meanprops = pprop1, capprops = cap1)
bprop2 = dict(linewidth = 2, edgecolor = 'k')
wprop2 = dict(linewidth = 2, linestyle = '-', color = 'k')
mprop2 = dict(linestyle = '-',linewidth = 2, color = 'k')
pprop2 = dict(marker = 'o', markeredgecolor = 'k', markerfacecolor = 'k')
cap2 = dict(linewidth = 2, color = 'k')
box1.boxplot([arnum2[57:67,1],arnum2[57:67,0],arnum2[57:67,2],arnum2[57:67,3]], vert = True, positions = (4,9,14,19), notch = False, patch_artist = True, showmeans = True, showfliers = False, boxprops = bprop2, whiskerprops = wprop2, medianprops = mprop2, meanprops = pprop2, capprops = cap2)
bprop3 = dict(linewidth = 2, edgecolor = 'grey', facecolor = 'grey')
wprop3 = dict(linewidth = 2, linestyle = '-', color = 'grey')
mprop3 = dict(linestyle = '-',linewidth = 2, color = 'w')
pprop3 = dict(marker = 'o', markeredgecolor = 'w', markerfacecolor = 'w')
cap3 = dict(linewidth = 2, color = 'grey')
box1.boxplot([arnum2[24:57,1],arnum2[24:57,0],arnum2[24:57,2],arnum2[24:57,3]], vert = True, positions = (1,6,11,16), notch = False, patch_artist = True, showmeans = True, showfliers = False, boxprops = bprop3, whiskerprops = wprop3, medianprops = mprop3, meanprops = pprop3, capprops = cap3)
bprop4 = dict(linewidth = 2, edgecolor = 'grey')
wprop4= dict(linewidth = 2, linestyle = '-', color = 'grey')
mprop4 = dict(linestyle = '-',linewidth = 2, color = 'grey')
pprop4 = dict(marker = 'o', markeredgecolor = 'grey', markerfacecolor = 'grey')
cap4 = dict(linewidth = 2, color = 'grey')
box1.boxplot([arnum2[67:72,1],arnum2[67:72,0],arnum2[67:72,2],arnum2[67:72,3]], vert = True, positions = (2,7,12,17), notch = False, patch_artist = True, showmeans = True, showfliers = False, boxprops = bprop4, whiskerprops = wprop4, medianprops = mprop4, meanprops = pprop4, capprops = cap4)

# borro ejes, ticks y labels
box1.spines['top'].set_visible(False)
box1.spines['bottom'].set_visible(False)
box1.spines['right'].set_visible(False)
box1.tick_params(length=0, which='both')
box1.axes.get_xaxis().set_visible(False)
# agrego vertical lines
plt.vlines(5,0,1,linestyle = '--')
plt.vlines(10,0,1,linestyle = '--')
plt.vlines(15,0,1,linestyle = '--')
# formateo ejes y ticks
plt.ylim(0,1)
plt.yticks(np.arange(0,1.1,0.5), size = 16, **csfont)
plt.xlim(0,20)

box2 = fig.add_axes([0.80, 0.10, 0.15, 0.8])
box2.boxplot([arnum2[24:57,4]], vert = True, positions = ([0.2]), notch = False, patch_artist = True, showmeans = True, showfliers = False, boxprops = bprop3, whiskerprops = wprop3, medianprops = mprop3, meanprops = pprop3, capprops = cap3)
box2.boxplot([arnum2[0:24,4]], vert = True, positions = ([0.8]), notch = False, patch_artist = True, showmeans = True, showfliers = False, boxprops = bprop1, whiskerprops = wprop1, medianprops = mprop1, meanprops = pprop1, capprops = cap1)
box2.boxplot([arnum2[67:72,4]], vert = True, positions = ([0.5]), notch = False, patch_artist = True, showmeans = True, showfliers = False, boxprops = bprop4, whiskerprops = wprop4, medianprops = mprop4, meanprops = pprop4, capprops = cap4)
box2.boxplot([arnum2[57:67,4]], vert = True, positions = ([1.1]), notch = False, patch_artist = True, showmeans = True, showfliers = False, boxprops = bprop2, whiskerprops = wprop2, medianprops = mprop2, meanprops = pprop2, capprops = cap2)
# borro ejes, ticks y labels
box2.spines['top'].set_visible(False)
box2.spines['bottom'].set_visible(False)
box2.spines['right'].set_visible(False)
box2.tick_params(length=0, which='both')
box2.axes.get_xaxis().set_visible(False)
# formateo ejes y ticks
plt.ylim(0.5,1)
plt.yticks(np.arange(0.5,1.01,0.25), size = 16, **csfont)
plt.xlim(0,1.2)

# agrego titles
box1.text(0.7,1.03,r'Fecal/Phyto', fontsize = 18, **csfont)
box1.text(6.2,1.03,r'Cop/epiCop', fontsize = 18, **csfont)
box1.text(10.5,1.03,r'Cop/ethylCop', fontsize = 18, **csfont)
box1.text(16,1.03,r'Sito/ethylCop', fontsize = 18, **csfont)
box1.text(21.7,1.03,r'Chnol/Chrol', fontsize = 18, **csfont)

print("Geographical differences:\nTraps:")
print("Fecal/Phyto: ", ttest_ind(arnum2[0:24,1],arnum2[25:57,1]))
print("BA vs N: %.2f %s %.3f vs %.2f %s %.2f"%((np.mean(arnum2[0:24,1])), u"\u00b1", (np.std(arnum2[0:24,1], dtype=float,ddof=1)),(np.mean(arnum2[25:57,1])), u"\u00b1", (np.std(arnum2[25:57,1], dtype=float,ddof=1)))).encode('utf-8')

print("Cop/Epi: ", ttest_ind(arnum2[0:24,0],arnum2[25:57,0]))
print("BA vs N: %.2f %s %.2f vs %.2f %s %.2f"%((np.mean(arnum2[0:24,0])), u"\u00b1", (np.std(arnum2[0:24,0], dtype=float,ddof=1)),(np.mean(arnum2[25:57,0])), u"\u00b1", (np.std(arnum2[25:57,0], dtype=float,ddof=1)))).encode('utf-8')

print("Cop/eCop: ", ttest_ind(arnum2[0:24,2],arnum2[25:57,2]))
print("BA vs N: %.2f %s %.3f vs %.2f %s %.2f"%((np.mean(arnum2[0:24,2])), u"\u00b1", (np.std(arnum2[0:24,2], dtype=float,ddof=1)),(np.mean(arnum2[25:57,2])), u"\u00b1", (np.std(arnum2[25:57,2], dtype=float,ddof=1)))).encode('utf-8')

print("Sito/eCop: ", ttest_ind(arnum2[0:24,3],arnum2[25:57,3]))
print("BA vs N: %.2f %s %.2f vs %.2f %s %.2f"%((np.mean(arnum2[0:24,3])), u"\u00b1", (np.std(arnum2[0:24,3], dtype=float,ddof=1)),(np.mean(arnum2[25:57,3])), u"\u00b1", (np.std(arnum2[25:57,3], dtype=float,ddof=1)))).encode('utf-8')

print("Chnol/Chrol: ", ttest_ind(arnum2[0:24,4],arnum2[25:57,4]))
print("BA vs N: %.2f %s %.3f vs %.3f %s %.3f"%((np.mean(arnum2[0:24,4])), u"\u00b1", (np.std(arnum2[0:24,4], dtype=float,ddof=1)),(np.mean(arnum2[25:57,4])), u"\u00b1", (np.std(arnum2[25:57,4], dtype=float,ddof=1)))).encode('utf-8')

print("\nSediments:")
print("Fecal/Phyto: ", ttest_ind(arnum2[57:67,1],arnum2[67:72,1]))
print("BA vs N: %.2f %s %.3f vs %.2f %s %.2f"%((np.mean(arnum2[57:67,1])), u"\u00b1", (np.std(arnum2[57:67,1], dtype=float,ddof=1)),(np.mean(arnum2[67:72,1])), u"\u00b1", (np.std(arnum2[67:72,1], dtype=float,ddof=1)))).encode('utf-8')

print("Cop/Epi: ", ttest_ind(arnum2[57:67,0],arnum2[67:72,0]))
print("BA vs N: %.2f %s %.2f vs %.2f %s %.2f"%((np.mean(arnum2[57:67,0])), u"\u00b1", (np.std(arnum2[57:67,0], dtype=float,ddof=1)),(np.mean(arnum2[67:72,0])), u"\u00b1", (np.std(arnum2[67:72,0], dtype=float,ddof=1)))).encode('utf-8')

print("Cop/eCop: ", ttest_ind(arnum2[57:67,2],arnum2[67:72,2]))
print("BA vs N: %.2f %s %.3f vs %.2f %s %.2f"%((np.mean(arnum2[57:67,2])), u"\u00b1", (np.std(arnum2[57:67,2], dtype=float,ddof=1)),(np.mean(arnum2[67:72,2])), u"\u00b1", (np.std(arnum2[67:72,2], dtype=float,ddof=1)))).encode('utf-8')

print("Sito/eCop: ", ttest_ind(arnum2[57:67,3],arnum2[67:72,3]))
print("BA vs N: %.2f %s %.2f vs %.2f %s %.2f"%((np.mean(arnum2[57:67,3])), u"\u00b1", (np.std(arnum2[57:67,3], dtype=float,ddof=1)),(np.mean(arnum2[67:72,3])), u"\u00b1", (np.std(arnum2[67:72,3], dtype=float,ddof=1)))).encode('utf-8')

print("Chnol/Chrol: ", ttest_ind(arnum2[57:67,4],arnum2[67:72,4]))
print("BA vs N: %.2f %s %.3f vs %.3f %s %.3f"%((np.mean(arnum2[57:67,4])), u"\u00b1", (np.std(arnum2[57:67,4], dtype=float,ddof=1)),(np.mean(arnum2[67:72,4])), u"\u00b1", (np.std(arnum2[67:72,4], dtype=float,ddof=1)))).encode('utf-8')

plt.show()
