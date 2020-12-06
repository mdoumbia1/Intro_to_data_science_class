#!/usr/bin/env python
# coding: utf-8

# In[1]:

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def impute_age(cols):
    Age = cols[0]
    Pclass = cols[1]
    if pd.isnull(Age):
        if Pclass == 1:
            return 37
        elif Pclass == 2:
            return 29
        else:
            return 24
    else:
        return Age


# In[ ]:


# #To read many csv files
# csv_list = glob.glob("FinanceData/*.csv")

# list_of_dfs = []

# for csv in csv_list:
#     df = pd.read_csv(csv, index_col=None, header=0)
#     list_of_dfs.append(df)


# In[ ]:


# all_df = pd.concat(list_of_dfs)

