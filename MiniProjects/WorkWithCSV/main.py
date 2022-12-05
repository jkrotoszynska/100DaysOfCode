# 1
# with open("weather_data.csv") as file:
#     file = file.readlines()
#     print(file)

#2
# import csv

# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temp = []
#     for item in data:
#         if item[1] != "temp":
#             temp.append(int(item[1]))
#         print(item)

# print(temp)

#3
import pandas

data = pandas.read_csv("weather_data.csv")

temp_list = data["temp"].to_list()
print(temp_list)

average = sum(temp_list) / len(temp_list)
print(round(average, 1))

print(data["temp"].mean())

max_temp = data["temp"].max()
print(max_temp)