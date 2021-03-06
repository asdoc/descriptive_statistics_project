# %load q03_pearson_correlation/build.py
# Default Imports
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataframe_1 = pd.read_csv('data/house_prices_multivariate.csv')
dataframe_2 = pd.read_csv('data/house_prices_copy.csv')


def correlation():
    coef = np.corrcoef(x = dataframe_1['SalePrice'], y = dataframe_2['SalePrice'])
    return coef[0][1]
    


