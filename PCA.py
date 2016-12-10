# PCA.py
from __future__ import print_function
#import openpyxl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.decomposition import PCA 

# importo datos de excel y paso valores al array arnum
#libro = openpyxl.load_workbook('MVA.xlsx')
#hoja = libro.get_sheet_by_name('data')
ar = pd.read_excel('MVA.xlsx','data', header=0, index_col=None, na_values=['NA'])
arnum=ar.values

dat = arnum[:,2:14]

pca = PCA(n_components = 2, whiten = True)
dat_r = pca.fit(dat).transform(dat)

print (pca.explained_variance_ratio_)
plt.scatter(dat_r[:,0],dat_r[:,1])
plt.scatter(dat_r[0:23,0],dat_r[0:23,1],color = 'red')
plt.scatter(dat_r[24:57,0],dat_r[24:57,1],color = 'green')
var= pca.components_
for i in range(12):
	plt.scatter(var[0,i],var[1,i], color = 'blue')
plt.show()
