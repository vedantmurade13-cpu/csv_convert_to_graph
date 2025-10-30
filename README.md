📊 CSV-to-Graph Data Visualization Tool

A Python-based system to convert CSV files into meaningful visual graphs

📝 Project Description

This project converts CSV-formatted data into visual graphs using Python libraries like Pandas and Matplotlib.
It is designed to help users visualize large datasets, identify trends, and analyze real-world information like:

📈 Meter readings (electricity, water, gas)

🌡 IoT sensor logs (temperature, humidity, etc.)

💰 Financial or sales data

🚗 Vehicle telematics data

📊 Academic & research datasets

This application is simple, lightweight, and ideal for students, researchers, engineers, and data analysts who want quick insights from CSV data.

🎯 Project Objectives

Automate CSV file reading using Python

Convert raw numeric data into clean graphs

Support time-series data visualization

Help in identifying data trends & anomalies

Reduce manual analysis efforts

🏗 Technologies Used
Technology	Purpose
Python	Core programming language
Pandas	Read & process CSV data
Matplotlib	Plot and visualize graphs
CSV File Format	Standard data input format
📂 Folder Structure
csv-to-graph-python/
│── plot_csv.py         # Main python script
│── sample.csv          # Example CSV input
│── README.md           # Project documentation
└── output/             # (Optional) save charts here

⚙️ Installation & Setup
✅ 1. Install Python

Download from: https://www.python.org/downloads/

✅ 2. Install Required Libraries
pip install pandas matplotlib

✅ 3. Run the Program
python plot_csv.py

🧾 Sample CSV File Format
Date	Usage
2025-01-01	120
2025-01-02	150
2025-01-03	135

Save the file as sample.csv (or your preferred file name)

📜 Python Code Used
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("sample.csv")

plt.figure()
plt.plot(data.iloc[:, 0], data.iloc[:, 1], marker='o')
plt.title("CSV Data Graph")
plt.xlabel(data.columns[0])
plt.ylabel(data.columns[1])
plt.grid(True)
plt.show()

🎨 Graph Output

The graph displays:

X-axis → First column of CSV (ex: Date)

Y-axis → Second column of CSV (ex: Usage)

Points with markers

Grid lines for better visualization

⚡ Features

✅ Reads any CSV file
✅ Auto-labels axis using column names
✅ Plots smooth line graphs
✅ User-friendly & beginner-friendly
✅ Works for small and large datasets

🎯 Real-World Applications
Domain	Use-case
Energy Sector	Electricity meter reading visualization
IoT Systems	Sensor data monitoring
Finance	Income vs expenditure graphs
Research Projects	Dataset trend analysis
Education	Data interpretation learning
🧠 Future Improvements
Planned Feature	Description
GUI File Uploader	Upload CSV via interface
Multiple Graph Types	Bar chart, scatter plot, histogram
Export Options	Save graph as PNG/PDF
Live Sensor Data	Real-time plotting
Web App Version	Streamlit/Django interface
🤝 Contributing

Contributions, issues, and feature requests are welcome!
Fork the repo & submit a pull request ✅

📬 Contact

Author: Vedant Murade
🎓 IT Student | India
💡 Interested in Data Science & Automation

⭐ Support

If you found this useful, please ⭐ star the repository to support the project
