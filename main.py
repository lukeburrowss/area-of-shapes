'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
def circle_area(radius):
  pi = 3.14
  area = pi * (radius ** 2)
  circumference = 2 * pi * radius
  print("The area of the circle is " + str(area))
  print("The circumference of the circle is " + str(circumference))
circle_area(0.5) 

def rectangle_area(base, height):
	area = base*height
	print("The area of the rectangle is " + str(area))
	
rectangle_area(5, 5)

def triangle_area(base, height):
  area = base / 2 * height
  print("The area of the triangle is " + str(area))
  
triangle_area(10, 12)

def square_area(length):
  area = length ** 2
  print("The area of the square is " + str(area))
  
square_area(10)

def parallelogram_area(base, height):
    area = base * height
    print("The area of the parallelogram is " + str(area))
    
parallelogram_area(5, 5)

def trapezoid_area(base1, base2, height):
  area = base1 + base2 / 2 * height
  print("The area of the trapezoid is " + str(area)) 
  
trapezoid_area(5, 10, 2)
  




    
