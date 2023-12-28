class Line():

    pi = 3.14

    def __init__(self, coord1, coord2):
        self.coord1 = coord1
        self.coord2 = coord2

    def distance(self):
        x1,y1 = self.coord1
        x2,y2 = self.coord2
        dist = (((y2-y1)**2) + ((x2-x1)**2))**0.5
        return dist
    
    def slope(self):
        x1,y1 = self.coord1
        x2,y2 = self.coord2
        if (x2-x1) == 0:
            return "NA"
        
        else:
            return (y2-y1) / (x2-x1)
        


class Cylinder:
    
    pi = 3.14

    def __init__(self,height=1,radius=1):
        self.height = height
        self.radius = radius
        
    def volume(self):
        return self.pi * (self.radius ** 2) * self.height
    
    def surface_area(self):
        return 2 * self.pi * self.radius * (self.radius + self.height)



if __name__ == "__main__":
    # line = Line((3,2), (8,10))
    # print(line.distance())
    # print(line.slope())

    cylinder = Cylinder(2,3)
    print(cylinder.volume())
    print(cylinder.surface_area())