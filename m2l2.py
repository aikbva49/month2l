class Car:
    #инициализатор (конструктор)
    def __init__(self, color, model):
        self.color = color
        self.model = model

    def drive_to(self, destination):
        print (f"машина {self.model} едет в {destination}")


class bus(Car):
    pass



class track:
    pass

bus_40 = bus(color='green', model='matiz')