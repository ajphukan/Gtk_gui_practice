import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class SpinnerAnimation(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Spinner")
        self.set_border_width(3)
        
        table = Gtk.Table(3, 2, True)

        button = Gtk.ToggleButton(label="Start Spinning")
        button.connect("toggled", self.on_button_toggled)
        button.set_active(False)
        table.attach(button, 0, 2, 0, 1)

        self.spinner = Gtk.Spinner()
        table.attach(self.spinner, 0, 2, 2, 3)

        self.add(table)

    def on_button_toggled(self, button):
        if button.get_active():
            self.spinner.start()
            button.set_label("Stop Spinning")
        else:
            self.spinner.stop()
            button.set_label("Start Spinning")        

win = SpinnerAnimation()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
    