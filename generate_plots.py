import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import os

# Raw data
years = list(range(2000, 2021))
crime_types = ["Assault", "Burglary", "Robbery", "Vehicle Theft"]
sample_values = [
    [523, 349, 128, 223], [610, 287, 105, 195], [724, 365, 142, 217], [819, 429, 178, 308],
    [897, 516, 221, 393], [1054, 643, 283, 472], [1215, 752, 329, 529], [1382, 864, 408, 648],
    [1567, 1012, 480, 742], [1769, 1194, 597, 869], [1946, 1421, 718, 1024], [2113, 1652, 839, 1263],
    [2339, 1981, 1024, 1498], [2562, 2357, 1316, 1865], [2798, 2732, 1582, 2187],
    [3025, 3191, 1903, 2578], [3251, 3669, 2225, 2957], [3484, 4223, 2601, 3304],
    [3719, 4801, 3104, 3776], [3962, 5498, 3583, 4359], [4205, 6203, 1573, 5462]
]

# Build DataFrame
data = {"Year": [], "Type of Crime": [], "Number of Crimes": []}
for year, row in zip(years, sample_values):
    for crime, value in zip(crime_types, row):
        data["Year"].append(year)
        data["Type of Crime"].append(crime)
        data["Number of Crimes"].append(value)

df = pd.DataFrame(data)

# Create output folder
os.makedirs("plots", exist_ok=True)

# Generate one chart per crime type
for crime in crime_types:
    fig = px.line(
        df[df["Type of Crime"] == crime],
        x="Year",
        y="Number of Crimes",
        title=f"{crime} Over Time",
        markers=True
    )
    fig.write_html(f"plots/{crime.lower().replace(' ', '_')}.html")

# Combined plot
fig_all = px.line(
    df,
    x="Year",
    y="Number of Crimes",
    color="Type of Crime",
    title="All Crime Types Over Time",
    markers=True
)
fig_all.write_html("plots/all.html")

print("✅ Plots generated successfully.")
