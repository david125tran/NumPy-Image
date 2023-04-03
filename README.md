# NumPy-Image
  
A very short and simple script using NumPy.
  
This converts a colored image to black and white.  
  
The background color of images consists of three-integer color tuples of an RGB (Red, Green, Blue) value.  The NumPy library for Python programming language is used to perform a wide variety of mathematical operations on arrays.  Here I extract the color tuple value of the colored image into an array using the NumPy library.  I do a simple matrix multiplication on the arrays using the ampersand operatior, "@" to convert the tuple values into gray scale tuple values.  Alternatively, I could have used the numpy.multiply() function.    

I then use the matplotlib library to show the image converted to black and white.  
  
Some Basic Colors:
Color	(Red, Green, Blue) value  
Black	(0,0,0)  
Red	(255,0,0)  
Green	(0,255,0)  
Blue	(0,0,255)  
White	(255,255,255)  
Light Gray	(122,122,122)  
