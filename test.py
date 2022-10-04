import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

wdi = pd.read_csv(
    "https://media.githubusercontent.com/media/nickeubank/MIDS_Data/master/World_Development_Indicators/wdi_small_tidy_2015.csv"
)

plot_data = wdi[
    [
        "Mortality rate, infant (per 1,000 live births)",
        "GDP per capita (constant 2010 US$)",
        "Country Name",
    ]
]

plot_data.plot(
    x="GDP per capita (constant 2010 US$)",
    y="Mortality rate, infant (per 1,000 live births)",
    kind="scatter",
)
plt.show()

## Perfect
