# Scatter1.py
from __future__ import print_function
import openpyxl
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind
from scipy.stats import pearsonr
import numpy as np
import pandas as pd

# importo datos de excel y paso valores al array arnum
libro = openpyxl.load_workbook('compWC.xlsx')
hoja = libro.get_sheet_by_name('h3')
ar = pd.read_excel('compWC.xlsx','h3', header=0, index_col=None, na_values=['NA'])
arnum=ar.values

# creo el fondo de la figura
fig=plt.figure(facecolor='white', figsize=(9,14))
csfont = {'fontname':'Liberation Sans'}

flux = arnum[:,2]
disch = arnum[:,15]

#plot todos transparente
#plot BA 
#plot N
#best fit for todos

