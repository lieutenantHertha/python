import math

class Vector:
    def __init__(self, demension_x, demension_y):
        self.demension_x = demension_x
        self.demension_y = demension_y
    
    def __repr__(self):
        return "Vector({}, {})".format(self.demension_x, self.demension_y)

    def __add__(self, other):
        new_demension_x = self.demension_x + other.demension_x
        new_demension_y = self.demension_y + other.demension_y
        return Vector(new_demension_x, new_demension_y)
    
    def __mul__(self, scalar):
        return Vector(self.demension_x * scalar, self.demension_y * scalar)

    def __abs__(self):
        magnitute = math.hypot(self.demension_x, self.demension_y)
        return magnitute
    
    def __bool__(self):
        return bool(abs(self))

v1 = Vector(3, 4)
v2 = Vector(5, 12)
v3 = Vector(7, 24)

print(v2 * 3)


        
