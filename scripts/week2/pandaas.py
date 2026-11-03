import pandas as pd
from pathlib import Path


file_path = Path(__file__).resolve().parent
file = pd.read_csv(
	file_path / "20161208_onlinedata.csv",
	sep=";",
	skiprows=21,
	encoding="iso-8859-1",
    skipinitialspace=True,
)
file.columns = file.columns.str.strip()

import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("TkAgg")


file["Dato og tid"] = pd.to_datetime(file["Dato og tid"])


x = file["Dato og tid"]


fig, axes = plt.subplots(
    4, 5,
    figsize=(18,12),
    sharex=True
)

axes = axes.flatten()

for i in range(20):
    col = str(i + 1)
    
    axes[i].plot(x, file[col])
    axes[i].set_title(col)
    axes[i].grid(True)
    
plt.tight_layout()
plt.show()
