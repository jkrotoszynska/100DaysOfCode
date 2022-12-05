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
print("------------------------")

average = sum(temp_list) / len(temp_list)
print(round(average, 1))
print("------------------------")

# Get Data in Columns
print(data["temp"].mean())
print("------------------------")

max_temp = data["temp"].max()
print(max_temp)
print("------------------------")

print(data.condition)
print("------------------------")

# Get Data in Row
print(data[data.day == "Monday"])
print("------------------------")

print(data[data.temp == data.temp.max()])
print("------------------------")

monday = data[data.day == "Monday"]
print(monday.condition)
print("------------------------")

monday_temp = int(monday.temp)
monday_temp_f = monday_temp * 9/5 + 32
print(monday_temp_f)
print("------------------------")

# Create a dataframe from scratch
data_dict = {
    "students" : ["Amy", "James", "Angela"],
    "scores" : [76, 56, 65]
}
data = pandas.DataFrame(data_dict)
print(data)
print("------------------------")

data.to_csv("new_data.csv")