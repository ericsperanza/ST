#AccEff.py
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
#import openpyxl

# importo datos de excel y paso valores al array arnum
#libro = openpyxl.load_workbook('sedDegr.xlsx')
ar = pd.read_excel('sedDegr.xlsx','Graph',header=0, index_col=None, na_values=['NA'])
arnum=ar.values
headers=list(ar)

# creo el fondo de la figura
fig=plt.figure(facecolor='white', figsize=(6,12))

#histo efficiencies BA
histo = fig.add_axes([0.15, 0.6, 0.7, 0.35])
cols = np.arange(11) # ctdad de barras (= esteroles)
wid = 0.6
hBA = histo.bar(cols+wid, arnum[0,2:13], wid, color = 'r', linewidth=0)
csfont = {'fontname':'Liberation Sans'}
#histo.set_ylabel('Accumulation Efficiency (%)', size=18,**csfont)
plt.ylim(0,40)
plt.xlim(0,11)
plt.yticks(np.arange(0,41,20), size = 18, **csfont)
histo.tick_params(length=0, which='both')
histo.set_xticks(cols+0.5)
histo.set_xticklabels(headers[2:13], rotation = 90, size=14,**csfont)
plt.setp(histo.get_xticklabels(),visible=False)
"""
# creo flux plot
EBA = histo.twinx()
#EBA.bar(cols, arnum[4,2:13], wid, color = 'b')
EBA.stem(cols+0.6, arnum[4,2:13], linefmt='k-', markerfmt='kv', basefmt='r-')
EBA.set_ylabel('Vertical flux (mg.$\mathregular{cm^{-2}.year^{-1}}$)', size=18,**csfont)
plt.ylim(0,90)
plt.xlim(0,11)
plt.yticks(np.arange(0,81,20), size = 14, **csfont)

plt.gca().invert_yaxis()
"""
# N

#histo efficiencies N
histo2 = fig.add_axes([0.15, 0.2, 0.7, 0.35])
cols = np.arange(11) # ctdad de barras (= esteroles)
wid = 0.6
hBA = histo2.bar(cols+wid, arnum[1,2:13], wid, color = 'g', linewidth=0)
csfont = {'fontname':'Liberation Sans'}
#histo2.set_ylabel('Accumulation Efficiency (%)', size=18,**csfont)
plt.ylim(0,10)
plt.xlim(0,11)
plt.yticks(np.arange(0,11,5), size = 18, **csfont)
histo2.tick_params(length=0, which='both')
histo2.set_xticks(cols+0.5)
histo2.set_xticklabels(headers[2:13], rotation = 90, size=16,**csfont)
# coloreo las ticklabels segun categoria
labelcol = ['saddlebrown','saddlebrown','saddlebrown','saddlebrown','limegreen','limegreen','limegreen','limegreen','grey','dodgerblue','dodgerblue']
[lab.set_color(i) for (i,lab) in zip(labelcol, histo2.xaxis.get_ticklabels())] 
fontdict = dict(color='red',weight='heavy',**csfont)
fontdictN2 = dict(color='g',weight='heavy',**csfont)

"""
# creo flux plot N
EBA = histo2.twinx()
#EBA.bar(cols, arnum[4,2:13], wid, color = 'b')
EBA.stem(cols+0.6, arnum[6,2:13], linefmt='k-', markerfmt='kv', basefmt='r-')
EBA.set_ylabel('Vertical flux (ug.$\mathregular{cm^{-2}.year^{-1}}$)', size=18,**csfont)
plt.ylim(0,40)
plt.xlim(0,11)
plt.yticks(np.arange(0,31,10), size = 14, **csfont)

plt.gca().invert_yaxis()
"""
plt.show()

