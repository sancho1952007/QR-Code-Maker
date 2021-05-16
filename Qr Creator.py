import pyqrcode as py
from tkinter import *
import png
import pyautogui as p
import pyperclip as pyc
from tkinter.filedialog import *
from tkinter.scrolledtext import *
from tkinter.messagebox import *
root=Tk()
root.title("Qr Code Maker")
root.resizable(False, False)

#Functions
def new():
   sure_new=askyesno("Clear?", "Are you sure to clear the all text?")
   if sure_new:
    main.delete(1.0, END)

def selall():
    p.hotkey("ctrl", "a")

def paste():
   main.insert(1.0, pyc.paste())

def gen():
 qr=py.create(main.get(1.0, END))
 save_sure=asksaveasfilename(title="Save Qr Code As", filetypes=[("Image Files", '*.png')])
 if save_sure:
  try: 
   if save_sure.endswith(".png"):
     qr.png(save_sure, scale=8)
     showinfo("Success", "Qr Code Successfully Made!")

   else:
      qr.png(save_sure+".png")
      showinfo("Success", "Qr Code Successfully Made!")
  except:
    showerror("Error!", "Coudn't Make Qr Code!")

def copy_all():
   pyc.copy(main.get(1.0, END))

def rclick(event):
    try:
        rc.tk_popup(event.x_root, event.y_root)

    finally:
        rc.grab_release()

#Menu
menu=Menu(root)
File=Menu(menu, tearoff=0)
menu.add_cascade(label="File", menu=File)
File.add_command(label="New", command=new)

Edit=Menu(menu, tearoff=0)
menu.add_cascade(label="Edit", menu=Edit)
Edit.add_command(label="Copy", command=copy_all)
Edit.add_command(label="Paste", command=paste)

menu.add_cascade(label="Generate", command=gen)


rc=Menu(root, tearoff=0)
rc.add_command(label="Select All", command=selall)

#Code
main=ScrolledText()
main.grid()

#Right Click
main.bind("<Button-3>", rclick)

#Root
root.config(menu=menu)
root.mainloop()
