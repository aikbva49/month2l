from datetime import datetime

class Person:
    def __init__(self, name, birth_date, occupation, higher_education):
        self.name = name
        self._occupation = occupation
        self._higher_education = higher_education
        self._birth_date = birth_date

    @property
    def occupation(self):
        return self._occupation

    @property
    def higher_education(self):
        return 'есть' if self._higher_education else 'нет'

    @property
    def age(self):
        birth = datetime.strptime(self._birth_date, '%d.%m.%Y')
        today = datetime.today()
        return today.year - birth.year - ((today.month, today.day) < (birth.month, birth.day))

    def introduce(self):
        print(f'Привет, меня зовут {self.name}. Моя профессия {self.occupation}. '
              f'У меня {self.higher_education} высшее образование.')


class Classmate(Person):
    def __init__(self, name, birth_date, occupation, higher_education, group_name):
        super().__init__(name, birth_date, occupation, higher_education)
        self.group_name = group_name

    def introduce(self):
        print(f'Привет, меня зовут {self.name}. По професии я {self.occupation}. '
              f'Я учился с друзьями в группе {self.group_name}. У меня {self.higher_education} высшее образование.')


class Friend(Person):
    def __init__(self, name, birth_date, occupation, higher_education, hobby):
        super().__init__(name, birth_date, occupation, higher_education)
        self.hobby = hobby

    def introduce(self):
        print(f'Привет, меня зовут {self.name}. По професии я {self.occupation}. '
              f'Моим хобби является {self.hobby}. У меня {self.higher_education} высшее образование.')


cl1 = Classmate('Кайрат', '24.06.2002', 'разработчик', True, 'епи-2')
fr1 = Friend('Айбек', '09.03.2001', 'экономист', True, 'футбол')

cl1.introduce()
fr1.introduce()

print(f'{cl1.name} возраст:', cl1.age)
print(f'{fr1.name} возраст:', fr1.age)