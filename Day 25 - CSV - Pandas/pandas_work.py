import csv
import pandas

data = pandas.read_csv("data.csv")

temp_data = data["temp"].to_list()

data_dict = {
    "students": ["Amy", "Angela", "James"],
    "scores": [76, 56, 65]
}

data = pandas.DataFrame(data_dict)

print(data)