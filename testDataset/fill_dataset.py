import re, random
from string import ascii_letters
from studentsql import StudentDatabase

names = open("names.txt", "r+", encoding="utf8").read().split("\n")

student_database = StudentDatabase(r"C:\Users\Abdul\PycharmProjects\StudentDatabase\student_database.db")

addresses = ["Broadway BRISTOL","St. John’s Road BRADFORD", "Kingsway ROCHESTER"]

for number, name in enumerate(names):
    first_name =  name
    last_name = random.choice(names)
    student_id = f"{first_name}.{last_name}{number}"
    age = random.randint(17,30)
    gender = random.choice(["male", "female"])
    address =f"{random.randint(1,500)} {random.choice(addresses)}"
    postcode = f"{random.choice(ascii_letters)}{random.choice(ascii_letters)}{random.randint(0,10)} {random.randint(0,10)}{random.choice(ascii_letters)}{random.choice(ascii_letters)}"
    mobile =f"07{random.randint(100000000,999999999)}"
    subject_score = random.randint(0,100)


    student_info = {'student_id': student_id,
                    'first_name':first_name,
                    'last_name': last_name,
                    'gender': gender,
                    'age': age,
                    'address': address,
                    'postcode': postcode,
                    'mobile': mobile,
                    'chemistry': random.randint(0,100),
                    'computing': random.randint(0,100),
                    'english': random.randint(0,100),
                    'physics': random.randint(0,100),
                    'biology': random.randint(0,100),
                    'business': random.randint(0,100),
                    'maths': random.randint(0,100),
                    'add_math': random.randint(0,100),
                    }

    student_database.add_student(student_info)

student_database.commit()