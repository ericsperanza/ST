#AccEff.py
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import openpyxl

# importo datos de excel y paso valores al array arnum
libro = openpyxl.load_workbook('sedDegr.xlsx')
ar = pd.read_excel('sedDegr.xlsx','Graph',header=0, index_col=None, na_values=['NA'])
arnum=ar.values
headers=list(ar)

# creo el fondo de la figura
fig=plt.figure(facecolor='white', figsize=(6,12))

#histo efficiencies BA
histo = fig.add_axes([0.15, 0.6, 0.7, 0.35])
cols = np.arange(11) # ctdad de barras (= esteroles)
wid = 0.4
histo.bar(cols+0.2, arnum[2,2:13], 0.6, color = 'k', linewidth=2)
csfont = {'fontname':'Liberation Sans'}
histo.set_ylabel('Accumulation Efficiency (%)', size=18,**csfont)
plt.ylim(0,50)
plt.xlim(0,11)
plt.yticks(np.arange(0,51,10), size = 14, **csfont)
plt.axhline(y=arnum[2,13], xmin=0, xmax=1, hold=None, linestyle = '--', color = 'grey', lw = 2)
histo.tick_params(length=0, which='both')
histo.set_xticks(cols+0.5)
histo.set_xticklabels(headers[2:13], rotation = 90, size=14,**csfont)
plt.setp(histo.get_xticklabels(),visible=False)

"""
for i,j,k in zip(cols,arnum[8,2:13],arnum[4,2:13]):
	histo.annotate((j),xy=(i+0.22,4), size =11, rotation=90)
"""

# creo flux plot
hBA = histo.twinx()
hBA.errorbar(cols+0.5,arnum[4,2:13],yerr=arnum[5,2:13],marker='o', markersize=8,markerfacecolor='w',markeredgecolor='silver',markeredgewidth=2,linestyle='none', lw=2.5,ecolor='silver',capsize=2.5,capthick=2.5)
hBA.set_ylabel('Vertical flux (mg/$\mathregular{cm^{2}/year}$)', size=18,**csfont)
plt.ylim(-50,200)
plt.xlim(0,11)
plt.yticks(np.arange(0,201,50), size = 14, **csfont)
histo.tick_params(length=0, which='both')
histo.set_xticks(cols+0.5)
plt.setp(histo.get_xticklabels(),visible=False)

# N

#histo efficiencies N
histo2 = fig.add_axes([0.15, 0.2, 0.7, 0.35])
cols = np.arange(11) # ctdad de barras (= esteroles)
wid = 0.4
histo2.bar(cols+0.2, arnum[3,2:13], 0.6, color = 'silver', linewidth=2,edgecolor='grey')
histo2.set_ylabel('Accumulation Efficiency (%)', size=18,**csfont)
plt.xlim(0,11)
plt.ylim(0,8)
plt.yticks(np.arange(0,8.1,2), size = 14, **csfont)
histo2.tick_params(length=0, which='both')
histo2.set_xticks(cols+0.5)
histo2.set_xticklabels(headers[2:13], rotation = 90, size=14,**csfont)
plt.axhline(y=arnum[3,13], xmin=0, xmax=1, hold=None, linestyle = '--', color = 'k',lw = 2)

'''
# coloreo las ticklabels segun categoria
labelcol = ['saddlebrown','saddlebrown','saddlebrown','saddlebrown','limegreen','limegreen','limegreen','limegreen','grey','dodgerblue','dodgerblue']
[lab.set_color(i) for (i,lab) in zip(labelcol, histo2.xaxis.get_ticklabels())] 
fontdict = dict(color='red',weight='heavy',**csfont)
fontdictN2 = dict(color='g',weight='heavy',**csfont)
'''

# creo flux plot N
hN = histo2.twinx()
hN.errorbar(cols+0.5,arnum[6,2:13],yerr=arnum[7,2:13],marker='o', markersize=8,markerfacecolor='w',markeredgecolor='grey',markeredgewidth=2,linestyle='none', lw=2.5,ecolor='grey',capsize=4,capthick=2.5)
hN.set_ylabel("Vertical flux (%sg/$\mathregular{cm^{2}/year}$)"%(u"\u03BC"), size=18,**csfont)
plt.ylim(-40,90)
plt.xlim(0,11)
plt.yticks(np.arange(0,91,30), size = 14, **csfont)


plt.show()

