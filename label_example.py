import gi
gi.require_version('Gtk','3.0')
from gi.repository import Gtk

win = Gtk.Window(title="Label Example")
win.connect('destroy', Gtk.main_quit)

# label getter setter 
# label = Gtk.Label(label="Hello World", angle=25, halign=Gtk.Align.END)
label = Gtk.Label()
label.set_label("Hello World")
label.set_angle(25)
label.set_halign(Gtk.Align.END)


#win.show_all()
win.add(label)
# YOU HAVE TO CALL SHOW_All WHENEVER YOU DYNAMICALY ADD NEW OBJECT AFTER THE FIRST show_all 
# oR JUST DO ALL THE CHANGES AND THEN CALL ONLY ONCE show_all
win.show_all()
Gtk.main()