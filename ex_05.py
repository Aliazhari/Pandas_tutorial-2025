# ******************************************
 # * @Author : Ali Azhari   
 # * Created On : Mon Dec 29 2025
 # * @File : ex_05.py
 # *
 # * Description: Creating lables With the index argument, 
 # * you can name your own labels - Series.
#  * *****************************************


import pandas as pd

a = [1, 7, 2]

myvar = pd.Series(a, index = ["x", "y", "z"])

print(myvar)
