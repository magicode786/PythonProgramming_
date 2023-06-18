class StarPattern:
    def __init__(self):
        pass
    def SquareStarPattern(self):
        pass
class SquarePatter_class(StarPattern):
    def __init__(self, pattern_size):
        self.pattern_size = pattern_size
    def SquareStarPattern(self):
        print(f"The size of the Pattern is:{self.pattern_size}")
        for row in range(0,self.pattern_size):
            print("* "*self.pattern_size)
class HollowSquarePatter_class(StarPattern):
    def __init__(self, pattern_size):
        self.pattern_size = pattern_size
    def HollowSquareStarPattern(self):
        print(f"The size of the Pattern is:{self.pattern_size}")
        for row in range(0,self.pattern_size):
            # Loop through rows
            #     # Loop to print pattern
            for col in range(self.pattern_size):
                if  row == 0 or row == self.pattern_size-1:
                    print('*' , end=' ')
                elif row >=1 or  row <= self.pattern_size-1:
                    if col == 0 or col == self.pattern_size-1:
                        print('*' , end=' ')
                    else:
                        print(' ', end=' ')
                        
                else:
                    pass
            print()
            
class RightTrianglePatter_class(StarPattern):
    def __init__(self, pattern_size):
        self.pattern_size = pattern_size
    def RightTriangleSquareStarPattern(self):
        print(f"The size of the Pattern is:{self.pattern_size}")
        for row in range(0,self.pattern_size+1):
            print("* "*row)
        ##or this logic can also be used
        for i in range(self.pattern_size+1):
        # nested loop
            for j in range(i):
                # display number
                print("*", end=' ')
            # new line after each row
            print('')
            
            
def main():
    pattern_size = getPatternSize()
    print(f"Pattern Size requested:{pattern_size}")
    squarePattern = SquarePatter_class(pattern_size)
    squarePattern.SquareStarPattern()
    HollowsquarePattern = HollowSquarePatter_class(pattern_size)
    HollowsquarePattern.HollowSquareStarPattern()
    RightTrianglepattern=RightTrianglePatter_class(pattern_size)
    RightTrianglepattern.RightTriangleSquareStarPattern()

def getPatternSize():
    user_pattern_size = int(input("Enter the Pattern Size you would like to see\n"))
    return user_pattern_size

if __name__ == "__main__":
    main()


        