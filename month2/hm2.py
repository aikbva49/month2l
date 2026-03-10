class Person:
    def __init__(self, name, birth_date, profession):
        self.name = name
        self.birth_date = birth_date
        self.profession = profession

    def introduce(self):
        print(f'Привет, меня зовут {self.name}. Я родился {self.birth_date}, по профессии я {self.profession}.'


class Classmate(Person):
    def __init__(self, name, birth_date, profession, group_name):
        super().__init__(name, birth_date, profession)
        self.group_name = group_name

    def introduce(self):
        print(f'Привет, меня зовут {self.name}. Я одногруппник из группы {self.group_name}. '
              f'Я родился {self.birth_date}, по профессии я {self.profession}.')


class Friend(Person):
    def __init__(self, name, birth_date, profession, hobby):
        super().__init__(name, birth_date, profession)
        self.hobby = hobby

    def introduce(self):
        print(f'Привет, меня зовут {self.name}. Я друг. '
              f'Я родился {self.birth_date}, моя работа {self.profession}, мое хобби — {self.hobby}.')


class BestFriend(Friend):
    def __init__(self, name, birth_date, profession, hobby, shared_memory):
        super().__init__(name, birth_date, profession, hobby)
        self.shared_memory = shared_memory

    def introduce(self):
        print(f'Привет, меня зовут {self.name}. Я лучший друг. '
              f'Я родился {self.birth_date}, моя работа {self.profession}, мое хобби — {self.hobby}.')
        print(f'Наше общее воспоминание с лучшим другом: {self.shared_memory}')


classmate1 = Classmate("Артем", "05.12.2008", "программист", "ЕПИ-2")
classmate2 = Classmate("Тариэл", "10.03.2007", "разработчик", "ЕПИ-2")

friend1 = Friend("Арлан", "12.07.2007", "инженер", "коллекционировать ножи")
friend2 = Friend("Даулет", "21.09.2007", "пилот", "сноубординг")

best_friend = BestFriend("Арсен", "15.05.2007", "предприниматель", "играть шахматы", "посещение игр Великих игр кочевников и поездка в Казахстан")


classmate1.introduce()
classmate2.introduce()
friend1.introduce()
friend2.introduce()
best_friend.introduce()