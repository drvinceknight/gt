import statistics as stat

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../data.csv")
slope, intercept = stat.linear_regression(df["Guess 1"], df["Guess 2"])

start_point, end_point = min(df["Guess 1"]), max(df["Guess 1"])
image_start_point = slope * start_point + intercept
image_end_point = slope * end_point + intercept

plt.figure()
plt.scatter(df["Guess 1"], df["Guess 2"])
plt.plot((start_point, end_point), (image_start_point, image_end_point), color="black")
plt.xlabel("Guess 1")
plt.ylabel("Guess 2")
plt.title(f"Fitted line: $y={slope:.2f}x + {intercept:.2f}$");
plt.savefig("main.pdf")
