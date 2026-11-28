#  Project: Railway Gauge Trends

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

project_folder = os.path.dirname(os.path.abspath(__file__))

graph_folder = os.path.join(project_folder, "graphs")

os.makedirs(graph_folder, exist_ok=True)

# Scenario 1: Load and Understand the Dataset

df = pd.read_csv("railway_gauges 1.csv")

print("First 5 Rows:")
print(df.head())

print("\nColumn Names:")
print(df.columns)

print("\nMissing Values:")
print(df.isnull().sum())

df = df.fillna(0)

gauge_columns = ['Broad Gauge', 'Metre Gauge', 'Narrow Gauge', 'Total']

for col in gauge_columns:
    df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0)

df['Year'] = pd.to_numeric(
    df['Year'].astype(str).str[:4],
    errors='coerce'
)

df = df.dropna(subset=['Year'])
df['Year'] = df['Year'].astype(int)

df = df.sort_values('Year')
df = df.reset_index(drop=True)

print("\nData Types:")
print(df.dtypes)


# Scenario 2: Total Railway Track Growth

years = df['Year']
total = df['Total']

plt.figure(figsize=(10, 5))
plt.plot(years, total, marker='o')
plt.title("Total Railway Track Growth")
plt.xlabel("Year")
plt.ylabel("Total Track Length")
plt.grid(True)
plt.tight_layout()
plt.savefig(os.path.join(graph_folder, "total_track_growth.png"))
plt.show()

growth = np.diff(total)

if np.all(growth >= 0):
    print("\nTrend: Increasing")
elif np.all(growth <= 0):
    print("\nTrend: Decreasing")
else:
    print("\nTrend: Fluctuating")


# Scenario 3: Recent Gauge Comparison

recent_data = df[df['Year'] > 2000]

recent_totals = recent_data[gauge_columns[:3]].sum()

print("\nRecent Gauge Totals:")
print(recent_totals)

print("\nDominant Gauge in Recent Years:")
print(recent_totals.idxmax())

recent_data.plot(
    x='Year',
    y=['Broad Gauge', 'Metre Gauge', 'Narrow Gauge'],
    kind='bar',
    figsize=(12, 6)
)

plt.title("Recent Gauge Comparison")
plt.xlabel("Year")
plt.ylabel("Track Length")
plt.tight_layout()
plt.savefig(os.path.join(graph_folder, "recent_gauge_comparison.png"))
plt.show()


# Scenario 4: Gauge Contribution Analysis

gauge_totals = df[gauge_columns[:3]].sum()

print("\nTotal Gauge Contribution:")
print(gauge_totals)

print("\nHighest Contributing Gauge:")
print(gauge_totals.idxmax())

plt.figure(figsize=(7, 7))
plt.pie(
    gauge_totals,
    labels=gauge_totals.index,
    autopct='%1.1f%%',
    startangle=90
)

plt.title("Gauge Contribution")
plt.tight_layout()
plt.savefig(os.path.join(graph_folder, "gauge_contribution_pie.png"))
plt.show()


# Scenario 5: Gauge Trend Analysis

df['Broad Gauge %'] = np.where(
    df['Total'] != 0,
    df['Broad Gauge'] / df['Total'] * 100,
    0
)

df['Metre Gauge %'] = np.where(
    df['Total'] != 0,
    df['Metre Gauge'] / df['Total'] * 100,
    0
)

df['Narrow Gauge %'] = np.where(
    df['Total'] != 0,
    df['Narrow Gauge'] / df['Total'] * 100,
    0
)

growth = np.diff(df['Total'].to_numpy(dtype=float))
df['Growth'] = np.insert(growth, 0, np.nan)

print("\nHighest Growth Year:")
if df['Growth'].notna().any():
    highest_growth_index = df['Growth'].idxmax()
    print(df.loc[highest_growth_index, 'Year'])
else:
    print("Not enough data to calculate growth.")

plt.figure(figsize=(10, 5))
plt.plot(df['Year'], df['Broad Gauge'], label='Broad Gauge')
plt.plot(df['Year'], df['Metre Gauge'], label='Metre Gauge')
plt.plot(df['Year'], df['Narrow Gauge'], label='Narrow Gauge')

plt.title("Gauge Trend Analysis")
plt.xlabel("Year")
plt.ylabel("Track Length")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig(os.path.join(graph_folder, "gauge_trend_analysis.png"))
plt.show()


# Stacked Bar Chart

plt.figure(figsize=(12, 6))

plt.bar(df['Year'], df['Broad Gauge'], label='Broad Gauge')
plt.bar(
    df['Year'],
    df['Metre Gauge'],
    bottom=df['Broad Gauge'],
    label='Metre Gauge'
)

plt.bar(
    df['Year'],
    df['Narrow Gauge'],
    bottom=df['Broad Gauge'] + df['Metre Gauge'],
    label='Narrow Gauge'
)

plt.title("Gauge Composition Over the Years")
plt.xlabel("Year")
plt.ylabel("Track Length")
plt.legend()
plt.tight_layout()
plt.savefig(os.path.join(graph_folder, "gauge_composition_stacked.png"))
plt.show()


# Declining Gauge Analysis

for col in gauge_columns[:3]:
    decline = df[col].diff()

    declining_years = df.loc[decline < 0, 'Year']

    print(f"\nDeclining Years for {col}:")
    print(declining_years.tolist())


# Final Conclusion

gauge_percentages = df[
    ['Broad Gauge %', 'Metre Gauge %', 'Narrow Gauge %']
].mean()

print("\nAverage Gauge Percentage:")
print(gauge_percentages)

print("\nFinal Conclusion:")

if gauge_percentages.idxmax() == 'Broad Gauge %':
    print("Broad Gauge has the highest average contribution.")
elif gauge_percentages.idxmax() == 'Metre Gauge %':
    print("Metre Gauge has the highest average contribution.")
else:
    print("Narrow Gauge has the highest average contribution.")

print("\nAnalysis Completed Successfully!")
print("All graphs are saved in the graphs folder.")
