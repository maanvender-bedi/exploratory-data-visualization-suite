import matplotlib.pyplot as plt

x = ["Hero", "Honda", "TVS"]
y = [5395924, 4092126, 2965744]

colors = ['black', 'red', 'blue']
plt.bar(x, y, color=colors)
plt.xlabel("brands")
plt.ylabel("sold")
plt.title("Sales Report in the 2024")
plt.show()