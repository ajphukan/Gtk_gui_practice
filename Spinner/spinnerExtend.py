import gi 
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, GObject

class SpinnerWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Spinner Demo")
        self.set_border_width(10)

        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(vbox)

        self.spinner = Gtk.Spinner()
        vbox.pack_start(self.spinner, True, True, 0)

        self.label = Gtk.Label()
        vbox.pack_start(self.label, True, True, 0)

        self.entry = Gtk.Entry()
        self.entry.set_text("10")
        vbox.pack_start(self.entry, True, True, 0)

        self.buttonStart = Gtk.Button(label="Start timer")
        self.buttonStart.connect("clicked", self.on_buttonStart_clicked)
        vbox.pack_start(self.buttonStart, True, True, 0)

        self.buttonStop = Gtk.Button(label="Stop timer")
        self.buttonStop.connect("clicked", self.on_buttonStop_clicked)
        vbox.pack_start(self.buttonStop, True, True, 0)

        self.timeout_id = None
        self.connect("destroy", self.on_SpinnerWindow_destroy)


    def on_buttonStart_clicked(self, widget):
        self.start_timer()
    
    def on_buttonStop_clicked(self, widget):
        self.stop_timer("Stopped from button")

    def on_SpinnerWindow_destroy(self, widget):
        # ensure the timeout function is stopped
        if self.timeout_id:
            GObject.source_remove(self.timeout_id)
            self.timeout_id = None
        Gtk.main_quit()

    def on_timeout(self, user_data):
        """ A timeout function.

        Return True to stop it.
        This is not a precise timer since next timeout
        is recalculated based on the current time."""

        self.counter -=1
        if self.counter <= 0:
            self.stop_timer("Reached time out")
            return False
        self.label.set_label("Remaining: " + str(int(self.counter / 4)))
        return True

    def start_timer(self):
        """ Start the timer """
        self.buttonStart.set_sensitive(False)
        self.buttonStop.set_sensitive(True)

        # time out will check every 250 miliseconds (1/4 of a second)
        self.counter = 4 * int(self.entry.get_text())
        self.label.set_label("Remaining: " + str(int(self.counter / 4)))
        self.spinner.start()
        self.timeout_id = GObject.timeout_add(250, self.on_timeout, None)

    def stop_timer(self, msg):
        """ Stop the timer """
        if self.timeout_id:
            GObject.source_remove(self.timeout_id)
            self.timeout_id = None

        self.spinner.stop()
        self.buttonStart.set_sensitive(True)
        self.buttonStop.set_sensitive(False)
        self.label.set_label(msg)


win = SpinnerWindow()
win.show_all()
Gtk.main()
        





