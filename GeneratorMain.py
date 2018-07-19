from tkinter import *
from tkinter import ttk

from tkinter import messagebox as mb
from tkinter import filedialog
from pathlib import Path
import zipfile
root = Tk()
mainmenu = Menu(root)
root.config(menu=mainmenu)

filemenu = Menu(mainmenu, tearoff=0)
filemenu.add_command(label="Открыть...")
filemenu.add_command(label="Новый")
filemenu.add_command(label="Сохранить...")
filemenu.add_command(label="Выход")

bazamenu = Menu(mainmenu, tearoff=0)
bazamenu.add_command(label="Помощь")
bazamenu.add_command(label="О программе")

helpmenu = Menu(mainmenu, tearoff=0)
helpmenu.add_command(label="Помощь")
helpmenu.add_command(label="О программе")

mainmenu.add_cascade(label="Настройки", menu=filemenu)
mainmenu.add_cascade(label="База реестров", menu=bazamenu)
mainmenu.add_cascade(label="Справка", menu=helpmenu)
root.title("Генератор номеров реестров в банки ")
x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 3
y = (root.winfo_screenheight() - root.winfo_reqheight()) / 3
root.wm_geometry("+%d+%d" % (x, y))

label1 = Label(root, text='Номер реестра', justify=RIGHT, font='Times 20', fg='#004C00')
label2 = Label(root, text='МСП', justify=RIGHT)
label3 = Label(root, text='Банк', justify=RIGHT)
entry1 = Entry(root, width=20,font='Times 20')
label4 = Label(root, text='Путь на файл', justify=RIGHT)
entry2 = Entry(root, width=50)
list1 = ["Один","Два","Три"]
combobox1 = ttk.Combobox(root,values = list1,height=10)
combobox1.set("Один")
combobox2 = ttk.Combobox(root,values = list1,height=10)
combobox2.set("Один")
b1 = Button(root, text="Сгенерировать номер ", font='Times 14')
b2 = Button(root, text="Сгенерировать ещё ", font='Times 14')
label1.grid(row=1,column=0)
label2.grid(row=1,column=2)
label3.grid(row=2,column=2)
entry1.grid(row=1, column=1,  padx=5, pady=5)
combobox1.grid(row=1,column=3,  padx=5, pady=5)
combobox2.grid(row=2,column=3)
b1.grid(row=4, column=0, padx=5, pady=5)
b2.grid(row=4, column=1, padx=5, pady=5)
label4.grid(row=3,column=0)

entry2.grid(row=3, column=1,  padx=5, pady=5)




root.mainloop()