
# this program draws a square of side 100

#import turtle
import turtle

# get number of sides of polygon
# draw a line of length 100
# then turn left thru 90 degrees
# repeat this process 4 times to
# draw the four sides of the square
side_num = int(input("How many sides does the polygon have? "))

for i in range(side_num):
    turtle.forward(100)
    turtle.left(360/side_num)
#end of for loop
