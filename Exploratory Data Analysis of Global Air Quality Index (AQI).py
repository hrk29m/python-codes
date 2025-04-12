import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load dataset
# Replace 'air_quality.csv' with the path to your actual dataset
df = pd.read_csv(r'C:\Users\Hridhya\Downloads\air_quality.csv')


# Show first few rows
print("First 5 rows:")
print(df.head())

# Basic info
print("\nDataset Info:")
print(df.info())

# Statistical Summary
print("\nStatistical Summary:")
print(df.describe())

# Drop missing values
df = df.dropna()

# Group by City and calculate mean PM2.5
city_pm25 = df.groupby('City')['PM2.5'].mean().sort_values(ascending=False).head(10)

# Bar plot: Top 10 cities with highest average PM2.5
plt.figure(figsize=(10, 6))
city_pm25.plot(kind='bar', color='crimson')
plt.title('Top 10 Cities with Highest PM2.5 Levels')
plt.xlabel('City')
plt.ylabel('Average PM2.5')
plt.grid(True)
plt.tight_layout()
plt.show()

# Line plot: PM2.5 over time for a sample city
sample_city = 'Delhi'  # change based on your dataset
df_city = df[df['City'] == sample_city]

plt.figure(figsize=(10, 5))
plt.plot(pd.to_datetime(df_city['Date']), df_city['PM2.5'], marker='o', linestyle='-', color='blue')
plt.title(f'PM2.5 Levels Over Time in {sample_city}')
plt.xlabel('Date')
plt.ylabel('PM2.5')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()

# Correlation heatmap of pollutants
pollutants = ['PM2.5', 'PM10', 'NO2', 'CO']
correlation = df[pollutants].corr()

plt.figure(figsize=(6, 5))
plt.imshow(correlation, cmap='coolwarm', interpolation='none')
plt.colorbar(label='Correlation Coefficient')
plt.xticks(range(len(pollutants)), pollutants)
plt.yticks(range(len(pollutants)), pollutants)
plt.title('Correlation Between Pollutants')
plt.tight_layout()
plt.show()
