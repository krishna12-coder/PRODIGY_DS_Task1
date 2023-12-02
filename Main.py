import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv(r'C:\Users\Hp\Downloads\API_SP.POP.TOTL_DS2_en_csv_v2_6011311\Metadata_Country.csv')


region_counts = df['Region'].value_counts()
plt.figure(figsize=(10, 6))
# Extracting the counts for each region and generating a range of values for the x-axis
counts = [region_counts[region] for region in region_counts.index]
x = range(len(region_counts))
# Define the base color (#C0B769)
base_color = '#FF5733'
# Generating shades of the base color for each region in reverse order
num_regions = len(region_counts)
colors = [plt.cm.Greens(1 - i / float(num_regions)) for i in range(num_regions)]
# Plotting a bar for each region with a different shade of the base color in reverse order
for i, count in enumerate(counts):
    plt.bar(i, count, color=colors[i], alpha=0.7, edgecolor='black', label=region_counts.index[i])
plt.xlabel('Region')
plt.ylabel('Count')
plt.title('Histogram-Like Distribution of Region Counts')
plt.xticks(x, region_counts.index, rotation=45)
plt.legend()
plt.tight_layout()
plt.show()
