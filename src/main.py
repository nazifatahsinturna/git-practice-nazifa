from datetime import date
import utils
print("Nazifa Tahsin") #my name
print(date.today()) # today's date

#using functions from utils.py
print(utils.add(6, 7))
print(utils.subtract(7, 3))

#using the new fuction
print(utils.multiply(5, 8))

#checking error handling
print(utils.add(5, "hi"))