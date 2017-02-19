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
EBA = histo.stem(cols+0.6, arnum[4,2:13], linefmt='r-',mec='r', lw=0, markerfmt='rv', basefmt='r-',edgecolor=None)
csfont = {'fontname':'Liberation Sans'}
histo.set_ylabel('Vertical flux (mg.$\mathregular{cm^{-2}.year^{-1}}$)', size=18,**csfont)
plt.ylim(0,90)
plt.xlim(0,11)
plt.yticks(np.arange(0,81,20), size = 14, **csfont)
histo.tick_params(length=0, which='both')
histo.set_xticks(cols+0.5)
histo.set_xticklabels(headers[2:13], rotation = 90, size=14,**csfont)
plt.setp(histo.get_xticklabels(),visible=False)

for i,j,k in zip(cols,arnum[8,2:13],arnum[4,2:13]):
	histo.annotate((j),xy=(i+0.22,4), size =11, rotation=90)

plt.gca().invert_yaxis()

# creo flux plot
hBA = histo.twinx()
hBA.bar(cols+wid, arnum[2,2:13], wid, color = 'r', linewidth=0)
hBA.set_ylabel('Accumulation Efficiency (%)', size=18,**csfont)
plt.ylim(0,50)
plt.xlim(0,11)
plt.yticks(np.arange(0,51,10), size = 14, **csfont)

# N

#histo efficiencies N
histo2 = fig.add_axes([0.15, 0.2, 0.7, 0.35])
cols = np.arange(11) # ctdad de barras (= esteroles)
wid = 0.4
EN = histo2.stem(cols+0.6, arnum[6,2:13], linefmt='g-', markerfmt='gv', basefmt='g-')
csfont = {'fontname':'Liberation Sans'}
histo2.set_ylabel('Vertical flux (ug.$\mathregular{cm^{-2}.year^{-1}}$)', size=18,**csfont)
plt.xlim(0,11)
plt.ylim(0,40)
plt.yticks(np.arange(0,31,10), size = 14, **csfont)
histo2.tick_params(length=0, which='both')
histo2.set_xticks(cols+0.5)
histo2.set_xticklabels(headers[2:13], rotation = 90, size=14,**csfont)
# coloreo las ticklabels segun categoria
labelcol = ['saddlebrown','saddlebrown','saddlebrown','saddlebrown','limegreen','limegreen','limegreen','limegreen','grey','dodgerblue','dodgerblue']
[lab.set_color(i) for (i,lab) in zip(labelcol, histo2.xaxis.get_ticklabels())] 
fontdict = dict(color='red',weight='heavy',**csfont)
fontdictN2 = dict(color='g',weight='heavy',**csfont)

for i,j,k in zip(cols,arnum[9,2:13],arnum[6,2:13]):
	histo2.annotate((j),xy=(i+0.22,2), size =11, rotation=90)

plt.gca().invert_yaxis()

# creo flux plot N
hN = histo2.twinx()
hN.bar(cols+wid, arnum[3,2:13], wid, color = 'g', linewidth=0)
hN.set_ylabel('Accumulation Efficiency (%)', size=18,**csfont)
plt.ylim(0,8)
plt.xlim(0,11)
plt.yticks(np.arange(0,8.1,2), size = 14, **csfont)






plt.show()

