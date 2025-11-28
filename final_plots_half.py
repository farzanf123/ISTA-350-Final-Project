#Second visualization
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import requests
import os
from bs4 import BeautifulSoup

#WEB SCRAPING
url = 'https://www.kaggle.com/datasets/abdelazizsami/lifestyle-dataset'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html')
description = soup.find('p', class_= 'dataset_description')
if description:
    dataset_description = description.get_text()
    print(dataset_description)
else:
    None

df = pd.read_csv("Sleep_health_and_lifestyle_dataset.csv")

#distribution of occupations data visualization

# calculating the count of each occupation
occupation_count = df['Occupation'].value_counts()

#extracts the occupation names and counts 
occupations = occupation_count.index.tolist()
counts = occupation_count.values.tolist()

# Bar chart
num_bars = len(occupations)

plt.figure(figsize=(12, 7))
bars = plt.bar(occupations, counts, color ='blue', edgecolor ='black')
plt.title('Distribution of Occupations', fontsize=16)
plt.xlabel('Occupation', fontsize=12)
plt.ylabel('Number of People', fontsize=12)
plt.xticks(rotation=45, fontsize=10)
plt.yticks(fontsize=10)
plt.tight_layout()
plt.show()

'''
linear regression graph
'''
import statsmodels.api as sm
# mean sleep duration by occupation linear regression line visualization
sleep_data= df['Sleep Duration']
stress_level_data = df['Stress Level']
X = sm.add_constant(stress_level_data)
model = sm.OLS(sleep_data, X)
results = model.fit()
results.params
plt.figure(figsize=(12, 7))
x_range = stress_level_data.min(), stress_level_data.max()
x_range_constant = sm.add_constant(x_range)
y_predict = results.predict(x_range_constant)
plt.plot(x_range, y_predict, color='red', linewidth=2, label='Linear Regression Line')
plt.scatter(stress_level_data, sleep_data, color='blue', edgecolor='black', linewidth=0.7, label='Individual Points')
plt.title('Relationship Between Stress Level and Sleep Duration', fontsize=18, weight='bold')
plt.xlabel('Stress Level 1-10', fontsize=14)
plt.ylabel('Sleep Duration (Hours)', fontsize=14)
plt.xticks(np.arange(stress_level_data.min(), stress_level_data.max()), fontsize = 10)
plt.yticks(fontsize=10)
plt.legend()
plt.tight_layout()
plt.show()

'''
Graph representing sleep quality by occupation 
'''
sleep_quality_by_occupation = (df.groupby('Occupation')['Quality of Sleep'].mean().sort_values(ascending=False).reset_index())
occupations = sleep_quality_by_occupation['Occupation'].tolist()
avg_sleep_quality = sleep_quality_by_occupation['Quality of Sleep'].values
num_occupations = len(occupations)
plt.figure(figsize=(12,7))
plt.bar(occupations, avg_sleep_quality, color='purple', edgecolor= 'black')
plt.title('Average Quality of Sleep VS Occupations', fontsize=18, weight='bold')
plt.xlabel('Occupation', fontsize=14)
plt.ylabel('Average Quality of Sleep (1-10)', fontsize=14)
plt.ylim(min(avg_sleep_quality) - 0.5, max(avg_sleep_quality) + 0.5)
plt.xticks(rotation=45, fontsize=10)
plt.yticks(fontsize=10)
plt.tight_layout()
plt.show()