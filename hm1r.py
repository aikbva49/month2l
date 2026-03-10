class Person:
    def __init__(self, name, birth_date, occupation, higher_education):
        self.name = name
        self.birth_date = birth_date
        self.occupation = occupation
        self.higher_education = higher_education

    def introduce(self):
        print(f"Меня зовут {self.name}, я родился {self.birth_date}, "
              f"по профессии я {self.occupation}, высшее образование: {self.higher_education}")


person1 = Person("Алия Аскарова", "15.03.1995", "инженер", True)
person2 = Person("Тилек Мукашев", "22.07.1998", "архитектор", False)
person3 = Person("Алмаз Русланов", "01.12.1990", "программист", True)


print("person1:")
print(person1.name, person1.birth_date, person1.occupation, person1.higher_education)
print()

print("person2:")
print(person2.name, person2.birth_date, person2.occupation, person2.higher_education)
print()

print("person3:")
print(person3.name, person3.birth_date, person3.occupation, person3.higher_education)
print()


person1.introduce()
person2.introduce()
person3.introduce()