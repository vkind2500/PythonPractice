import math

class Circle:
    def __init__(self,radius):
        self._radius = radius
        self._area = None
    
    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self,radius):
        if radius <= 0:
            raise ValueError('Radius should be greater > 0')
        else:
            if self._radius != radius:
                self._radius = radius
                self._area = None
    
    @radius.deleter            
    def radius(self):
        del self._radius            
    
    @property
    def area(self):
        if self._area is None:
            self._area = math.pi*math.pow(self._radius,2)
        return self._area
    
circle = Circle(10)
print(f'Area of Circle is {circle.area}')   

print(circle.__dict__)

del circle.radius

print(circle.__dict__) 