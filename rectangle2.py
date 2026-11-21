class rectangle2:
    def __init__(self, length, breadth):
        self.__length = length
        self.__breadth = breadth

    def area(self):
        return self.__length * self.__breadth

    def __lt__(self, other):
        return self.area() < other.area()


l1 = int(input("Enter length of rectangle 1: "))
b1 = int(input("Enter breadth of rectangle 1: "))

l2 = int(input("Enter length of rectangle 2: "))
b2 = int(input("Enter breadth of rectangle 2: "))

r1 = rectangle2(l1, b1)
r2 = rectangle2(l2, b2)

if r1 < r2:
    print("Rectangle 1 has smaller area")
elif r2 < r1:
    print("Rectangle 2 has smaller area")
else:
    print("Both have equal area")
