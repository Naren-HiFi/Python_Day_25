'''

            Day 25 => Working with CSV Files and Analysing Data with Pandas

                   Pandas is one of the most popular python data analysis libraries

with open('weather_data.csv') as csv_file:
    data = csv_file.readlines()
    print(data)


import csv

with open('weather_data.csv') as csv_file:
    data = csv.reader(csv_file)
    temperatures = []
    for row in data:
        temp = row[1]
        if temp != 'temp':
            int_temp = int(temp)
            temperatures.append(int_temp)

    print(temperatures)


import pandas

data = pandas.read_csv('weather_data.csv')
print(type(data))
temp_column = data["temp"]
print(type(temp_column))
print(temp_column)

data_dict = data.to_dict()
print(data_dict)

temp_list =  data["temp"].to_list()
print(temp_list)

temperature = 0
for temp in temp_list:
    temperature += temp
sum_of_temperature = temperature
number_of_temp = len(temp_list)

average = sum_of_temperature/number_of_temp
print(average)

average_of_temperature = sum(temp_list)/number_of_temp
print(average_of_temperature)

mean_temperature = temp_column.mean()
print(mean_temperature)

max_value = 0
for temp in temp_list:
    if temp > max_value:
        max_value = temp
print(max_value)

max_temp = temp_column.max()
print(max_temp)

#Get data in columns
condition_column = data["condition"]
print(condition_column)
print(data.condition)

#Get data in rows
print(data[data.day == "Monday"])
print(data[data.temp == max_temp])

monday = data[data.day == "Monday"]
print(monday.condition)
#monday_temp = int(monday.temp)
monday_temp_F = monday_temp * 9/5 + 32
print(monday_temp_F)

# Create a dataframe from scratch
data_dictionary = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}
data_one = pandas.DataFrame(data_dictionary)
print(data_one)

convert_Data_To_Csv = data_one.to_csv("new_data.csv")
'''

#Central Park Squirrel Data Analysis
import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
print(grey_squirrels_count)
print(red_squirrels_count)
print(black_squirrels_count)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")
