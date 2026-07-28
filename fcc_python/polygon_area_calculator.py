class Rectangle:
    """Rectangle class to find the area, perimeter and diagonal of a rectangle."""
    def __init__(self,width,height):
        self.width = width
        self.height = height

    def set_width(self,new_width):
        """Sets the new width to the attribute."""
        self.width = new_width      

    def set_height(self,new_height):
        """Sets the new height to the attribute."""
        self.height = new_height

    def get_area(self):
        """Calculates the area of the rectangle."""

        return self.width * self.height

    def get_perimeter(self):
        """Calculates the perimeter of the rectangle."""
        return 2 * (self.width + self.height)

    def get_diagonal(self):
        """Calculates the diagonla of the rectangle."""
        return (self.width ** 2 + self.height ** 2) ** 0.5

    def get_picture(self):
        """Shows the rectangle in a * pattern."""
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
            
        return ("*" * self.width + "\n") * self.height

    def get_amount_inside(self,obj):
        """Calculates the number of shapes that are perfectly fit into the rectangle."""
        return (self.height//obj.height) * (self.width // obj.width)
        

    def __str__(self):
        """A string representation of the rectangle."""
        return f"Rectangle(width={self.width}, height={self.height})"


class Square(Rectangle):
    """Square class that inherits the rectangle class."""
    
    def __init__(self,side):
        super().__init__(side,side)

    def set_side(self,new_side):
        """Sets the height and width of the Rectangle class to same value."""
        self.height = new_side
        self.width = new_side

    def set_width(self,new_width):
        """Changes the side of the square."""
        self.set_side(new_width)

    def set_height(self,new_height):
        """Changes the side of the square."""
        self.set_side(new_height)


    def __str__(self):
        """String representation of the Square object."""
        return f"Square(side={self.height})"