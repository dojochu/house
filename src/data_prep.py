import pandas as pd
import sys

def read_house_data(resource_path):
    data = pd.read_csv(resource_path+'train.csv')
    return data