#!/usr/bin/env python
# Author: Hector Garcia Huerta <lliurex_devel1@edu.gva.es>
# Licensed under GPL v3 or higher

# -*- coding: utf8 -*-

import threading
import polib
import potools
import sys
import signal
from gi.repository import Gtk, Gdk,GObject

signal.signal(signal.SIGINT, signal.SIG_DFL)


class Troba:

	def __init__(self):

		self.load_gui()


	#def init

	def load_po(self,f):
		print("[Troba] Loading po...")
		def load_po_t(f):
			try:
				self.memoria=polib.pofile(f)
				self.memoria_dic={}
				for entry in self.memoria:
					self.memoria_dic[entry.msgid]=(entry.msgstr,entry.occurrences)
				self.search_entry.set_sensitive(True)
				self.msg_label.set_text("PO file loaded")
				self.spinner.hide()
				

			except Exception as e:
				pass
			
		self.pothread=threading.Thread(target=load_po_t,args=(f,))
		self.pothread.daemon=True
		self.pothread.start()

	#def load_po

	def load_gui(self):

		builder = Gtk.Builder()
		builder.add_from_file("window.glade")
		self.window=builder.get_object("window")
		self.window.connect("destroy",self.close_window)
		self.search_entry=builder.get_object("searchEntry")
		self.search_entry.set_sensitive(False)
		self.main_vbox=builder.get_object("mainVBox")
		#self.result_treeview=builder.get_object("resultTreeview")

		self.liststore = Gtk.ListStore(str,str,str)
		self.liststore.append(["test","prueba","tooltip"])
		self.result_treeview=Gtk.TreeView(self.liststore)
		self.result_treeview.set_enable_tree_lines(True)
		self.result_treeview.set_rubber_banding(True)
		self.result_treeview.set_rules_hint(True)
		self.result_treeview.connect("query-tooltip",self.tooltip_query)

		self.scrolled_window=Gtk.ScrolledWindow()
		self.scrolled_window.add(self.result_treeview)
		self.main_vbox.pack_start(self.scrolled_window,True,True,0)
		msgid_rend = Gtk.CellRendererText()
		msgid_rend.props.wrap_width = 400
		msgid_rend.props.wrap_mode = Gtk.WrapMode.WORD
		msgid_col = Gtk.TreeViewColumn("Original message")
		msgid_col.pack_start(msgid_rend, True)
		msgid_col.add_attribute(msgid_rend,"text",0)
		self.result_treeview.append_column(msgid_col)
		

		msgtr_rend = Gtk.CellRendererText()
		msgtr_rend.props.wrap_width = 800
		msgtr_rend.props.editable=True
		msgtr_rend.props.wrap_mode = Gtk.WrapMode.WORD

		msgtr_col = Gtk.TreeViewColumn("Translation")

		msgtr_col.pack_start(msgtr_rend, True)
		msgtr_col.add_attribute(msgtr_rend,"text",1)
		self.result_treeview.append_column(msgtr_col)
		self.result_treeview.set_has_tooltip(True)
		self.result_treeview.set_tooltip_column(2)

		self.msg_label=builder.get_object("msgLabel")
		self.search_entry=builder.get_object("searchEntry")
		#self.search_entry.connect("changed",self.entry_changed)
		self.search_entry.connect("activate",self.entry_return)

		self.option_combobox=builder.get_object("optionCombobox")
		combo_store=Gtk.ListStore(str)
		combo_store.append(["Original message"])
		combo_store.append(["Translation"])
		self.option_combobox.set_model(combo_store)
		combo_rend=Gtk.CellRendererText()
		self.option_combobox.pack_start(combo_rend,True)
		self.option_combobox.add_attribute(combo_rend,"text",0)
		self.option_combobox.set_active(0)
		self.option_combobox.connect("changed",self.combobox_changed)

		self.spinner=builder.get_object("spinner")
		self.spinner.start()

		self.window.show_all()
		self.load_po("/svn/polin/llx1306/llx-l10n/workspace/poto.po")
		Gtk.main()

	#def load_gui


	def entry_return(self,widget):

		self.populate_treeview(self.search_entry.get_text())

	#def entry_return
	def combobox_changed(self,combobox):

		if len(self.search_entry.get_text())>3:
			self.populate_treeview(self.search_entry.get_text())

	#def combobox_changed

	def close_window(self,widget):

		Gtk.main_quit()
		sys.exit(0)

	#def close_window

	def tooltip_query(self,treeview,x,y,mode,tooltip):
		path=treeview.get_path_at_pos(x,y)

		if path:
			treepath,column=path[:2]
			model=treeview.get_model()
			iterator=model.get_iter(treepath)
			tooltip.set_text(model[iterator][2])

		return False

	def populate_treeview(self,text):
		if type(text)==type(""):
			text=unicode(text,"utf-8")
		self.liststore.clear()
		if text.find("*")!=-1:
			text=text.replace("*","")
			for key in self.memoria_dic:
				if self.option_combobox.get_active()==0:
					text_to_find=key
				else:
					text_to_find=self.memoria_dic[key][0]
				if text_to_find.find(text)!=-1:
					try:
						tooltip=" ".join(list(self.memoria_dic[key][1][0]))
					except:
						tooltip=""
					self.liststore.append([key,self.memoria_dic[key][0],tooltip])
			
		else:
			

			for key in self.memoria_dic:
				if self.option_combobox.get_active()==0:
					text_to_find=key
				else:
					
					text_to_find=self.memoria_dic[key][0]
				if text_to_find==text:
					try:
						tooltip=" ".join(list(self.memoria_dic[key][1][0]))
					except:
						tooltip=""
					self.liststore.append([key,self.memoria_dic[key][0],tooltip])

	#def populate_treeview

	def entry_changed(self,entry):
		if len(entry.get_text())>3:
			self.populate_treeview(entry.get_text())
		#print self.search_entry.get_text()
	#def entry_changed
		


	#def entry_changed


#class Troba

if __name__=="__main__":
	GObject.threads_init()
	t=Troba()
	GObject.threads_leave()
	#print "waiting..."
	sys.exit(0)

#memoria = polib.pofile("/svn/polin/llx1306/llx-l10n/workspace/poto.po")







