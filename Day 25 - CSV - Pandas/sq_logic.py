import pandas

data = pandas.read_csv("sq_data.csv")

gray_squirrel = data[data["Primary Fur Color"] == "Gray"]
gray_squirrel_count = len(data[data["Primary Fur Color"] == "Gray"])

print(gray_squirrel_count)
