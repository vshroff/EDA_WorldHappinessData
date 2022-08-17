# Imports
import pandas as pd
import matplotlib.pyplot as plt

# Funtion Definations
def createTypeColumnList(df_scores):
    col_list=[]
    for value in df_scores:
        if(value >= 7.000):
            col_list.append('Happiest')
        elif(value >= 6.000):
            col_list.append('Happier')
        elif(value >=  5.000):
            col_list.append('Happy')
        else:
            col_list.append('Not_Happy')
    col_list=pd.Series(col_list)
    return col_list

"end of function"

def createCondensedDf(df):
    rows_list=[]
    for type in df['Type'].unique():
       scoreSum = df.loc[df['Type'] == type]['Score'].sum()
       generositySum = df.loc[df['Type'] == type]['Generosity'].sum()
       perceptionsOfCorruptionSum = df.loc[df['Type'] == type]['Perceptions of corruption'].sum() 
       num = len(df.loc[df['Type'] == type])
       avgScore = scoreSum/num
       avgGenorosity = generositySum/num
       avgCorruption = perceptionsOfCorruptionSum/num
       newDict = {'Type': type, 'Avg Score': avgScore, 'Avg Genorosity': avgGenorosity, 'Avg Percept. corruptions': avgCorruption, 'numCountriesInType': num}
       rows_list.append(newDict)
    new_df = pd.DataFrame(rows_list)
    new_df.sort_values(['Avg Score'], ascending=False, inplace=True)

    return new_df

"end of function"

# Reading the csv files - downloaded from Kaggle
df_2019 = pd.read_csv("./00_data_raw/world_happiness_report_2019.csv")
    
# Looking at 2019 year report to examine table
df_2019.info()
df_2019.describe()
df_2019.head()
type(df_2019['Score']).mro()

# Data cleaning
df_2019 = df_2019.rename(columns={'Country or region':'Country'})

df_2019['Type']=createTypeColumnList(df_2019['Score'].to_numpy())

new_df_2019 = createCondensedDf(df_2019)


# Plotting 2019 happiness data 

# Plot 1
axs = df_2019.plot.area(x="Score", figsize=(12, 4), subplots=True) 

# Plot 2
axs = df_2019.plot.area(x="Type",figsize=(4, 4), subplots=True )

plt.show()
