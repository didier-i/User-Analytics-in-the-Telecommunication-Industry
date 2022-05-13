import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

class Clean_df:
    def __init__(self, df):
        self.df = df
        
    def percent_missing(self, df):
    total_cells = np.product(df.shape)
    total_missing = np.sum(df.isna().sum())
    print(f'There is {round((total_missing/total_cells)*100, 1)}% missing values') 
    
    def drop_50percent_missing(self, df):
    for i in df.columns:
        if df[i].isna().sum() >= df.shape[0]/2:
            df.drop(labels=i, axis=1, inplace=True)
            print(f'Dropped column: {i}')
    
    def ffill_missing(self, df, col):
        df[col] = df[col].fillna(method='ffill')

    def bfill_missing(self, df, col):
        df[col] = df[col].fillna(method='bfill')
    
    def fill_missing(df):
        df_numeric = df.select_dtypes(include='float')
        for i in df_numeric.columns:
            if df_numeric[i].skew() < 0.5 and df_numeric[i].skew() > -0.5:
                df[i].fillna(df[i].median(), inplace=True)
            else:
                df[i].fillna(df[i].mean(), inplace=True) 
        bfill_missing(df, 'Start')
        ffill_missing(df, 'End')
    
    