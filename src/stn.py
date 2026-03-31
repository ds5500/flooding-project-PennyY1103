"""
This script is used to collect and preprocess flood event observations from high-water marks
documented in the USGS Short-Term Network System (https://stn.wim.usgs.gov/STNServices/Documentation/HWM/AllHWMs).

This script includes the following steps:
    * step 1 - download high-water marks from Short-Term Network System;
    * step 2 - preprocess the collected high-water marks.
"""

# import libraries
import time
from utils import stn_utils, global_utils

# start and track the runtime
start = time.time()
print('\nSTART - STN FLOOD EVENT DATA COLLECTION AND PREPROCESSING')

# set variables
area_list = list(global_utils.area_abbr_list.values()) # two-letter state abbreviation list (New England Region)
attr_list = global_utils.attr_list # attributes selected for this project 
check_list = ['event', 'latitude', 'longitude'] # list used to drop the observations sharing the same location and event name
date_threshold = 2017 # date used to select the flood event observations (Harmonized Sentinel-2 MSI Level-2A availability)

stn_raw_file = 'df_stn_raw' # original dataset
stn_mod_file = 'df_stn_mod' # modified dataset

# step 1 - collect high-water marks from STN database
stn_raw = stn_utils.collect_stn(area_list, stn_raw_file)

# step 2 - preprocess high-water marks
stn_mod = stn_utils.preprocess_stn(stn_raw, attr_list, check_list, date_threshold, stn_mod_file)

# complete and calculate the runtime
print('\nCOMPLETE - STN FLOOD EVENT DATA COLLECTION AND PREPROCESSING')
end = time.time()
print(f'\nRUNTIME: {round((end - start) / 60, 2)} minutes')



