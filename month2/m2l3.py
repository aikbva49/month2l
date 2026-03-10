class Car:
    def __init__(self, color, model):
        self.color = color
        self.model = model
        self.__fined = False
        self.__max_speed = 100

    def _test(self):
        print(f'Test car color: {self.color}, {self.__fined } ')

    def _test2(self):
         print(f'test private method {self.__max_speed} ')

    def drive_to(self, destination):
        if not self.__fined:
            print (f'car {self.model} drive to {destination}, max speed {self.__max_speed}')
        else:
            print('car oshtrafovana')
            self.__test2()

    def change_color(self, new_color):
        self.color = new_color

car_m = Car(color='black', model='f')
car_m._test()
print(car_m.color)
car_m.drive_to('karakol')
print(car_m._Car__max_speed)
car_m.__max_speed = 50
car_m.drive_to('karakol')

