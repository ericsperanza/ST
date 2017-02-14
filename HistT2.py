# histograma c/tortas de traps
from __future__ import print_function
import openpyxl
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook
import matplotlib.ticker as ticker
from scipy import interpolate 
from scipy import signal
import numpy as np
import pandas as pd

# importo datos de excel y paso valores al array arnum
libro = openpyxl.load_workbook('HistRatios.xlsx')
ardw = pd.read_excel('HistRatios.xlsx','dw',header=0, index_col=None, na_values=['NA'])
arnumdw=ardw.values
headers=list(ardw)
arpp = pd.read_excel('HistRatios.xlsx','pp',header=0, index_col=None, na_values=['NA'])
arnumpp=arpp.values
arsed = pd.read_excel('HistRatios.xlsx','sed',header=0, index_col=None, na_values=['NA'])
arnumsed=arsed.values
#arfec = pd.read_excel('HistRatios.xlsx','fec',header=0, index_col=None, na_values=['NA'])
#arnumfec= arfec.values

# cuento cuantas muestras hay en BZ y N
sizeBZ=0
for a in arnumdw[:,0]:
	if a == 'BZ':
		sizeBZ+=1
sizeN=0
for a in arnumdw[:,0]:
	if a == 'N':
		sizeN+=1
print(sizeBZ, sizeN)

# calculo medias
meandevBZ = np.empty((2,0))
meandevN = np.empty((2,0))

for a in range(1,18):
	meandevBZ = (np.append(meandevBZ,[[np.mean(arnumdw[0:sizeBZ,a])],[np.std(arnumdw[0:sizeBZ,a],dtype=float,ddof=1)]], axis = 1))
for a in range(1,18):
	meandevN = (np.append(meandevN,[[np.mean(arnumdw[sizeBZ:(sizeBZ+sizeN),a])],[np.std(arnumdw[sizeBZ:(sizeBZ+sizeN),a],dtype=float,ddof=1)]], axis = 1))

# creo el fondo de la figura
fig=plt.figure(facecolor='white', figsize=(7,13.2))

#creo el histograma
histo = fig.add_axes([0.18, 0.59, 0.8, 0.25])
cols = np.arange(17) # ctdad de barras(= esteroles)
ancho = 0.3
eb = {'linewidth':2,'capsize':4,'ecolor':'r'}
eb2 = {'linewidth':2,'capsize':4,'ecolor':'g'}
#eb3 = {'linewidth':2,'capsize':4,'ecolor':'brown'}
rect1 = histo.bar(cols,meandevBZ[0,:],ancho, color = 'r', yerr=[np.zeros(17), meandevBZ[1,:]], error_kw=eb, linewidth=0, log=True)
rect2 = histo.bar(cols+ancho,meandevN[0,:], ancho, color = 'g', yerr = [np.zeros(17),meandevN[1,:]], error_kw = eb2, linewidth=0, log=True)
#rect3 = histo.bar(cols+ancho*2,arnumfec[0,1:18], ancho, color = 'brown', yerr = [np.zeros(17),arnumfec[1,1:18]], error_kw = eb3, linewidth=0, log=True)
# labels y ejes
csfont = {'fontname':'Liberation Sans'}
histo.set_ylabel('Trap sterols (ug.$\mathregular{g^{-1}}$)', size=18,**csfont)
plt.ylim(0,10000)
plt.xlim(0,17)
histo.yaxis.set_major_formatter(ticker.FuncFormatter(lambda y,pos: ('{{:.{:1d}f}}'.format(int(np.maximum(-np.log10(y),0)))).format(y)))
plt.yticks(size = 16,**csfont)
histo.spines['top'].set_visible(False)
histo.spines['right'].set_visible(False)
histo.tick_params(length=0, which='both')
histo.set_xticks(cols+ancho)
histo.set_xticklabels(headers[1:18], rotation = 90, size=14,**csfont)
plt.setp(histo.get_xticklabels(),visible=False)

#creo las tortas
tortaBZ = fig.add_axes([0.21,0.77,0.265,0.265])
tortaN = fig.add_axes([0.69,0.77,0.265,0.265])
categ = ('Fecal','Phytosterols','Cholesterol','Others')
colors = ['saddlebrown','limegreen','grey','dodgerblue']
colorsN = ['limegreen','saddlebrown','dodgerblue','grey']
BZ=[(np.mean(arnumpp[0:sizeBZ,19])),(np.mean(arnumpp[0:sizeBZ,20])),(np.mean(arnumpp[0:sizeBZ,14])),(np.mean(arnumpp[0:sizeBZ,21]))]
print(BZ)
N=[(np.mean(arnumpp[sizeBZ:(sizeBZ+sizeN),20])),(np.mean(arnumpp[sizeBZ:(sizeBZ+sizeN),19])),(np.mean(arnumpp[sizeBZ:(sizeBZ+sizeN),21])),(np.mean(arnumpp[sizeBZ:(sizeBZ+sizeN),14]))]
print(N)
tortaBZ.pie(BZ,startangle=40, colors=colors,wedgeprops={'linewidth':0})
tortaN.pie(N,startangle=245, colors=colorsN,wedgeprops={'linewidth':0})
tortaBZ.set_aspect('equal')
tortaN.set_aspect('equal')
# agrego los rotulos
tortaBZ.text(1.8,0.75, r'Fecal', fontsize=18,**csfont)
tortaBZ.arrow(0.66,0.76,1.08,0.1,head_width=0.02,width=0.01,head_length=0,clip_on=False,color='black',edgecolor='black')
tortaBZ.arrow(2.63,0.85,1.65,0.1,head_width=0.02,width=0.01,head_length=0,clip_on=False,color='black',edgecolor='black')
tortaBZ.text(1.7,0.36, r'Others', fontsize=18,**csfont)
tortaBZ.arrow(0.82,0.53,0.8,-0.05,head_width=0.02,width=0.01,head_length=0,clip_on=False,color='black',edgecolor='black')
tortaBZ.arrow(2.73,0.45,1.22,0.25,head_width=0.02,width=0.01,head_length=0,clip_on=False,color='black',edgecolor='black')
tortaBZ.text(1.45,-0.14, r'Cholesterol', fontsize=18,**csfont)
tortaBZ.arrow(0.96,0.00,0.4,0.00,head_width=0.02,width=0.01,head_length=0,clip_on=False,color='black',edgecolor='black')
tortaBZ.arrow(3.15,0,0.65,0,head_width=0.02,width=0.01,head_length=0,clip_on=False,color='black',edgecolor='black')
tortaBZ.text(1.4,-1.06, r'Phytosterols', fontsize=18,**csfont)
tortaBZ.arrow(0.74,-0.6,0.6,-0.33,head_width=0.02,width=0.01,head_length=0,clip_on=False,color='black',edgecolor='black')
tortaBZ.arrow(3.26,-0.95,1.4,0,head_width=0.02,width=0.01,head_length=0,clip_on=False,color='black',edgecolor='black')
# coloreo las ticklabels segun categoria
labelcol =['saddlebrown','saddlebrown','saddlebrown','saddlebrown','saddlebrown','limegreen','limegreen','limegreen','limegreen','limegreen','limegreen','limegreen','dodgerblue','grey','dodgerblue','dodgerblue','dodgerblue']
[lab.set_color(i) for (i,lab) in zip(labelcol, histo.xaxis.get_ticklabels())] 
fontdict = dict(color='red',weight='heavy',**csfont)
tortaBZ.text(-1.5,0.7,r'BA', fontsize=22,fontdict=fontdict)
fontdictN = dict(color='g',weight='heavy',**csfont)
tortaN.text(0.91,0.7,r'N', fontsize=22,fontdict=fontdictN)

"""
SEDIMENTS
"""

# cuento cuantas muestras hay en BZ y N
sBZ=0
sN=0
for a in arnumsed[:,0]:
	if a == 'BA':
		sBZ+=1
	else:
		sN+=1

# calculo medias sedimentos
meansedBZ = np.empty((2,0))
meansedN = np.empty((2,0))

for i in range(1,18):
	meansedBZ = (np.append(meansedBZ,[[np.mean(arnumsed[0:sBZ,i])],[np.std(arnumsed[0:sBZ,i],dtype=float,ddof=1)]],axis=1))
	meansedN = (np.append(meansedN,[[np.mean(arnumsed[sBZ:(sBZ+sN),i])],[np.std(arnumsed[sBZ:(sBZ+sN),i],dtype=float,ddof=1)]], axis = 1))

#creo el histograma sedimentos
ancho=0.3
histo2 = fig.add_axes([0.18, 0.21, 0.8, 0.25])
rect4 = histo2.bar(cols,meansedBZ[0,:],ancho, color = 'r', yerr=[np.zeros(17), meansedBZ[1,:]], error_kw=eb, linewidth=0, log=True)
rect5 = histo2.bar(cols+ancho,meansedN[0,:], ancho, color = 'g', yerr = [np.zeros(17),meansedN[1,:]], error_kw = eb2, linewidth=0, log=True)
# labels y ejes
csfont = {'fontname':'Liberation Sans'}
histo2.set_ylabel('Sediment sterols (ug.$\mathregular{g^{-1}}$)', size=18,**csfont)
plt.ylim(0,10000)
plt.xlim(0,17)
histo2.yaxis.set_major_formatter(ticker.FuncFormatter(lambda y,pos: ('{{:.{:1d}f}}'.format(int(np.maximum(-np.log10(y),0)))).format(y)))
plt.yticks(size = 16,**csfont)
histo2.spines['top'].set_visible(False)
histo2.spines['right'].set_visible(False)
histo2.tick_params(length=0, which='both')
histo2.set_xticks(cols+ancho)
histo2.set_xticklabels(headers[1:18], rotation = 90, size=14,**csfont)

#creo las tortas
tortaBZ2 = fig.add_axes([0.21,0.36,0.265,0.265])
tortaN2 = fig.add_axes([0.69,0.36,0.265,0.265])
BZ2=[(np.mean(arnumsed[0:sBZ,18])),(np.mean(arnumsed[0:sBZ,19])),(np.mean(arnumsed[0:sBZ,21])),(np.mean(arnumsed[0:sBZ,20]))]
print(BZ2)
N2=[(np.mean(arnumsed[sBZ:(sBZ+sN),19])),(np.mean(arnumsed[sBZ:(sBZ+sN),18])),(np.mean(arnumsed[sBZ:(sBZ+sN),20])),(np.mean(arnumsed[sBZ:(sBZ+sN),21]))]
print(N2)
tortaBZ2.pie(BZ2,startangle=40, colors=colors,wedgeprops={'linewidth':0})
tortaN2.pie(N2,startangle=245, colors=colorsN,wedgeprops={'linewidth':0})
tortaBZ2.set_aspect('equal')
tortaN2.set_aspect('equal')

# coloreo las ticklabels segun categoria
labelcol = ['saddlebrown','saddlebrown','saddlebrown','saddlebrown','saddlebrown','limegreen','limegreen','limegreen','limegreen','limegreen','limegreen','limegreen','grey','dodgerblue','dodgerblue','dodgerblue','dodgerblue']
[lab.set_color(i) for (i,lab) in zip(labelcol, histo2.xaxis.get_ticklabels())] 
fontdict = dict(color='red',weight='heavy',**csfont)
#tortaBZ2.text(-1.5,0.3,r'BA', fontsize=22,fontdict=fontdict)
fontdictN2 = dict(color='g',weight='heavy',**csfont)
#tortaN.text(0.91,0.3,r'N', fontsize=22,fontdict=fontdictN)
#print(arnumfec[0,1:18])

plt.show()
