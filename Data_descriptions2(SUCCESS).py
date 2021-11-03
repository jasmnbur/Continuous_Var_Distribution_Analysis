#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
hpums = pd.read_csv(r'H:\Data\psam_husa.csv')


# In[25]:


variables = ['WGTP','TAXAMT','SMOCP','OCPIP','NRC','NOC','NPF','HINCP','GRPIP','GRNTP','FINCP','WATP','VALP','SMP','RNTP','RMSP','MRGP','MHP','INSP','GASP','FULP','ELEP','CONP','NP','BDSP']


# In[181]:


from matplotlib.pyplot import figure
import warnings
warnings.simplefilter(action="ignore", category=FutureWarning)

def dist_analyze(x,df):
    
    variable = df[x]
    
    print("Variable: " + x)
    print("count: " + str(variable.count()))
    print("median: " + str(variable.median()))
    print("mean: " + str(variable.mean()))
    print("std: " + str(variable.std()))
    print("min: " + str(variable.min()))
    print("max: " + str(variable.max()))
    print("")
    
    figure(figsize=(15, 5))
    plt.hist(df[x], bins=40)
    plt.xlabel(x, fontsize=10)
    plt.ylabel("Frequency", fontsize=10)
    plt.title(x + " Distribution", fontsize=12)
    plt.show()
    sns.displot(df[x], kde=True, height=5, aspect=12.5/5)
    plt.show()
    sns.boxplot(df[x], palette="Set2", width=0.2)
    plt.show()
    print("")
    
    return;


# In[184]:


dist_analyze("NP",hpums)


# In[182]:


dist_analyze("RNTP",hpums)


# In[32]:


import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style="whitegrid")


# In[15]:


prop_tax = hpums['TAXAMT']
print(prop_tax.describe())


# In[185]:


for x in variables:
    dist_analyze(x, hpums)


# In[187]:


python -m pip install -U notebook-as-pdf
pyppeteer-install


# In[36]:


# f, ax = plt.subplots(figsize=(8,8))

# sns.violinplot(data=hpums, x="NP", palette="Set3", inner="points", bw =.2, cut=2, linewidth=3)
# sns.despine(left=True)


# In[35]:


# import numpy as np
# np.random.seed(10)
# collectn_1 = np.random.normal(100, 10, 200)
# collectn_2 = np.random.normal(80, 30, 200)
# collectn_3 = np.random.normal(90, 20, 200)
# collectn_4 = np.random.normal(70, 25, 200)

# ## combine these different collections into a list
# data_to_plot = [collectn_1, collectn_2, collectn_3, collectn_4]

# # Create a figure instance
# fig = plt.figure()

# # Create an axes instance
# ax = fig.add_axes([0,0,1,1])

# # Create the boxplot
# bp = ax.violinplot(data_to_plot)
# plt.show()


# In[164]:


# plt.hist(hpums['TAXAMT'], bins=20)


# In[165]:


# sns.displot(hpums['TAXAMT'], kde=True)


# In[166]:


# from matplotlib.pyplot import figure
# figure(figsize=(15, 5))
# sns.boxplot(hpums['TAXAMT'], palette="Set2", width=0.2)


# In[167]:


# print(hpums['TAXAMT'].count())
# print(hpums['TAXAMT'].median())
# print(hpums['TAXAMT'].mean())
# print(hpums['TAXAMT'].std())
# print(hpums['TAXAMT'].min())
# print(hpums['TAXAMT'].max())


# In[183]:


# def dist_visual(list,df):
#     for x in list:
#         variable = df[x]
#         print("Variable: " + x)
#         median = str(variable.median())
#         print("median: " + median)
#         print(variable.describe())
#         print("")
#     for x in list:
#         plt.hist(df[x], bins=20)
#         plt.xlabel(x, fontsize=10)
#         plt.ylabel("Frequency", fontsize=10)
#         plt.title(x + " Distribution", fontsize=12)
#         plt.show()
#     for x in list:
#         sns.distplot(df[x])
#     for x in list:
#         sns.boxplot(df[x], palette="Set2", width=0.2)
#     return;

# test = ['WGTP','TAXAMT','SMOCP']
# dist_visual(test,hpums)


# In[ ]:




