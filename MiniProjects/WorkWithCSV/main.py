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

suma = 0
for t in temp_list:
    suma += t

average = suma / len(temp_list)
print(round(average, 1))