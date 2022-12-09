import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

title = "Primary Fur Color"
#print(data[title].drop_duplicates())
#print(data[title].unique())

gray_rows = data[data[title] == 'Gray']
gray_rows_count = len(gray_rows)

cinnamon_rows = data[data[title] == 'Cinnamon']
cinnamon_rows_count = len(cinnamon_rows)

black_rows = data[data[title] == 'Black']
black_rows_count = len(black_rows)


data_dict = {
    "Fur Color" : ["Gray", "Cinnamon", "Black"],
    "Count" : [gray_rows_count, cinnamon_rows_count, black_rows_count]
}

df = pandas.DataFrame(data_dict)
print(df)

df.to_csv("squirrel_count.csv")