# get_data.py

import requests
import json


print("REQUESTING SOME DATA FROM THE INTERNET...")
print("")

request_url = "https://raw.githubusercontent.com/prof-rossetti/intro-to-python/master/data/products.json"
response = requests.get(request_url)
print(type(response))
print("")

print(response.status_code)
print("")

parsed_response = json.loads(response.text)

print(parsed_response)
print("")

for d in parsed_response:
    print(d["name"])
    print(d["id"])
    print("")

print( parsed_response[0]["name"])

print("DONE WITH THE PRODUCTS DATA\n")
print("NOW MOVING TO GRADES DATA\n")

request_url1 = "https://raw.githubusercontent.com/prof-rossetti/intro-to-python/master/data/gradebook.json"
response1 = requests.get(request_url1)

print(response1.status_code)
print("")

parsed_response1 = json.loads(response1.text)


#local variables
grades_list = []
subtotal = 0.0
average = 0.0
grades_list = parsed_response1["students"]

for d in grades_list:
    subtotal += d["finalGrade"]

#list comprehension method
#grades_list = [student["finalGrade"] for student in pased_response1["students"]]


average = subtotal / len(grades_list)
average = str(round(average, 2))

print("The average grade is:", f"{average}%")
print("")



