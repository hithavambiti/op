import json
import sys
import os

import numpy as np
from tqdm import tqdm

sys.path.append(os.path.join(os.path.dirname(__file__), "src"))

from maths.earth_frame_conversions import *
from astropy.time import Time
times = ['1999-01-01T00:00:00.123456789', '2010-01-01T00:00:00']
t = Time(times, format='isot', scale='utc')

print(ecef_to_eci(eci_to_ecef([7000,0,0],t[1]),t[1]))
