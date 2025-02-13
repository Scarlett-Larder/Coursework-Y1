from Term_2.graphix import Window, Point, Circle

win = Window()

#p = Point(10, 20)
#p.draw(win)

c = Circle(Point(20, 100), 50)

c.draw(win)
c.outline_colour = "blue"
c.fill_colour = "red"
c.outline_colour = 'blue'


