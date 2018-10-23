

import numpy as np
import pandas as pd
import random as rd

all_data=np.loadtxt("combined_data.data", delimiter=",")
2d_data=all_data[:,[0, 1, 3]]

np.savetxt("sonam_2d.data", 2d_data, fmt='%0.10f', delimiter=",")
