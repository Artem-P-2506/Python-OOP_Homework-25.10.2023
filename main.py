from Line import *
from Square import *
from Coordinates import *

def compare(firstOBJ, secondOBJ):
     return str(firstOBJ) == str(secondOBJ)

if __name__ == "__main__":
     square1Coordinates = Coordinates(1, 4)
     square2Coordinates = Coordinates(9, 6)
     line1Coordinates = Coordinates(-3, 8)
     line2Coordinates = Coordinates(-3, 8)

     line1 = Line("black" ,"wood" , line1Coordinates, 10)
     line2 = Line("black", "wood", line2Coordinates, 10)
     square1 = Square("red" ,"plastic" , square1Coordinates, 5)
     square2 = Square("red", "plastic", square2Coordinates, 5)

     print(f"\n{str(line1)}")
     print(f"\n{str(line2)}")
     print(f"\nCompare:\t{compare(line1, line2)}")

     print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
     print(f"\n{str(square1)}")
     print(f"\n{str(square2)}")
     print(f"\nCompare:\t{compare(square1, square2)}")

     print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
     print(f"\n{str(line1)}")
     print(f"\n{str(square1)}")
     print(f"\nCompare:\t{compare(line1, square1)}")