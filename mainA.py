# print("Jolanta")
#
# print("Hello")
#
# string = "My name is"
# print(string)
# print(type(string))
# print(type("Jolanta"))
# float = 1.99
# print(type(1.99))
# print(type(True))
# name_of_the_variable = "Jolanta"
# print(name_of_the_variable)

# dial_code = "+371"
# country = "LV"
# def print_the_number_of_the_country():
#     print(f"I am from {country} and the dial code is {dial_code}")
#
# print_the_number_of_the_country()
#
# def add_two_numbers():
#     print(1+2)
#
# add_two_numbers()
#
# def print_my_name():
#     print("Hello User")
#
# print_my_name()

#name = input()
#surname = input()
#def my_name_is():
#    print(f"May name is {name} {surname}")

#my_name_is()


""""Ā list can have different type of data. It can be a string, integer, float and a boolean"""

# list = ["Jolanta", 12, 1.99, True, False]
# print(list[0])
# print(list[4])

""""We know how to define string, integer, float, list and calling an element from the list"""
#
# dictionary = {"name": "Jolanta", "surname": "Ijannidi", "age": 38, "my_orders": [1, 2, 3, 4, 5]}
#
# json_formated = {
#     "name": "Jolanta",
#     "surname": "Ijannidi",
#     "age": 38,
#     "my_orders": [1, 2, 3, 4, 5]
# }
#
# print(len(dictionary))
# print(dictionary)
# print(dictionary["my_orders"])
#
# my_cv = {
#     "name": "value",
#     "experience": 1
# }

"""The moon missions are called as Apolo. There are 17 apolo missions and we are describing 3 out of them.
The missions 11 & 12 happened in 1969, on the months Jul and Nov. But the 13 on April 1970.
Out of the 3, apollo third was unsucessfull. The first moon landing was by apolo 11 by the 
astronauts Neil Armstrong, Edwin Aldrin & Michael Collins.
Apolo 12 was with Astronauts, Charles Conrad, Alan Bean & Richard Gordon, whereas Apolo 13 had John Swigert, 
James Lovell and Fred Haise."""

moon_mission_apolo = [
    {"number_of_missions": 17},
    {
    "name_of_mission": "Apolo 11",
    "month_of_mission": "Jul",
    "year_of_mission": 1969,
    "participants": ["Neil Armstrong", "Edwin Aldrin", "Michael Collins"],
    "is_success": True
    },
    {
    "name_of_mission": "Apolo 12",
    "month_of_mission": "Nov",
    "year_of_mission": 1969,
    "participants": ["Charles Conrad", "Alan Bean", "Richard Gordon"],
    "is_success": True
    },
    {
    "name_of_mission": "Apolo 13",
    "month_of_mission": "April",
    "year_of_mission": 1970,
    "participants": ["John Swigert", "James Lovell", "Fred Haise"],
    "is_success": False
    }
]
print(moon_mission_apolo[0])

year = moon_mission_apolo[2]["year_of_mission"]
if year > 1969:
    print(year)
#mutable
list = [1, 2, 3]

#immutable - no update for tuple, use for example for year of production
tuple = ("a", "b", "c")

list.append(10)
print(list)

set = {1, 2, 3, 4, 5, 5, 100, 1000}
print(set)

""""Input function: sum(), print(), sort(), append(), max()"""
# print(input("Do you want to apply: (type yes)"))

""""Global variable"""
need_your_name = "Zane Ieva"

def welcome(name, surname):
    print(f"Hello user {name} {surname}")


welcome("Jolanta", "Ijannidi")

# while True:
#     voice = input()
#     if voice == "alex":
#         print("I am on")