import os

os.chdir(os.path.join(os.getcwd(), '12_Project/'))

import census2010

print(census2010.alldata['AK']['Anchorage'])