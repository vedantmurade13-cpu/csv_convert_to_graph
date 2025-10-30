import pandas as pd
import matplotlib.pyplot as plt

# Load CSV file
file_path = "sample.csv"  # change filename to your file
data = pd.read_csv(file_path)

# Display data (optional)
print(data.head())

# Plot graph
plt.figure()
plt.plot(data.iloc[:, 0], data.iloc[:, 1], marker='o')  # first col X, second col Y
plt.title("CSV Data Graph")
plt.xlabel(data.columns[0])
plt.ylabel(data.columns[1])
plt.grid(True)

# Show graph
plt.show()
