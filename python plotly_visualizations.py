import pandas as pd
import plotly.express as px

data = {
    'Electronics': ['Laptop', 'Mobile', 'Tablet', 'Camera', 'Headphones'],
    'Stock': [150, 200, 100, 80, 120],
    'Category': ['Green', 'Blue', 'Orange', 'Red', 'Brown']
}

df = pd.DataFrame(data)

# Bar Chart
fig = px.bar(df, x='Electronics', y='Stock', color='Category', title="Stock by Electronics")
fig.write_image("bar_chart.png")

# Pie Chart
fig = px.pie(df, names='Electronics', values='Stock', title="Stock Distribution")
fig.write_image("pie_chart.png")

# Line Chart
df_sorted = df.sort_values(by='Electronics')
fig = px.line(df_sorted, x='Electronics', y='Stock', color='Category', markers=True, title="Stock of Electronics by Category")
fig.write_image("line_chart.png")

# Scatter Plot
fig = px.scatter(df, x='Electronics', y='Stock', color='Category', size='Stock', title="Stock Scatter Plot")
fig.write_image("scatter_plot.png")

# Area Plot
fig = px.area(df, x='Electronics', y='Stock', color='Category', title="Stock Area Plot")
fig.write_image("area_plot.png")

# Box Plot
fig = px.box(df, x='Category', y='Stock', title="Stock Distribution by Category")
fig.write_image("box_plot.png")

# Histogram
fig = px.histogram(df, x='Stock', nbins=5, title="Stock Histogram")
fig.write_image("histogram.png")

# Heatmap
heatmap_data = df.pivot_table(values='Stock', index='Electronics', columns='Category', fill_value=0)
fig = px.imshow(heatmap_data, title="Stock Heatmap")
fig.write_image("heatmap.png")

# Gantt Chart
data_gantt = {
    'Electronics': ['Laptop', 'Mobile', 'Tablet', 'Camera', 'Headphones'],
    'Stock': [150, 200, 100, 80, 120],
    'Category': ['Green', 'Blue', 'Orange', 'Red', 'Black'],
    'Start': ['2025-09-01', '2025-09-03', '2025-09-05', '2025-09-02', '2025-09-04'],
    'Finish': ['2025-09-05', '2025-09-07', '2025-09-08', '2025-09-06', '2025-09-09']
}
df_gantt = pd.DataFrame(data_gantt)
fig = px.timeline(df_gantt, x_start="Start", x_end="Finish", y="Electronics", color="Category", title="Stock Availability Timeline")
fig.update_yaxes(autorange="reversed")
fig.write_image("gantt_chart.png")

print("All charts saved successfully!")