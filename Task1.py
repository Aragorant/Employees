import csv
import random
from faker import Faker
from faker.providers import BaseProvider

class CustomProvider(BaseProvider):
    def female_middle_name(self):
        female_middle_names = [
            "Миколаївна",
            "Володимирівна",
            "Олександрівна",
            "Іванівна",
            "Василівна",
            "Сергіївна",
            "Вікторівна",
            "Михайлівна"
        ]
        return self.random_element(female_middle_names)

    def male_middle_name(self):
        male_middle_names = [
            "Миколайович",
            "Володимирович",
            "Олександрович",
            "Іванович",
            "Васильович",
            "Сергійович",
            "Вікторович",
            "Михайлович"
        ]
        return self.random_element(male_middle_names)

fake = Faker('uk_UA')
fake.add_provider(CustomProvider)

total_records = 2000

records = []

for i in range(total_records):
    if i < total_records * 0.4:
        gender = "Жіноча"
        name = fake.first_name_female()
        middle_name = fake.female_middle_name()

    else:
        gender = "Чоловіча"
        name = fake.first_name_male()
        middle_name = fake.male_middle_name()

    birthdate = fake.date_of_birth(minimum_age=15, maximum_age=85)
    record = {
        "Прізвище": fake.last_name(),
        "Ім’я": name,
        "По батькові": middle_name,
        "Стать": gender,
        "Дата народження": birthdate,
        "Посада": fake.job(),
        "Місто проживання": fake.city(),
        "Адреса проживання": fake.address(),
        "Телефон": fake.phone_number(),
        "Email": fake.email()
    }
    records.append(record)

random.shuffle(records)

with open('employees.csv', mode='w', newline='', encoding='utf-8') as csv_file:
    fieldnames = ["Прізвище", "Ім’я", "По батькові", "Стать", "Дата народження",
                  "Посада", "Місто проживання", "Адреса проживання", "Телефон", "Email"]

    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()

    for record in records:
        writer.writerow(record)

print("Генерація завершена. Файл employees.csv створено.")
