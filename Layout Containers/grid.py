# Gtk.Grid is a container which arranges its child widgets in rows and columns, but you do not need to specify the dimensions in the constructor. Children are added using Gtk.Grid.attach(). They can span multiple rows or columns. The Gtk.Grid.attach() method takes five parameters:

#     The child parameter is the Gtk.Widget to add.
#     left is the column number to attach the left side of child to.
#     top indicates the row number to attach the top side of child to.
#     width and height indicate the number of columns that the child will span, and the number of rows that the child will span, respectively.

# It is also possible to add a child next to an existing child, using Gtk.Grid.attach_next_to(), which also takes five parameters:

#     child is the Gtk.Widget to add, as above.
#     sibling is an existing child widget of self (a Gtk.Grid instance) or None. The child widget will be placed next to sibling, or if sibling is None, at the beginning or end of the grid.
#     side is a Gtk.PositionType indicating the side of sibling that child is positioned next to.
#     width and height indicate the number of columns and rows the child widget will span, respectively.

# Finally, Gtk.Grid can be used like a Gtk.Box by just using Gtk.Grid.add(), which will place children next to each other in the direction determined by the “orientation” property (defaults to Gtk.Orientation.HORIZONTAL).



import gi
gi.require_version("Gtk","3.0")
from gi.repository import Gtk

class GridWindow(Gtk.Window):
    

    def __init__(self):
        Gtk.Window.__init__(self, title="Grid Layout Example")

        grid = Gtk.Grid()
        self.add(grid)

        button1 = Gtk.Button(label="Button 1")
        button2 = Gtk.Button(label="Button 2")
        button3 = Gtk.Button(label="Button 3")
        button4 = Gtk.Button(label="Button 4")
        button5 = Gtk.Button(label="Button 5")
        button6 = Gtk.Button(label="Button 6")

        grid.add(button1)
        grid.attach(button2, 1 , 0, 2, 1)
        grid.attach_next_to(button3, button1, Gtk.PositionType.BOTTOM, 1, 2)
        grid.attach_next_to(button4, button3, Gtk.PositionType.RIGHT, 2, 1)
        grid.attach(button5, 1, 2, 1, 1)
        grid.attach_next_to(button6, button5, Gtk.PositionType.RIGHT, 1, 1)


win = GridWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
        