import csv
import pandas as pd


df = pd.read_csv("mainData.csv")

x = df.loc[:, 'lot']


lotNumberDict = x.to_dict()

agent_entry = input('Enter a lot number.')

row_number = lotNumberDict.keys()[lotNumberDict.values().index(str(agent_entry))]

print row_number

def find_address_by_row_number():

    print df.iloc[row_number,37]


find_address_by_row_number()

