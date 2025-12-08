import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


#reading my csv file into a data

dframe = pd.read_csv("Sleep_health_and_lifestyle_dataset.csv", index_col=["Person ID"] , usecols=[0,1,2,3,4,5,6,7,8,9,10,11,12])

# get rid of nan values in the dataframe, replace them with values that are similar
print(dframe["Sleep Duration"].isna().sum()) #based on this result it would be hard to correlate sleep disorder to something else as so much of the data would need to be modified

"""
First Visualization: distribution of sleep duration.
"""
print(type(dframe["Sleep Duration"]))

#y_axe = dframe.loc[:,"Sleep Duration"]
#x_axe = dframe.loc["Person ID":,:]
plt.figure(figsize=(10,4))
plt.bar(dframe["Sleep Duration"], bins =50,
        color="violet", edgecolor="blue")
plt.xlabel("Sleep Duration (Hours)")
plt.ylabel("Frequency")
plt.title("Typical Sleep Hour Histogram Graph")
plt.tight_layout()
plt.show()

#average person is getting 6 hours and above
#find out how/who/occupation many of people sleeping less than or equal to six hours are

sleep_less = dframe[dframe["Sleep Duration"] <= 6.5]
sleep_dic = {}
all_dic = {}
for pation in dframe["Occupation"]:
    all_dic[pation] = all_dic.get(pation, 0) + 1 #
    if pation in sleep_less["Occupation"].values:
        sleep_dic[pation] = sleep_dic.get(pation, 0) + 1 #c
        

print(sleep_dic)
print(all_dic)
"""
Doctors and Nurse were the occupations that had the highest number of people sleeping 6 hours or less.

"""