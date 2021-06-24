
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from stickleback.stickleback import Stickleback
plt.rcParams['figure.figsize'] = [12, 8]

# print(pd.Series(pd.DatetimeIndex(pd.read_pickle("data/bw180828-49_breaths.pkl"))))

# Read example data
breath_sb = Stickleback(
    sensors=pd.read_pickle("data/bw180828-49_prh10.pkl"), 
    events=pd.DatetimeIndex(pd.read_pickle("data/bw180828-49_breaths.pkl")),
    win_size=50 #, min_period=10
)

ex_data_plot = breath_sb.plot_sensors_events(interactive=False)