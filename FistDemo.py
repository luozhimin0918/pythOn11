# print("1 is equal to 2")
# if True:
#     print ("wo are True")
# else:
#     print ("wo are False")
#
# if 3 < 1:
#     print ("dddd")
# elif 4 > 5:
#     print ("ffff")
# else:
#     print ("kkkk")

# news = 1
# while news <= 10:
#     print (news)
#     news += 1

# loop_condition = True
# while loop_condition:
#     print("Loop Condition keeps: %s" %(loop_condition))
#     loop_condition = True

# for i in range(1, 11):
#     print (i)

# my_integers = [5, 7, 1, 3, 4]
# print(my_integers[0])
# print(my_integers[1])
# print(my_integers[4])

# relatives_names = ["Toshiaki",  "Juliana",  "Yuji",  "Bruno",  "Kaio"]
# print(relatives_names[4])


# bookshelf = []
# bookshelf.append("The Effective Engineer")
# bookshelf.append("The 4 Hour Work Week")
# print(bookshelf[0])
# print(bookshelf[1])


# dictionary_example = {
#   "key1": "value1",
#   "key2": "value2",
#   "key3": "value3"
# }
# print("My name is %s" %(dictionary_example["key1"]))  # My name is Leandro
# print("But you can call me %s" %(dictionary_example["key2"]))  # But you can call me Tk
# print("And by the way I'm %s" %(dictionary_example["key3"]))  # And by the way I'm Brazilian


# dictionary_tk = {
#   "name": "Leandro",
#   "nickname": "Tk",
#   "nationality": "Brazilian",
#   "age": 24
# }
# print("My name is %s" % (dictionary_tk["name"]))
# print("But you can call me %s" % (dictionary_tk["nickname"]))
# print("And by the way I'm %i and %s" % (dictionary_tk["age"], dictionary_tk["nationality"]))


# bookshelf = [
#   "The Effective Engineer",
#   "The 4 hours work week",
#   "Zero to One",
#   "Lean Startup",
#   "Hooked"
# ]
# for book in bookshelf:
#     print(book)

# dictionary = {"some_key": "some_value","non_key":"one_value"}
# for key in dictionary:
#     print("%s --> %s" % (key, dictionary[key]))  # some_key --> some_value


dictionary = {"some_key": "some_value", "non_key": "one_value"}
for attr, value in dictionary.items():
    print("%s --> %s" % (attr, value))


from VerCar import VerCar
car = VerCar(2, 3, 3)
print (car.SpeedTwoNum)