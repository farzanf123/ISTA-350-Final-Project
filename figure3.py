import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os


#reading my csv file into a data

dframe = pd.read_csv("Sleep_health_and_lifestyle_dataset.csv", index_col=["Person ID"] , usecols=[0,1,2,3,4,5,6,7,8,9,10,11,12])

# get rid of nan values in the dataframe, replace them with values that are similar
print(dframe["Sleep Disorder"].isna().sum()) #based on this result it would be hard to correlate sleep disorder to something else as so much of the data would need to be modified


#each gender is side by side

pivot_df = dframe.pivot_table(index = 'Occupation', columns='Gender', values='Stress Level', aggfunc='mean').fillna(0)


#plt.figure(figsize=(12,6))
#plt.bar(x - width/2, pivot_df['Male'], width, label='Male')
#plt.bar(x + width/2, pivot_df['Female'], width, label='Female')

pivot_df.plot(kind='bar', figsize=(12,6), color= ['skyblue', 'pink']) 
plt.xlabel('Occupation')
plt.ylabel('Average Stress Level')
plt.title('Male Vs. Female Stress Level by Occupation')
plt.xticks(rotation = 45, ha='right')
plt.legend(title = 'Genders')
plt.tight_layout()
plt.show()
