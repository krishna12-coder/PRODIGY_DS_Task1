# PRODIGY_DS_Task1
Bar Graph




1.Library Import:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


pandas: Used for handling and manipulating data.
matplotlib.pyplot: Provides a MATLAB-like plotting framework.
numpy: Provides support for numerical operations.


2. Reading Data:
   
df = pd.read_csv(r'C:\Users\Hp\Downloads\API_SP.POP.TOTL_DS2_en_csv_v2_6011311\Metadata_Country.csv')

Reads a CSV file named Metadata_Country.csv into a pandas DataFrame df.

3. Counting Region Occurrences:
   
region_counts = df['Region'].value_counts()

Calculates the count of occurrences for each unique region present in the 'Region' column of the DataFrame df.
The resulting counts are stored in the region_counts variable.

4. Plotting Preparation:
   
plt.figure(figsize=(10, 6))
counts = [region_counts[region] for region in region_counts.index]
x = range(len(region_counts))
base_color = '#FF5733'
num_regions = len(region_counts)
colors = [plt.cm.Greens(1 - i / float(num_regions)) for i in range(num_regions)]

Sets up the figure size for the upcoming plot.
Extracts the counts of occurrences for each region and generates a range of x-values for the x-axis.
Defines a base color and calculates the number of regions and corresponding shades of green based on the number of regions.

6. Plotting the Bar Chart:
   for i, count in enumerate(counts):
    plt.bar(i, count, color=colors[i], alpha=0.7, edgecolor='black', label=region_counts.index[i])
plt.xlabel('Region')
plt.ylabel('Count')
plt.title('Histogram-Like Distribution of Region Counts')
plt.xticks(x, region_counts.index, rotation=45)
plt.legend()
plt.tight_layout()
plt.show()

Uses a loop to create a bar plot where each bar represents a region.
Each bar is assigned a specific color shade corresponding to the count of occurrences for that region.
Sets labels for the x-axis and y-axis, title for the plot, rotates x-axis labels for better readability, includes a legend, and displays the plot.
This code performs data reading, data manipulation, and visualization steps to generate a histogram-like bar plot showing the distribution of counts for different regions based on the data provided in the Metadata_Country.csv file.
