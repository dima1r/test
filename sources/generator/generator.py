from sources.data.data import Person
from faker import Faker
import random

faker_en = Faker('en_US')
Faker.seed(0)

def generated_person():
    yield Person(
        full_name=faker_en.first_name() + faker_en.last_name(),
        firstname=faker_en.first_name(),
        lastname=faker_en.last_name(),
        age=random.randint(18, 99),
        salary = random.randint(10000, 15000),
        department=faker_en.job(),
        email=faker_en.email(),
        current_address=faker_en.address(),
        permanent_address=faker_en.address(),
        mobile=faker_en.msisdn(),
    )

def generated_file():
    path = rf'C:\Files\filetst{random.randint(0, 999)}.txt'
    file = open(path, 'w+')
    file.write('Hello, World')
    file.close()
    return file.name, path