import matplotlib.pyplot as plt

# Basic line plot
x = [1, 2, 3, 4, 5]
y = [10, 15, 13, 18, 16]

plt.plot(x, y)
plt.title("Basic Line Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.show()

# Multiple line plots
x = [1, 2, 3, 4, 5]
y1 = [1, 4, 9, 16, 25]
y2 = [25, 16, 9, 4, 1]

plt.plot(x, y1, label='y1')
plt.plot(x, y2, label='y2')
plt.title("Multiple Line Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend()
plt.grid(True)
plt.show()

# Bar chart
categories = ['A', 'B', 'C', 'D']
values = [10, 24, 36, 18]

plt.bar(categories, values, color='skyblue')  # ✅ corrected color name
plt.title("Basic Bar Chart")
plt.xlabel("Categories")
plt.ylabel("Values")
plt.grid(axis='y')
plt.show()
