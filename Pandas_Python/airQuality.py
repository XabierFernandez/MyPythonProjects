import pandas as pd
from matplotlib import pyplot as plt

air_quality = pd.read_csv('air_quality_no2.csv',index_col=0, parse_dates=True)
# air_quality.plot()

air_quality["station_london"].plot()

air_quality.plot.scatter(x="station_london",
                            y="station_paris",
                            alpha=0.5)
air_quality.plot.density(x="station_london",
                            y="station_paris",
                            alpha=0.5)
axs = air_quality.plot.area(figsize=(12, 4), subplots=True)

fig, axs = plt.subplots(figsize=(12, 4));
air_quality.plot.area(ax=axs);
axs.set_ylabel("NO$_2$ concentration");
fig.savefig("no2_concentrations.png")

[method_name for method_name in dir(air_quality.plot)
 if not method_name.startswith("_")]