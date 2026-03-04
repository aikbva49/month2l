class Car:
    #инициализатор (конструктор)
    def __init__(self, color, model):
        self.color = color
        self.model = model

    def drive_to(self, destination):
        print (f"машина {self.model} едет в {destination}")

car1 = Car(color='black', model='Dodge RAM trx 6*6')
car2 = Car(color='black', model='chevloret camaro zl1')

print("Car1:", car1.color, car1.model)
print("Car2:", car2.color, car2.model)
print(type(car1))
car1.drive_to("бишкек")