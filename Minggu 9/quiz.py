
from itertools import count
from unittest import result


people = [
    {'name': 'bob', 'age': 20, 'score':{'math':90,'science':70}},
    {'name': 'carry', 'age': 38, 'score':{'math':40,'science':72}},
    {'name': 'smith', 'age': 28, 'score':{'math':80,'science':90}},
    {'name': 'john', 'age': 34, 'score':{'math':75,'science':100}}
]

science_score = people[2]['score']['science']
print(science_score)

num_list = [1, 2, 3, 6, 3, 2, 4, 5, 6, 2, 4]

for num in num_list:
    if num % 2 == 0:
        print(num)

num_list = [1, 2, 3, 6, 3, 2, 4, 5, 6, 2, 4]        

count = 0

for num in num_list:
    if num % 2 == 0:
        count += 1

print(count)        

num_list = [1, 2, 3, 6, 3, 2, 4, 5, 6, 2, 4] 

result = 0

for num in num_list:
    result += num

print(result) 

num_list = [1, 2, 3, 6, 3, 2, 4, 5, 6, 2, 4] 

max_value = 0

for num in num_list:
    if num > max_value:
        max_value = num

print(max_value)

def check_gender(pin):
    num = int(pin.split('-')[1][0])

    if num % 2 == 0:
        print('female')
    else:
        print('male')

my_pin = '200101-4012345'

check_gender(my_pin)

def division(x,y):
    print(x/y)

division(1024,512)