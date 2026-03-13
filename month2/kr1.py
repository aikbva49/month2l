class Animal:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        self.__age = age

    def make_sound(self):
        print(f'{self.__name}, издает звук')


class Dog(Animal):
    def make_sound(self):
        print(f'{self.get_name()}, издает звук: гав')


class Cat(Animal):
    def make_sound(self):
        print(f'{self.get_name()}, издает звук: мяу')


dog = Dog('Айва', 3)
kitty = Cat('Муиза', 1)

dog.set_name('Зорька')
kitty.set_age(2)

dog.make_sound()
kitty.make_sound()

print(f'возраст: {dog.get_name()} {dog.get_age()}')
print(f'возраст: {kitty.get_name()} {kitty.get_age()}')