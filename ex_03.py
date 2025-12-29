# ******************************************
 # * @Author : Ali Azhari   
 # * Created On : Mon Dec 29 2025
 # * @File : ex_03.py
 # *
 # * Description: Working with DataFrame
#  * *****************************************

import pandas as pd

mydataset = {
 "cities": ["Boston", "Chicago", "Seattle"],
  "population_millions": [0.7, 2.6, 0.75]
}

myvar = pd.DataFrame(mydataset)

print(myvar)

