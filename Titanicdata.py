# how to download the csv file
import urllib.request
import requests
import pandas as pd

titanic_data = pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")

titanic_data.to_csv('Titanic.csv', sep = ',',index = True)