import gi
gi.require_version('AppIndicator3', '0.1')
gi.require_version('Gtk', '3.0')

import threading
import subprocess

from gi.repository import Gtk
from gi.repository import AppIndicator3 as appindicator
from gi.repository import GLib

class PanelIndicator:
    def __init__(self, update_interval):

        self.ind = appindicator.Indicator.new(
                    "AppIndicator",
                    "go-down-symbolic",
                    appindicator.IndicatorCategory.APPLICATION_STATUS)
        self.ind.set_status (appindicator.IndicatorStatus.ACTIVE)

        self.menu = Gtk.Menu()
        #
        item = Gtk.MenuItem()
        item.set_label("Exit")
        item.connect("activate", self.quit)
        self.menu.append(item)
        #
        self.menu.show_all()
        self.ind.set_menu(self.menu)

        self.update_interval = update_interval

        self.main()

    """ get the output of any script file inside python scripts """
    def bash_script_runner(self, script_file):
        out, err = subprocess.Popen(["bash", script_file], stdout=subprocess.PIPE).communicate()
        return (out, err)

    def set_value(self, val):
        self.ind.set_label(val, "")
        self.ind.set_status(appindicator.IndicatorStatus.ATTENTION)

    def set_new_value(self):
        """runs periodically"""
        pass

    def update_value(self):
        val = self.set_new_value()
        self.set_value(val)
        return True

    def f1(self):
        """ runs once"""
        GLib.timeout_add_seconds(self.update_interval, self.update_value)

    def main(self):
        threading.Thread(target=self.f1).start()
        Gtk.main()

    def quit(self, widget):
        Gtk.main_quit()
