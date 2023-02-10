import sys
from math import atan2

class Polygon: 
    def __init__(self):
        self.__field = None
        self.__area = None
    def polygon_area(self):
        x = []
        y = []
        for line in self.__field:
            numbers = line.strip()
            coordinates = numbers.split(",")
            print(coordinates)          
            x.append(float(coordinates[0]))
            y.append(float(coordinates[1]))
        area = 0
        for i in range(len(self.__field)):
            if (i+1) == len(self.__field):
                area += (x[i]*(y[0]-y[i-1]))/2
            else:
                area += (x[i]*(y[i+1]-y[i-1]))/2
        self.__total_area = abs(area)
    def sort_clockwise(self):
        if self.__field == None:
            sys.exit ("There is no data")
        x = 0
        y = 0
        for coordinate in self.__field:
            coordinates = coordinate.split(",")
            x += float(coordinates[0])
            y += float(coordinates[1])
        centroid = (x//len(self.__field), y//len(self.__field))
        angle = []
        for coordinate in self.__field:
            coordinates = coordinate.split(",")
            angle.append(atan2(float(coordinates[1])-centroid[1],float(coordinates[0])-centroid[0]))
        for idx_1 in range(len(angle)):
            for idx_2 in range(idx_1,len(angle)):
                if angle[idx_1] < angle[idx_2]:
                    tmp = angle[idx_1]
                    angle[idx_1] = angle[idx_2]
                    angle[idx_2] = tmp
                    tmp = self.__field[idx_1]
                    self.__field[idx_1] = self.__field[idx_2]
                    self.__field[idx_2] = tmp
        print(angle)
        print(coordinates)
    def load(self,adress):
        try:
            with open (adress, 'r', encoding = "utf-8") as input:
                self.__field = input.readlines()
        except FileNotFoundError:
            sys.exit ("The file has not been found.")
        except PermissionError:
            sys.exit ("You don't have the permission to open this file.")
        except IOError:
            sys.exit ("An error occured while opening the input file.")
        except KeyError:
            sys.exit ("An error occured while reading the input file.")
        except:
            sys.exit ("Something went wrong.")
    def print(self):
        print(f"The area of the polygon is {self.__total_area}")

def main():
    object = Polygon()
    object.load("input.txt")
    object.sort_clockwise()
    object.polygon_area()
    object.print()

main()
