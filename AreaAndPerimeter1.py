class GeometricShapes:
    def __init__(self):
        pass
    def CalculateArea(self):
        pass
    def CalculatePerimeter(self):
        pass
class RectangeAreaAndPerimeter(GeometricShapes):
    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth
    def CalculateArea(self):
        return (self.length*self.breadth)
    def CalculatePerimeter(self):
        return 2*(self.length+self.breadth)

def main():
    while(1):
        geometricShape = getGeometricShape()
        print(geometricShape)
        if geometricShape ==  'r' or geometricShape == 'rectangle' :
            length = eval(input("What is the length:  <{}> "))
            breadth = eval(input("What is the breadth:< {} > "))
            if length and breadth:
                rectangle = RectangeAreaAndPerimeter(length,breadth)
                rectangle_area = rectangle.CalculateArea()
                rectangle_perimeter = rectangle.CalculatePerimeter()
                print(f"Area of Rectangle is {rectangle_area} and Perimeter of Rectangle is  {rectangle_perimeter} ")
            else:
                print("Kindly enter non zero values for Length and Breadth")
            
        else:
            print("Kindly Enter the correct Geometric Shape Name")
        
    

def getGeometricShape():
    input_shape = input("Enter the Geometric Shape Name R - Rectangle: " )
    input_shape = input_shape.strip().lower()
    return input_shape


if __name__ == "__main__":
    main()

