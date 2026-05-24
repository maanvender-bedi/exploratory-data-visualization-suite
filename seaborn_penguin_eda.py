import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df = sns.load_dataset('penguins')

sns.set_theme(style="whitegrid")
sns.set_context("talk", font_scale=1.2)
sns.set_style({
    "axes.facecolor": "#f5f5f5",
    "axes.edgecolor": "black",
    "axes.grid": True,
    "grid.color": ".8",
    "grid.linestyle": "--",
    "grid.linewidth": 0.8
})

# Scatter Plot
plt.figure(figsize=(8,6))
sns.scatterplot(
    data=df,
    x="bill_length_mm",
    y="bill_depth_mm",
    hue="species",
    style="sex",
    size="flipper_length_mm",
    sizes=(50, 200),
    alpha=0.7
)
plt.title("Scatter Plot with Hue, Style, and Size")
plt.show()

# Strip Plot
plt.figure(figsize=(8,6))
sns.stripplot(
    data=df,
    x="species",
    y="bill_length_mm",
    jitter=True,
    hue="sex",
    dodge=True
)
plt.title("Scatter (Strip) Plot with Jitter")
plt.show()

# Histogram
plt.figure(figsize=(8,6))
sns.histplot(data=df, x="flipper_length_mm", kde=True, bins=20, color='skyblue', edgecolor='black')
plt.title("Histogram of Flipper Length")
plt.show()