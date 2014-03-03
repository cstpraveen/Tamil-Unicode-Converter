#!/usr/bin/env python

import pygtk
pygtk.require('2.0')
import gtk

TextBox = gtk.TextView()

class Base:
    def destroy(self, widget, data=None):
        gtk.main_quit()

    def __init__(self):
        #create a new Window

       	self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.set_position(gtk.WIN_POS_CENTER)
        self.window.set_size_request(800,600)
        self.window.connect("destroy", self.destroy)
        self.window.set_title("Tamil Unicode Converter")

        TextBox.set_wrap_mode(gtk.WRAP_WORD)
        TextBox.set_editable(True)
        TextBox.set_cursor_visible(True)	
        TextBox.set_border_window_size(gtk.TEXT_WINDOW_LEFT,2)
        TextBox.set_border_window_size(gtk.TEXT_WINDOW_RIGHT,2)
        TextBox.set_border_window_size(gtk.TEXT_WINDOW_TOP,2)
        TextBox.set_border_window_size(gtk.TEXT_WINDOW_BOTTOM,2)

        self.box1=gtk.HBox()
        self.box1.pack_start(TextBox)
        self.window.add(self.box1)
        self.window.show_all()

    def main(self):
        gtk.main()

if __name__=="__main__":
    base=Base()
    base.main()
