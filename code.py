'''

hopefully a working (very) basic text editor

'''

import sys
from tkinter import *
import tkinter.filedialog
from tkinter import messagebox

savelocation = ''

def saveas():
	global text
	global savelocation
	t = text.get('1.0','end-1c')
	savelocation = tkinter.filedialog.asksaveasfilename(defaultextension='.txt')
	f = open(savelocation, 'w+')
	f.write(t)
	f.close()

def openfile():
	global text
	global savelocation
	savelocation = tkinter.filedialog.askopenfile(title='Open file',defaultextension='.txt')
	t = savelocation.read()
	text.delete('1.0','end')
	text.insert(END,t)
	savelocation.close()
	
def savefile():
	global text
	global savelocation
	
	
	if savelocation:
		t = text.get('1.0','end-1c')
		save_text = open(savelocation.name, 'w+')
		save_text.write(t)
		save_text.close()

	else:
		messagebox.showinfo("Error - Filename", "Filename not set, use SaveAs")

def frame(root):
	frame = Frame(root)
	frame.pack()
	menubar = Menu(root)
	filemenu = Menu(menubar, tearoff = 0)
	filemenu.add_command(label='Open', command=openfile)
	filemenu.add_command(label='Save', command=savefile)
	filemenu.add_command(label='SaveAs', command=saveas)
	filemenu.add_command(label='Quit', command=root.quit)
	menubar.add_cascade(label='File', menu=filemenu)
	root.config(menu = menubar)


root = Tk('Text Editor')
root.title('SR Text Editor')
frame(root)
text = Text(root)
text.pack(side='left', expand = True, fill = 'both')
scroll_y = Scrollbar(root, orient="vertical", command=text.yview)
scroll_y.pack(side="right", fill="y")
text.config(yscrollcommand=scroll_y.set)



root.mainloop()
root.destroy()
