import csv
import pandas

data = pandas.read_csv("data.csv")

temp_data = data["temp"].to_list()

