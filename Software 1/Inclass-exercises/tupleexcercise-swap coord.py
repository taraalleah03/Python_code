import math

def calculate_distance(point1, point2):
    (x1,y1) = point1
    (y2,x2) = point2
    c = math.sqrt((x2-x1)**2 + (y2-y1)**2)
    return c

def swap_coordinates(point):
    #unpack the point
    (x,y) = point
    return y,x

point = (int(input("Give x coordinate: "))), int(input("Give y coordinate: "))
print(swap_coordinates(point))
print("The distance between two points is", round(calculate_distance(point, point),2))



