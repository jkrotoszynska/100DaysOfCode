import csv

# with open("weather_data.csv") as file:
#     file = file.readlines()
#     print(file)

with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    for item in data:
        print(item)