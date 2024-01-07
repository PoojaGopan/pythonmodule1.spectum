#photo image
# from tkinter import *#to import all packages
# from tkinter import ttk#to import image

# root = Tk()
# label = Label(root, text="This is Image").pack(side=TOP, pady=10)

# path = PhotoImage(file="C:/Users/ASUS/Downloads/flower.png")#only png files supported
# label_image = Label(root, image=path,width=800, height=800)
# label_image.pack()

# root.geometry("600x440")
# root.title("PythonLobby.com")
# root.mainloop()

# from tkinter import *
# window=Tk()#window,frame,root
# window.title("message")
# window.geometry("600x400")#height and width
# a=Label(window,text="hello")
# a.pack()#save
# b=Entry(window)
# b.pack()
# def name():
#     d=Label(window,text="hi")
#     d.pack()
# c=Button(window,text="click",command=name)
# c.pack()
# window.mainloop()

# from tkinter import *
# window=Tk()
# window.title("login")
# window.geometry("600x400")
# a=Label(window,text="enter username and password")
# a.pack()
# b=Entry(window)
# b.pack()
# e=Entry(window)
# e.pack()
# def name():
#     d=Label(window,text="logging in")
#     d.pack()
# c=Button(window,text="enter",command=name)
# c.pack()
#window.mainloop()#to close to run

# from tkinter import *
# frame=Tk()
# l1=Label(frame,text="username")
# l2=Label(frame,text="passowrd")
# entry=Entry(frame)
# entry2=Entry(frame)
# l1.grid(row=0,column=0)#matrix position (00,01,10,11) according to grid
# entry.grid(row=0,column=1)
# l2.grid(row=1,column=0)
# entry2.grid(row=1,column=1)
# btn=Button(frame,text="login",fg="red",bg="black")#button,label,checkout etc are widgets#forground colur and background colour
# btn.grid(row=2,column=0)
# frame.mainloop()

#canvas in tkinder
# from tkinter import *
# #setting up parent window
# root = Tk()
# canvas = Canvas(root, bg="red", width=150, height=250)
# canvas.pack()
# line = canvas.create_line(100,100,240,10)#these dimensions are distance from each end
# root.geometry("350x220")
# root.title("PythonLobby.com")
# root.mainloop()

# from tkinter import *
# #setting up parent window
# root = Tk()
# canvas = Canvas(root, bg="yellow", width=150, height=250)#canvas widget
# canvas.pack()
# rectangle= canvas.create_oval(30, 20, 120, 110, fill="light green")#change dimensions of oval to make circle;the dimensions are the distance of the circle from the rectangle
# root.geometry("350x220")
# root.title("PythonLobby.com")
# root.mainloop()

# from tkinter import *
# #setting up parent window
# root = Tk()

# canvas = Canvas(root, bg="yellow", width=150, height=250)
# canvas.pack()
# line = canvas.create_line(30,50,100,5,23,30, width=5, fill="red")

# root.geometry("350x220")
# root.title("PythonLobby.com")
# root.mainloop()

# from tkinter import *
# #setting up parent window
# root = Tk()

# canvas = Canvas(root, bg="yellow", width=150, height=250)
# canvas.pack()
# rectangle= canvas.create_rectangle(30,20,140,90, fill="light green")
# root.geometry("350x220")
# root.title("PythonLobby.com")
# root.mainloop()

# from tkinter import *
# root = Tk()
# root.title("PythonLobby")
# w = Label(root, text='PythonLobby.Com', font="60")
# w.pack()
# Checkbox1 = IntVar()#to store checkbox values as integers only
# Checkbox2 = IntVar()

# Button0 = Checkbutton(root, text="Learning",
#                       variable=Checkbox1,
#                       onvalue=1,#if checked then 1 other wise zero
#                       offvalue=0,
#                       height=3,
#                       width=12)

# Button1 = Checkbutton(root, text="Tutorial",
#                       variable=Checkbox2,
#                       onvalue=1,
#                       offvalue=0,
#                       height=3,
#                       width=12)
# Button0.pack()
# Button1.pack()
# root.geometry("320x220")
# mainloop() 

#radiobutton only one selection possible
# Importing Tkinter module
# from tkinter import *
# root = Tk()
# root.title("PythonLobby")
# # Tkinter string variable it can store any string value
# value1 = StringVar(root,"1")#variable that holds string value #default first check box selected
# rbtn1 = Radiobutton(root, text="Radio Button 1", variable = value1 , value="1") #value corresponding to each box
# rbtn1.pack()
# rbtn2 = Radiobutton(root, text="Radio Button 2", variable = value1 , value="2")
# rbtn2.pack()
# rbtn3 = Radiobutton(root, text="Radio Button 3", variable = value1 , value="3")
# rbtn3.pack()
# root.geometry("250x200")
# mainloop()

#menu button widget
# from tkinter import *
# root = Tk() 
# root.geometry("300x200") 
# w = Label(root, text ='GeeksForGeeks', font = "50")  
# w.pack() 
# menubutton = Menubutton(root, text = "Menu")    
# menubutton.menu = Menu(menubutton)   
# menubutton["menu"]= menubutton.menu   
# var1 = IntVar() 
# var2 = IntVar() 
# var3 = IntVar() 
# menubutton.menu.add_checkbutton(label = "Courses", 
#                                 variable = var1)   
# menubutton.menu.add_checkbutton(label = "Students", 
#                                 variable = var2) 
# menubutton.menu.add_checkbutton(label = "Careers", 
#                                 variable = var3) 
# menubutton.pack()   
# root.mainloop() 

# import tkinter as tk
# root = tk.Tk()
# root.title("Menu Example")
# # Create a menu bar
# menu_bar = tk.Menu(root)
# root.config(menu=menu_bar)
# # Create a File menu
# file_menu = tk.Menu(menu_bar, tearoff=0)
# menu_bar.add_cascade(label="File", menu=file_menu)#a cascading submenu to the menu
# # Add items to the File menu
# file_menu.add_command(label="New")#to be executed when the menu item is clicked
# file_menu.add_command(label="Open")
# file_menu.add_separator()#the line in btwn
# file_menu.add_command(label="Exit", command=root.destroy)
# # Create an Edit menu
# edit_menu = tk.Menu(menu_bar, tearoff=0)#A tear-off menu is a small, detachable window that contains the menu items. When you set the tearoff option to a non-zero value, a tear-off menu is created
# menu_bar.add_cascade(label="Edit", menu=edit_menu)
# # Add items to the Edit menu
# edit_menu.add_command(label="Cut")
# edit_menu.add_command(label="Copy")
# edit_menu.add_command(label="Paste")
# # Start the Tkinter event loop
# root.mainloop()

# from tkinter import *
# #setting up parent window
# root = Tk()
# textbox=Text(root, width=40, height=13, wrap=WORD)
# textbox.grid(row=0, column=0)
# scroll=Scrollbar(root, orient=VERTICAL, command= textbox.yview)
# scroll.grid(row=0, column=1, sticky=N+S)
# textbox.config(yscrollcommand=scroll.set)
# root.geometry("350x220")
# root.title("PythonLobby.com")
# root.mainloop()


#scroll bar
# from tkinter import *
# #setting up parent window
# root = Tk()
# textbox=Text(root, width=40, height=13)
# textbox.grid(row=0, column=0)
# scroll=Scrollbar(root, orient=VERTICAL, command= textbox.yview)
# scroll.grid(row=0, column=1, sticky=N+S)
# textbox.config(yscrollcommand=scroll.set)
# root.geometry("350x220")
# root.title("PythonLobby.com")
# root.mainloop()

# #listbox
# import tkinter as tk
# root = tk.Tk()
# root.title("Listbox Example")
# # Create a Listbox widget
# listbox = tk.Listbox(root, selectmode=tk.SINGLE)#listbox widget#seelection of listbox,selection of one item in the list
# listbox.pack()#pack a widget in tkinter
# # Add items to the Listbox
# items = ["Item 1", "Item 2", "Item 3", "Item 4", "Item 5"]
# for item in items:
#     listbox.insert(tk.END, item)#end of list
# # Start the Tkinter event loop
# root.mainloop()
