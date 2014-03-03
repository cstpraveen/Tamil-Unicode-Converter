#!/usr/bin/env python
import sys
import pygtk
import gtk
TextBox = gtk.TextView()
MenuBar = gtk.MenuBar()
StatusBar = gtk.Statusbar()
Window = gtk.Window(gtk.WINDOW_TOPLEVEL)
class MainForm:
	_File = ""
	def open_file(menuitem, user_param1):
		chooser = gtk.FileChooserDialog(title="Open a file",action=gtk.FILE_CHOOSER_ACTION_OPEN, buttons=(gtk.STOCK_CANCEL,gtk.RESPONSE_CANCEL,gtk.STOCK_OPEN,gtk.RESPONSE_OK))
		chooser.set_default_response(gtk.RESPONSE_OK)
		filter = gtk.FileFilter()
		filter.set_name("Text Files")
		filter.add_mime_type("text/data")
		filter.add_pattern("*.txt")
		chooser.add_filter(filter)
		filter2 = gtk.FileFilter()
		filter2.set_name("All Files")
		filter2.add_pattern("*.*")
		chooser.add_filter(filter2)
		response = chooser.run()
		if response == gtk.RESPONSE_OK:
			global _File
			filename = chooser.get_filename()
			_File = filename
			textbuffer = TextBox.get_buffer()
			print "Opened File: " + filename
			StatusBar.push(0,"Opened File: " + filename)
			index = filename.replace("\\","/").rfind("/") + 1
			window.set_title(filename[index:] + " - PyPad")
			file = open(filename, "r")
			text = file.read()
			textbuffer.set_text(text)
			file.close()
		elif response == gtk.RESPONSE_CANCEL:
			chooser.destroy()
			chooser.destroy()
	def save_file_as(menuitem,user_param):
		chooser = gtk.FileChooserDialog(title="Save file",action=gtk.FILE_CHOOSER_ACTION_SAVE, buttons=(gtk.STOCK_CANCEL,gtk.RESPONSE_CANCEL,gtk.STOCK_SAVE,gtk.RESPONSE_OK))
		chooser.set_default_response(gtk.RESPONSE_OK)
		filter = gtk.FileFilter()
		filter.set_name("Text Files")
		filter.add_mime_type("text/data")
		filter.add_pattern("*.txt")
		chooser.add_filter(filter)
		filter2 = gtk.FileFilter()
		filter2.set_name("All Files")
		filter2.add_pattern("*.*")
		chooser.add_filter(filter2)
		response = chooser.run()
		if response == gtk.RESPONSE_OK:
			global _File
			filename = chooser.get_filename()
			_File = filename
			textbuffer = TextBox.get_buffer()
			print "Saved File: " + filename
			StatusBar.push(0,"Saved File: " + filename)
			index = filename.replace("\\","/").rfind("/") + 1
			text = textbuffer.get_text(textbuffer.get_start_iter() , textbuffer.get_end_iter())
			window.set_title(filename[index:] + " - PyPad")
			file = open(filename, "w")
			file.write(text)
			file.close()
		elif response == gtk.RESPONSE_CANCEL:
			chooser.destroy()
			chooser.destroy()
	def reset_new(menuitem,user_param):
		_File = ""
		print "PyPad has been reset!"
		Window.set_title("Untitled - PyPad")
		textbuffer = TextBox.get_buffer()
		textbuffer.set_text("")
	def save_file(menuitem,user_param):
		if _File is not "":
			textbuffer = TextBox.get_buffer()
			print "Saved File: " + _File
			StatusBar.push(0,"Saved File: " + filename)
			index = filename.replace("\\","/").rfind("/") + 1
			text = textbuffer.get_text(textbuffer.get_start_iter() , textbuffer.get_end_iter())
			Window.set_title(_File[index:] + " - PyPad")
			file = open(_File, "r+")
			file.write(text)
			file.close()
	def __init__(self):
		Window.set_title("Untitled - PyPad")
		Window.set_default_size(750,450)
		Window.connect('destroy', gtk.main_quit)
		TextBox.set_wrap_mode(gtk.WRAP_WORD)
		TextBox.set_editable(True)
		TextBox.set_cursor_visible(True)	
		TextBox.set_border_window_size(gtk.TEXT_WINDOW_LEFT,1)
		TextBox.set_border_window_size(gtk.TEXT_WINDOW_RIGHT,1)
		TextBox.set_border_window_size(gtk.TEXT_WINDOW_TOP,1)
		TextBox.set_border_window_size(gtk.TEXT_WINDOW_BOTTOM,1)
		vbox = gtk.VBox(False,0)
		box1 = gtk.VBox(False, 10)
		box2 = gtk.VBox(False, 20)
		box3 = gtk.VBox(False, 70)
		vbox.pack_start(box2, False, False, 0)
		vbox.pack_start(box1, True, True, 0)
		vbox.pack_start(box3, False, False, 0)
		sw = gtk.ScrolledWindow()
		sw.set_policy(gtk.POLICY_AUTOMATIC, gtk.POLICY_AUTOMATIC)
		sw.add(TextBox)
		box1.pack_start(sw)
		box2.pack_start(MenuBar, True, False, 0)
		box3.pack_start(StatusBar, True, False, 0)
		filemenu = gtk.Menu()
		filem = gtk.MenuItem("File")
		newm = gtk.MenuItem("New")
		openm = gtk.MenuItem("Open")
		savem = gtk.MenuItem("Save")
		saveasm = gtk.MenuItem("Save As")
		openm.connect("activate",self.open_file)
		saveasm.connect("activate",self.save_file_as)
		newm.connect("activate",self.reset_new)
		savem.connect("activate",self.save_file)
		filemenu.append(newm)
		filemenu.append(openm)
		filemenu.append(savem)
		filemenu.append(saveasm)
		filem.set_submenu(filemenu)
		MenuBar.append(filem)
		Window.add(vbox)
		Window.show_all()
def main():
	gtk.gdk.threads_enter()
	gtk.main()
	gtk.gdk.threads_leave() 
	
if __name__ == "__main__":
	Initialize = MainForm()
	main()
