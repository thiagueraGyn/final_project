import pandas as pd
import numpy as np
import matplotlib as plt
import seaborn as sns

def load_data():
    df = pd.read_csv('titanic-data-6.csv')
    return df


if __name__ == '__main__':
    load_data()