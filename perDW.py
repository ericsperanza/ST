# perDW.py
import openpyxl
from scipy.stats import pearsonr
import pandas as pd
import numpy as np

# importo datos de excel y paso valores al array arnum
libro = openpyxl.load_workbook('perDW.xlsx')
hoja = libro.get_sheet_by_name('BA')
ar = pd.read_excel('perDW.xlsx','BA', header=0, index_col=None, na_values=['NA'])
arnum=ar.values

libro2 = openpyxl.load_workbook('perDW.xlsx')
hoja2 = libro.get_sheet_by_name('N')
ar2 = pd.read_excel('perDW.xlsx','N', header=0, index_col=None, na_values=['NA'])
arnum2=ar2.values


headers = []
for i in ar.columns:
	headers.append(i)

print("BA:")
print("DW concentration vs. percentage (percent, r, p-value)")
for i in range(1,18):
	print("%s: %.2f %s %.2f; r: %.2f, %.3f "%(headers[i], (np.mean(arnum[24:48,i])), u"\u00b1", (np.std(arnum[24:48,i],dtype=float,ddof=1)), (pearsonr(arnum[0:24,i],arnum[24:48,i]))[0], (pearsonr(arnum[0:24,i],arnum[24:48,i]))[1] ) ).encode('utf-8')

print("\nN:")
print("DW concentration vs. percentage (percent, r, p-value)")
for i in range(1,18):
	print("%s: %.2f %s %.2f; r: %.2f, %.3f "%(headers[i], (np.mean(arnum2[33:66,i])), u"\u00b1", (np.std(arnum2[33:66,i],dtype=float,ddof=1)), (pearsonr(arnum2[0:33,i],arnum2[33:66,i]))[0], (pearsonr(arnum2[0:33,i],arnum2[33:66,i]))[1] ) ).encode('utf-8')

# Para que guarde el resultado: python perDW.py > output.txt

