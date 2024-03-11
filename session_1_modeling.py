# # object-oriented programming (OOP)
# # data science, regressions, time series, applicable coding.
# # OOP: different way of looking at programming.
# # Programming paradigm: a philosophy or style of programming.
# # We map real life situations into programming language.
# # we use objects to model our problem and solve it.
# # We structure programs in a way such as properties bundled together in an object.
# # car: wheels, engines, doors, windows...
# # we model these objects in as objects which have data and methods (functions) they can perform.
#
# # class: a blueprint for creating objects.
# # Everything in python is an object
#
#     # each object has:
#         # a type
#         # an internal data representation
#         # a set of procedures for interacting with the object.
#
# # def defines a function, class defines and object / class
# # capitalize the first letter of the class name for convention to distinguish it from a function.
# # action of using a class after its defined: creating an instance of the class.
# #
# class Point:
#     def __init__(self, x, y):
#         """""""" # init method that initializes the point with x and y
#         self.x = x
#         self.y = y
#     def __str__(self): #print this point with return
#         return (f"<{self.x}, {self.y}>")
#
# #
# # a = Point(2, 3) # A is an instance of the class Point
# #
# # print(a.x) # 2
# # print(a.y) # 3
# #
# # # Almost all classes must have an __init__ method. This method is used to initialize the object's state.
# # # Each point must have two attributes (coordinates) x and y.
# #
# # # we call the name of the class with uppercase, instances with lowercase a instead of mathematical A, etc...
# # b = Point(7, 9) # B is an instance of the class Point
# # print(b.x, b.y) # 7 9
# #
# # # every point that has x and y given, is an instance of the class Point.
# # # the class is a constructor that allows us to create instances of the class.
# # # an instance could be a black bwm, and a red tesla... it's a particular version of that class.
# #
# # #Create a for loop and add 5 random points into a list
# # #
# import random
# # #
# points = []
# # # # for _ in range(5):
# # # #     x = random.randint(1, 100)
# # # #     y = random.randint(1, 100)
# # # #     points.append(Point(x, y))
# # # #
# # # # print(Points)
#
# for _ in range(5):
#     points.append(Point(random.randint(0, 100), random.randint(0, 100)))
#
# for point in points:
#     print(point) # this gives you the ID of the object in memory
# #     print(point.x, point.y) # this gives you the x and y coordinates of the point
# #
# # # we need to instruct python on how to print the points of an object
#


#FINAL CODE
import random

points = []
class Point:
    def __init__(self, x, y):
        """""""" # init method that initializes the point with x and y
        self.x = x
        self.y = y
    def __str__(self): #print this point with return
        return (f"<{self.x}, {self.y}>")

#################### how to print in a list

    def __repr__(self):
        return self.__str__()  # or f"<{self.x}, {self.y}>"


########################################################

for _ in range(5):
    points.append(Point(random.randint(0, 100), random.randint(0, 100)))

for point in points:
    print(point)

print(points) # this gives you the ID of the object in memory, doesn't work for obtaining numbers
# it iterates and calls point.repr for each point in the list.