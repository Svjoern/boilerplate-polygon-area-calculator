class Rectangle:
  def __init__(self, width, height):
    self.width = width
    self.height = height

  def set_width(self, width):
    self.width = width

  def set_height(self, height):
    self.height = height

  def get_area(self):
    return self.width * self.height

  def get_perimeter(self):
    return 2 * self.width + 2 * self.height

  def get_diagonal(self):
    return (self.width ** 2 + self.height ** 2) ** .5

  def get_picture(self):
    if self.width > 50 or self.height > 50:
     return "Too big for picture."
    else:
      t_str = ""
      for j in range(self.height):
        for i in range(self.width):
          t_str += "*"
        t_str += "\n"
      return t_str

  def get_amount_inside(self, object):
    return int(self.get_area()/object.get_area())
    
  def __str__(self):
    return "Rectangle(width="+str(self.width)+", height="+str(self.height)+")";
  

class Square(Rectangle):
  def __init__(self, side):
    self.set_side(side)

  def set_side(self, side):
    self.width = side
    self.height = side
   
  def set_width(self, side):
    self.set_side(side)

  def set_height(self, side):
    self.set_side(side)

  def __str__(self):
    return "Square(side="+str(self.width)+")";

