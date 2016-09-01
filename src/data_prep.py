import pandas as pd
import sys

def read_house_data(resource_path):

    data = pd.read_csv(resource_path+'train.csv')
    cat_var = data.columns[data.dtypes == "object"].tolist()
    cat_var.extend(['MSSubClass'])
    for col in cat_var:
        data[col] = data[col].astype('category')


    return data