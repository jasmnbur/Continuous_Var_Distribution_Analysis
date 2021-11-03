# importing packages
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style="whitegrid")

# to get rid of any annoying future warnings that don't affect the validity of the analysis
import warnings
warnings.simplefilter(action="ignore", category=FutureWarning)

# load ACS 2019 1-year PUMS data into dataframe
hpums = pd.read_csv(r'H:\Data\psam_husa.csv')

# List of variables in question (continouous household variables)
variables = ['WGTP','TAXAMT','SMOCP','OCPIP','NRC','NOC','NPF','HINCP','GRPIP','GRNTP','FINCP','WATP','VALP','SMP','RNTP','RMSP','MRGP','MHP','INSP','GASP','FULP','ELEP','CONP','NP','BDSP']


# Define a function to analyze the distribution of a certain variable in the dataframe
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

# Examples: Number of persons in household & Gross monthly rent
dist_analyze("NP",hpums)
dist_analyze("RNTP",hpums)

# looping function through list of variables
for x in variables:
    dist_analyze(x, hpums)



