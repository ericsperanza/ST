#MultRegr.py
from __future__ import print_function
import openpyxl
import matplotlib.pyplot as plt
import matplotlib.ticker as tick
from matplotlib import rcParams
from scipy.stats import ttest_ind
from scipy.stats import pearsonr
from scipy.optimize import curve_fit
from sklearn.feature_selection import f_regression
import numpy as np
import pandas as pd

# importo datos de excel y paso valores al array arnum
libro = openpyxl.load_workbook('compWC.xlsx')
hoja = libro.get_sheet_by_name('h4')
ar = pd.read_excel('compWC.xlsx','h4', header=0, index_col=None, na_values=['NA'])
arnum=ar.values

x = arnum[:,4:14].astype(float)
y = arnum[:,1].astype(float)

Fs,vals = f_regression(x, y, center=True)

print(Fs)
print(vals)

