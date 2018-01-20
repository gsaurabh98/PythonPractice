import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# For this capstone project we will be analyzing some 911 call data from Kaggle. The data contains the following fields:
#
# lat : String variable, Latitude
# lng: String variable, Longitude
# desc: String variable, Description of the Emergency Call
# zip: String variable, Zipcode
# title: String variable, Title
# timeStamp: String variable, YYYY-MM-DD HH:MM:SS
# twp: String variable, Township
# addr: String variable, Address
# e: String variable, Dummy variable (always 1)
# Just go along with this notebook and try to complete the instructions or
# answer the questions in bold using your Python and Data Science skills!

#Data and Setup


df = pd.read_csv('911.csv')
print df.head()