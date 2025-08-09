'''
list = [11,22,3,2,3,1,45,1]
list.append(1)
print(list)
list.pop(3)
print(list)
list.remove(22)
print(list)
list.insert(0,100)
print(list)
list.sort()
print(list)

set = {1,2,3,4,5}
set.discard(5)
set.add(6)
set.update([8,9])
print(set)


tuple = (1,2,3,4,5,5)
print(tuple)
print(tuple[0])


zoo = ["monkey","dog","cat","pig","horse"]
print(zoo)
zoo.pop(2)
print(zoo)
zoo.append("elephant")
print(zoo)
zoo.pop(0)
print(zoo)
print(zoo[2])



grede = 33

if grede >= 90:
    print("A")
elif 80 <= grede < 90:
    print("B")
elif 70 <= grede < 80:
    print("C")
elif 60 <= grede < 70:
    print("D")
else:
    print("E")



my_list = ["Monday","tuesday","wednesday","thursday","friday"]
i = 0
while i < 3:
    for literator in my_list:
        if literator == "Monday":
            continue
        print(literator)
    i += 1


user_dictionary = {
    "name":"yuto",
    "age":21,
    "sex":"male"
}

user_dictionary["joy"] = "soccer"
print(user_dictionary)

for z,y in user_dictionary.items():
    print(z,y)

user_dictionary2 = user_dictionary.copy()
user_dictionary2.pop("name")
print(user_dictionary2)
print(user_dictionary)



my_vehicle = {
    "model": "Ford",
    "make": "Explorer",
    "year": 2018,
    "mileage": 40000
}

for x,y in my_vehicle.items():
    print(x,y)

vehicle2 = my_vehicle.copy()
vehicle2["number_of_tries"] = 4
del vehicle2["mileage"]
print(vehicle2.keys())


def print_my_name(name,age):
    print(name)
    print(age)

print_my_name(name="yuto",age =21)

def mulitiple_number(a,b):
    return a*b

soluton = mulitiple_number(3,7)
print(soluton)

def print_list(number_list):
    for x in number_list:
        print(x)

number = [1,2,3,4,5]
print_list(number)


def user_name_database(first_name,last_name,age):
    return {
        "first_name":first_name,
        "last_name":last_name,
        "age":age
    }

print(user_name_database("yuto","shimomura","21"))

#高階関数
def buy_cost(item_price):
    return item_price + item_add_tax(item_price)

def item_add_tax(item_price):
    tax_rate = .03
    return item_price*tax_rate

print(buy_cost(600))


import useful_asemble.grade_avarage_service as g

home_work_assignment = {
    1:100,
    2:58,
    3:75
}

result = g.caculate_homework(home_work_assignment)
print(result)

import random as r
aaa = r.randint(1,100)
print(aaa)

'''


