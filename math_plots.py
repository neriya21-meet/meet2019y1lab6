Python 3.6.8 (default, Jan 14 2019, 11:02:34) 
[GCC 8.0.1 20180414 (experimental) [trunk revision 259383]] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
import turtle

x = 0
while x<300:
   y = x**2/300 #x**2 is the same as x*x
   turtle.goto(x, y)
   x = x + 1

turtle.mainloop()
