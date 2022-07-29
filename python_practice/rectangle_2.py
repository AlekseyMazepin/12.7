from python_practice.rectangle import Rectangle, Square, Circle

rect_1 = Rectangle(3, 4)
rect_2 = Rectangle(12, 5)

print(rect_1.get_area())
print(rect_2.get_area())

square_1 = Square(5)
square_2 = Square(10)

print(square_1.get_area_square(), square_2.get_area_square())

circle_1 = Circle(10)
circle_2 = Circle(15)

print("Площадь круга 1:=%.2f" % (circle_1.get_area_circle()), "Площадь круга 2:=%.3f" % (circle_2.get_area_circle()))

figures = [rect_1, rect_2, square_1, square_2, circle_1, circle_2]
for figure in figures:
        if isinstance(figure,Square):
            print(figure.get_area_square())
        elif isinstance(figure, Rectangle):
            print(figure.get_area())
        else:
            print("Площадь круга:=%.2f" % (figure.get_area_circle()))