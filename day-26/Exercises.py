# # Ex-1
#
# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# # 🚨 Do Not Change the code above 👆
#
# # Write your 1 line code 👇 below:
# squared_numbers = [n**2 for n in numbers]
#
# # Write your code 👆 above:
#
# print(squared_numbers)

# # EX-2
#
# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# # 🚨 Do Not Change the code above
#
# # Write your 1 line code 👇 below:
# result = [num for num in numbers if num % 2 == 0]
#
# # Write your code 👆 above:
#
# print(result)

# # Ex-3
#
#
# data_1 = []
# data_2 = []
#
# with open("file1.txt") as file:
#     data_1 = [int(num) for num in file.readlines()]
# with open("file2.txt") as file:
#     data_2 = [int(num) for num in file.readlines()]
#
# result = [num for num in data_1 if num in data_2]
# print(result)

# # Ex-4
# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# # Don't change code above 👆
# result = {item: len(item) for item in sentence.split()}
# # Write your code below:
#
#
# print(result)

# Ex-5

weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}


# 🚨 Don't change code above 👆


# Write your code 👇 below:
def fahrenheit_convertor(degree):
    return degree * 1.8 + 32


weather_f = {day: fahrenheit_convertor(temp) for (day, temp) in weather_c.items()}

print(weather_f)