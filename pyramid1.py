class StarPattern:
    def __init__(self):
        pass
    def SquareStarPattern(self):
        pass

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

#class MirrorRightTrianglePatter_class(StarPattern):


class PyramidPattern(StarPattern):
    def __init__(self, pattern_size):
        self.pattern_size = pattern_size
    def PyramidPatternfunc(self):
        print(f"The size of the Pattern is:{self.pattern_size}")
        cnt = self.pattern_size
        for row in range(0,self.pattern_size+1):
            print(" "*(cnt), end='')
            print("* "*row)
            cnt = cnt -  1
class InvertedPyramidPattern(StarPattern):
    def __init__(self, pattern_size):
        self.pattern_size = pattern_size
    def InvertedPyramidPatternfunc(self):
        print(f"The size of the Pattern is:{self.pattern_size}")
        cnt = 0
        pointer = self.pattern_size
        while(pointer+1>=0):
            print(" "*(cnt), end='')
            print("* "*pointer)
            
            cnt = cnt +  1
            pointer = pointer - 1



            
            
def main():
    pattern_size = getPatternSize()
    print(f"Pattern Size requested:{pattern_size}")
    RightTrianglepattern=RightTrianglePatter_class(pattern_size)
    RightTrianglepattern.RightTriangleSquareStarPattern()
    #MirrorRightTrianglepattern=MirrorRightTrianglePatter_class(pattern_size)
    #MirrorRightTrianglepattern.MirrorRightTriangleSquareStarPattern()
    Pyramid = PyramidPattern(pattern_size)
    Pyramid.PyramidPatternfunc()
    InvertedPyramind = InvertedPyramidPattern(pattern_size)
    InvertedPyramind.InvertedPyramidPatternfunc()

def getPatternSize():
    user_pattern_size = int(input("Enter the Pattern Size you would like to see\n"))
    return user_pattern_size

if __name__ == "__main__":
    main()


        

