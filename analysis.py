# ============================================================
# Research on Exchange Rate and Inflation in Pakistan
# ============================================================

"""
This project examines the relationship between the USD/PKR
exchange rate and consumer price inflation in Pakistan.

Study Period:
January 2020 – June 2025

Observations:
66 monthly observations

Data Sources:
- State Bank of Pakistan (SBP): USD/PKR exchange rate
- Pakistan Bureau of Statistics (PBS): CPI-based inflation

Methodology:
- Descriptive statistics
- Monthly trend analysis
- Pearson correlation
- Statistical significance test
- Scatter plot with linear trend

The analysis is descriptive and does not establish causality.
"""

# ============================================================
# 1. Import Libraries
# ============================================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import pearsonr

# Load the dataset

df = pd.read_excel(
    r"C:\Users\tooba\OneDrive\Desktop\Project 2\Exchange Rate vs. Inflation Analysis (2020-2025).xlsx.xlsx"
)
print(df.head())
print(df.info())
print(df.tail())
# Check the date column

print(df["Date"].head(10))
print(df["Date"].tail(10))
# Create a correct date variable from Year and Month

df["Date_Corrected"] = pd.to_datetime(
    df["Year"].astype(str) + "-" + df["Month"] + "-01"
)

print(df[["Year", "Month", "Date_Corrected"]].head())
# Descriptive statistics

print(df[["Exchange Rate", "Inflation Rate (%)"]].describe())

# Load the dataset
import os

print(os.listdir())
# ==========================================
# Pearson Correlation Analysis
# ==========================================

correlation = df["Exchange Rate"].corr(df["Inflation Rate (%)"])

print("\nPearson Correlation:")
print(f"Correlation coefficient (r): {correlation:.3f}")

# ==========================================
# Pearson Correlation Significance Test
# ==========================================

from scipy.stats import pearsonr

r, p_value = pearsonr(
    df["Exchange Rate"],
    df["Inflation Rate (%)"]
)

print("\nPearson Correlation Test:")
print(f"r = {r:.3f}")
print(f"p-value = {p_value:.6f}")
# ==========================================
# Scatter Plot: Exchange Rate vs Inflation
# ==========================================


plt.figure(figsize=(8, 6))

plt.scatter(
    df["Exchange Rate"],
    df["Inflation Rate (%)"]
)

plt.xlabel("Exchange Rate (PKR per USD)")
plt.ylabel("Inflation Rate (%)")
plt.title("Exchange Rate and Inflation in Pakistan (2020–2025)")

plt.grid(True, alpha=0.3)

plt.show()
# ==========================================
# Scatter Plot with Linear Trend Line
# ==========================================

import matplotlib.pyplot as plt
import numpy as np

x = df["Exchange Rate"]
y = df["Inflation Rate (%)"]

# Calculate linear trend line
slope, intercept = np.polyfit(x, y, 1)
trend_line = slope * x + intercept

plt.figure(figsize=(8, 6))

plt.scatter(
    x,
    y,
    label="Monthly observations"
)

plt.plot(
    x,
    trend_line,
    linewidth=2,
    label="Linear trend"
)

plt.xlabel("Exchange Rate (PKR per USD)")
plt.ylabel("Inflation Rate (%)")
plt.title("Exchange Rate and Inflation in Pakistan (2020–2025)")

plt.legend()
plt.grid(True, alpha=0.3)

plt.show()
# ==========================================
# Linear Trend Statistics
# ==========================================

r_squared = correlation ** 2

print("\nLinear Trend Statistics:")
print(f"Slope: {slope:.6f}")
print(f"Intercept: {intercept:.6f}")
print(f"R-squared: {r_squared:.4f}")

print("\nRegression Equation:")
print(f"Inflation Rate = {intercept:.4f} + ({slope:.4f} × Exchange Rate)")
# ==========================================
# Exchange Rate Trend Over Time
# ==========================================

plt.figure(figsize=(10, 6))

plt.plot(
    df["Date_Corrected"],
    df["Exchange Rate"],
    linewidth=2
)

plt.xlabel("Date")
plt.ylabel("Exchange Rate (PKR per USD)")
plt.title("USD/PKR Exchange Rate in Pakistan (2020–2025)")

plt.grid(True, alpha=0.3)
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()
# ==========================================
# Inflation Trend Over Time
# ==========================================

plt.figure(figsize=(10, 6))

plt.plot(
    df["Date_Corrected"],
    df["Inflation Rate (%)"],
    linewidth=2
)

plt.xlabel("Date")
plt.ylabel("Inflation Rate (%)")
plt.title("Inflation Rate in Pakistan (2020–2025)")

plt.grid(True, alpha=0.3)
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()
# ==========================================
# Combined Exchange Rate and Inflation Trends
# ==========================================

fig, ax1 = plt.subplots(figsize=(10, 6))

# Exchange rate
ax1.plot(
    df["Date_Corrected"],
    df["Exchange Rate"],
    linewidth=2,
    label="Exchange Rate"
)

ax1.set_xlabel("Date")
ax1.set_ylabel("Exchange Rate (PKR per USD)")

# Inflation on second axis
ax2 = ax1.twinx()

ax2.plot(
    df["Date_Corrected"],
    df["Inflation Rate (%)"],
    linewidth=2,
    label="Inflation Rate"
)

ax2.set_ylabel("Inflation Rate (%)")

plt.title("Exchange Rate and Inflation Trends in Pakistan (2020–2025)")

ax1.grid(True, alpha=0.3)
plt.xticks(rotation=45)

fig.tight_layout()
plt.show()
# ==========================================
# Verification of SSRN Paper Statistics
# ==========================================

print("\n--- SSRN Paper Verification ---")

print("Number of observations:", len(df))

print("\nExchange Rate:")
print(f"Mean: {df['Exchange Rate'].mean():.2f}")
print(f"Minimum: {df['Exchange Rate'].min():.2f}")
print(f"Maximum: {df['Exchange Rate'].max():.2f}")

print("\nInflation Rate:")
print(f"Mean: {df['Inflation Rate (%)'].mean():.2f}")
print(f"Minimum: {df['Inflation Rate (%)'].min():.2f}")
print(f"Maximum: {df['Inflation Rate (%)'].max():.2f}")
# ==========================================
# Verify Study Period
# ==========================================

print("\n--- Study Period Verification ---")

print("Start Date:", df["Date_Corrected"].min().strftime("%B %Y"))
print("End Date:", df["Date_Corrected"].max().strftime("%B %Y"))
# ==========================================
# Check for Missing Values
# ==========================================

print("\n--- Missing Values Check ---")

print("Exchange Rate missing values:",
      df["Exchange Rate"].isna().sum())

print("Inflation Rate missing values:",
      df["Inflation Rate (%)"].isna().sum())
# ==========================================
# Check for Duplicate Months
# ==========================================

print("\n--- Duplicate Month Check ---")

duplicates = df["Date_Corrected"].duplicated().sum()

print("Duplicate months:", duplicates)
# ==========================================
# Figure 1: Exchange Rate and Inflation
# ==========================================

fig, ax1 = plt.subplots(figsize=(12, 6))

# Exchange Rate
ax1.plot(
    df["Date_Corrected"],
    df["Exchange Rate"],
    linewidth=2,
    label="USD/PKR Exchange Rate"
)

ax1.set_xlabel("Date")
ax1.set_ylabel("Exchange Rate (PKR per USD)")

# Inflation
ax2 = ax1.twinx()

ax2.plot(
    df["Date_Corrected"],
    df["Inflation Rate (%)"],
    linewidth=2,
    label="Inflation Rate"
)

ax2.set_ylabel("Inflation Rate (%)")

plt.title(
    "Monthly Exchange Rate and Consumer Price Inflation "
    "in Pakistan (January 2020–June 2025)"
)

ax1.grid(True, alpha=0.3)
plt.xticks(rotation=45)

fig.tight_layout()
plt.show()
