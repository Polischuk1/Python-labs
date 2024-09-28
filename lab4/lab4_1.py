from faker import Faker
import pandas as pd
import numpy as np
from datetime import date
import random

fake = Faker(locale='uk_UA') 

female_patronymics = [
    "Іванівна", "Олександрівна", "Михайлівна", "Василівна", "Сергіївна",
    "Петрівна", "Андріївна", "Юріївна", "Дмитрівна", "Олегівна",
    "Богданівна", "Миколаївна", "Григорівна", "Олексіївна", "Володимирівна",
    "Артемівна", "Євгенівна", "Вікторівна", "Ігорівна", "Степанівна"
]

male_patronymics = [
    "Іванович", "Олександрович", "Михайлович", "Васильович", "Сергійович",
    "Петрович", "Андрійович", "Юрійович", "Дмитрович", "Олегович",
    "Богданович", "Миколайович", "Григорович", "Олексійович", "Володимирович",
    "Артемович", "Євгенович", "Вікторович", "Ігорович", "Степанович"
]

num_empl = 2000
num_female = int(num_empl * 0.4)  
num_male = num_empl - num_female    
employee_list = []

for _ in range(num_male):
    employee = {}
    gender = "Ч"  
    patronymic = random.choice(male_patronymics)
    
    employee["Ім'я"] = fake.first_name_male()  
    employee['Прізвище'] = fake.last_name()  
    employee["По-батькові"] = patronymic  
    employee['Стать'] = gender
    employee['Дата народження'] = fake.date_between_dates(date_start=date(1938, 1, 1), date_end=date(2008, 12, 31))  
    employee['Посада'] = fake.random_element(elements=('Manager', 'Developer', 'Analyst', 'HR')) 
    employee['Місто'] = fake.city() 
    employee['Телефон'] = fake.phone_number() 
    employee['Email'] = fake.email() 

    employee_list.append(employee)

for _ in range(num_female):
    employee = {}
    gender = "Ж"  
    patronymic = random.choice(female_patronymics)
    
    employee["Ім'я"] = fake.first_name_female()  
    employee['Прізвище'] = fake.last_name()  
    employee["По-батькові"] = patronymic  
    employee['Стать'] = gender
    employee['Дата народження'] = fake.date_between_dates(date_start=date(1938, 1, 1), date_end=date(2008, 12, 31))  
    employee['Посада'] = fake.random_element(elements=('Manager', 'Developer', 'Analyst', 'HR')) 
    employee['Місто'] = fake.city() 
    employee['Телефон'] = fake.phone_number() 
    employee['Email'] = fake.email() 

    employee_list.append(employee)


random.shuffle(employee_list)

df = pd.DataFrame(employee_list)

df.to_csv(r'C:\Users\User\Desktop\python 4th course\Polishchuk_Olha\lab4\employees.csv', index=False, encoding='utf-8-sig')
