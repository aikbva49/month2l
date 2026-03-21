class Distance:
    def __init__(self, value, unit):
        self.value = value
        self.unit = unit

    def __str__(self):
        return f"{self.value} {self.unit}"

    def to_meters(self):
        if self.unit == "cm":
            return self.value / 100
        elif self.unit == "m":
            return self.value
        elif self.unit == "km":
            return self.value * 1000

    def __add__(self, other):
        total_meters = self.to_meters() + other.to_meters()
        return Distance(total_meters, "m")

    def __sub__(self, other):
        total_meters = self.to_meters() - other.to_meters()
        return Distance(total_meters, "m")


d1 = Distance(10, "m")
d2 = Distance(2, "km")
d3 = Distance(300, "cm")

print(d1)
print(d2)

result_add = d1 + d2
print(result_add)

result_sub = d2 - d1
print(result_sub)

result_add2 = d1 + d3
print(result_add2)