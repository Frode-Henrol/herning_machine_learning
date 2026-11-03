
import matplotlib.pyplot as plt
import matplotlib
import pandas as pd
from pathlib import Path

matplotlib.use("TkAgg")



if __name__ == "__main__":
    
    filepath = Path(__file__).resolve().parent
    print(filepath)
    filename = "aquifer_day.txt"
    
    filepath = filepath / filename
    
    data = pd.read_csv(filepath, sep="\s+",skiprows=[0,2])
    
    gis_id = data["gis_id"]
    flo = data["flo"]
    
    flo_corr = [f for f, g in zip(flo, gis_id) if g == 11]
    
    x = list(range(len(flo_corr)))
    
    plt.plot(x, flo_corr)
    plt.show()
    
    
    print(flo_corr)
    
    print("done")
