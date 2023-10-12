import csv
import matplotlib.pyplot as plt
from datetime import datetime

def calculate_age(birthdate):
    today = datetime.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age

def calculate_statistics():
    try:
        with open('employees.csv', mode='r', newline='', encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file)

            age_categories = {"younger_18": {"male": 0, "female": 0},
                              "18-45": {"male": 0, "female": 0},
                              "45-70": {"male": 0, "female": 0},
                              "older_70": {"male": 0, "female": 0}}
            gender_counts = {"male": 0, "female": 0}

            for row in csv_reader:
                birthdate = datetime.strptime(row["Дата народження"], '%Y-%m-%d')
                age = calculate_age(birthdate)
                if age < 18:
                    age_category = "younger_18"
                elif 18 <= age <= 45:
                    age_category = "18-45"
                elif 45 < age <= 70:
                    age_category = "45-70"
                else:
                    age_category = "older_70"

                if row["Стать"] == "Чоловіча":
                    gender_category = "male"
                    gender_counts["male"] += 1
                elif row["Стать"] == "Жіноча":
                    gender_category = "female"
                    gender_counts["female"] += 1
                else:
                    continue

                age_categories[age_category][gender_category] += 1

            print("\nСтатистика за статтю:")
            print(f"Чоловіки: {gender_counts['male']} співробітників")
            print(f"Жінки: {gender_counts['female']} співробітників")

            print("\nСтатистика за віком:")
            for category, counts in age_categories.items():
                print(f"{category}: {counts['male'] + counts['female']} співробітників")

            print("\nСтатистика за статтю та віком:")
            for category, counts in age_categories.items():
                print(f"{category}: Чоловіки - {counts['male']}, Жінки - {counts['female']}")

            build_age_bar_chart(age_categories)
            build_gender_age_stacked_bar_chart(age_categories)
            build_gender_pie_chart(gender_counts)

            print("Ok")

    except FileNotFoundError:
        print("Повідомлення про відсутність, або проблеми при відкритті файлу CSV.")
    except Exception as e:
        print("Помилка:", str(e))

def build_age_bar_chart(age_categories):
    categories = list(age_categories.keys())
    total_counts = [counts["male"] + counts["female"] for counts in age_categories.values()]
    plt.figure()
    plt.bar(categories, total_counts, color='teal')
    plt.xlabel('Вікова категорія')
    plt.ylabel('Кількість співробітників')
    plt.title('Статистика за віком')
    plt.xticks(rotation=45)

def build_gender_age_stacked_bar_chart(age_categories):
    categories = list(age_categories.keys())
    male_counts = [counts["male"] for counts in age_categories.values()]
    female_counts = [counts["female"] for counts in age_categories.values()]

    bar_width = 0.35
    index = range(len(categories))
    plt.figure()
    plt.bar(index, male_counts, bar_width, label='Чоловіки', color='blue')
    plt.bar(index, female_counts, bar_width, label='Жінки', color='pink', bottom=male_counts)
    plt.xlabel('Вікова категорія')
    plt.ylabel('Кількість співробітників')
    plt.title('Статистика за статтю та віком')
    plt.xticks(index, categories, rotation=45)
    plt.legend()

def build_gender_pie_chart(gender_counts):
    labels = 'Чоловіча стать', 'Жіноча стать'
    sizes = [gender_counts["male"], gender_counts["female"]]
    colors = ['blue', 'pink']
    plt.figure()
    plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
    plt.axis('equal')
    plt.title('Статистика за статтю')

calculate_statistics()
plt.show()
