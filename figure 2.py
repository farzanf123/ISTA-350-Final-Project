import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os


#reading my csv file into a data

dframe = pd.read_csv("Sleep_health_and_lifestyle_dataset.csv", index_col=["Person ID"] , usecols=[0,1,2,3,4,5,6,7,8,9,10,11,12])

# get rid of nan values in the dataframe, replace them with values that are similar
print(dframe["Sleep Disorder"].isna().sum()) #based on this result it would be hard to correlate sleep disorder to something else as so much of the data would need to be modified



"""

fig, ax1 = plt.subplots(figsize = (14,8))
ax2 = ax1.twinx()

slope = np.polyfit(dframe["Occupation"].astype('category').cat.codes, dframe["Stress Level"], 1)
inter_1 =  slope[1]

slope2 = np.polyfit(dframe["Occupation"].astype('category').cat.codes, dframe["Quality of Sleep"], 1)
inter_2 =  slope2[1]

occ_codes = dframe["Occupation"].astype("category").cat.codes
occ_labels = dframe["Occupation"].astype("category").cat.categories

# Regression lines
line_of_best_fit1 = slope[0] * occ_codes + inter_1
line_of_best_fit2 = slope2[0] * occ_codes + inter_2

# Plot
ax1.scatter(occ_codes, dframe["Stress Level"], color='green')
ax2.scatter(occ_codes, dframe["Quality of Sleep"], color='orange')
ax1.plot(occ_codes, line_of_best_fit1, color='green', label='Stress Level Trend')
ax2.plot(occ_codes, line_of_best_fit2, color='orange', label='Quality of Sleep Trend')


ax1.set_xlabel('Occupation')
ax1.set_ylabel('Stress Level', color='green')
ax1.tick_params(axis = "y", labelcolor ="green")
ax1.legend(loc='upper left')

ax2.set_ylabel('Quality of Sleep', color='orange')
ax2.tick_params(axis = "y", labelcolor ="orange")
ax2.legend(loc='upper right')

# Proper x-axis tick labels
plt.xticks(ticks=range(len(occ_labels)), labels=occ_labels, rotation=65, ha='right')
plt.show()
"""

dframe_mean = dframe.groupby("Sleep Duration")[['Stress Level', 'Quality of Sleep']].mean().reset_index()
fig, ax1 = plt.subplots(figsize = (14,8))
ax2 = ax1.twinx()

slope = np.polyfit(dframe_mean["Sleep Duration"].astype('category').cat.codes, dframe_mean["Stress Level"], 1)
inter_1 =  slope[1]


slope2 = np.polyfit(dframe_mean["Sleep Duration"].astype('category').cat.codes, dframe_mean["Quality of Sleep"], 1)
inter_2 =  slope2[1]

occ_codes = dframe_mean["Sleep Duration"].astype("category").cat.codes
occ_labels = dframe_mean["Sleep Duration"].astype("category").cat.categories
# Regression lines
line_of_best_fit1 = slope[0] * occ_codes + inter_1
line_of_best_fit2 = slope2[0] * occ_codes + inter_2

# Plot
ax1.scatter(occ_codes, dframe_mean["Stress Level"], color='green')
ax2.scatter(occ_codes, dframe_mean["Quality of Sleep"], color='orange')
ax1.plot(occ_codes, line_of_best_fit1, color='green', label='Stress Level Trend')
ax2.plot(occ_codes, line_of_best_fit2, color='orange', label='Quality of Sleep Trend')


ax1.set_xlabel('Sleep Duration (In Hours )')
ax1.set_ylabel('Stress Level', color='green')
ax1.tick_params(axis = "y", labelcolor ="green")
ax1.legend(loc='upper left')

ax2.set_ylabel('Quality of Sleep', color='orange')
ax2.tick_params(axis = "y", labelcolor ="orange")
ax2.legend(loc='upper right')

# Proper x-axis tick labels
plt.xticks(ticks=range(len(occ_labels)), labels=occ_labels, rotation=65, ha='right')
plt.title('Stress Level And Quality of Sleep Vs. Sleep Duration')
plt.tight_layout()
plt.show()
