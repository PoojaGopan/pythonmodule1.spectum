#calculator using tkinter
# import tkinter#to import tkinter module and its all packages
# from tkinter import *
# root=Tk()#to call it as a function

# root.title("simple calculator")
# root.geometry("570x600+100+200")
# root.resizable(False,False)
# root.configure(bg="#17161b")#to configure various tkinter windows and hexcode to set to a dark colour

# equation=""
# def show(value):
#     global equation#value is appended to global equation
#     equation+=value
#     label_result.config(text=equation)#text of the label widget updated

# def clear():
#     global equation
#     equation=""
#     label_result.config(text=equation)#clear function sets equation to an empty string

# def Calculate():
#     global equation
#     result=""
#     if equation !="":
#         try:
#             result=eval(equation)#built in function to evaluate
#         except:
#             result="error"#error other wise
#             equation=""
#     label_result.config(text=result)

# label_result=Label(root,width=25,height=2,text="",font=("ariel",30))
# label_result.pack()

# Button(root,text="c",width=5,height=1,font=("ariel",30,"bold"),bd=1,fg="#fff",bg="#3697f5",command=lambda: clear()).place(x=10,y=100)#button widget used and cleasr function called
# Button(root,text="/",width=5,height=1,font=("ariel",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda: show("/")).place(x=150,y=100)#.place specifies the coordinanates of the widget
# Button(root, text="%", width=5, height=1, font=("Arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("%")).place(x=290, y=100)
# Button(root,text="*",width=5,height=1,font=("ariel",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda: show("*")).place(x=430,y=100)

# Button(root,text="7",width=5,height=1,font=("ariel",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda: show("7")).place(x=10,y=200)
# Button(root,text="8",width=5,height=1,font=("ariel",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda: show("8")).place(x=150,y=200)
# Button(root,text="9",width=5,height=1,font=("ariel",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda: show("9")).place(x=290,y=200)
# Button(root,text="-",width=5,height=1,font=("ariel",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda: show("-")).place(x=430,y=200)

# Button(root,text="4",width=5,height=1,font=("ariel",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda: show("4")).place(x=10,y=300)
# Button(root,text="5",width=5,height=1,font=("ariel",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda: show("5")).place(x=150,y=300)
# Button(root,text="6",width=5,height=1,font=("ariel",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda: show("6")).place(x=290,y=300)
# Button(root,text="+",width=5,height=1,font=("ariel",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda: show("+")).place(x=430,y=300)

# Button(root,text="1",width=5,height=1,font=("ariel",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda: show("1")).place(x=10,y=400)
# Button(root,text="2",width=5,height=1,font=("ariel",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda: show("2")).place(x=150,y=400)
# Button(root,text="3",width=5,height=1,font=("ariel",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda: show("3")).place(x=290,y=400)
# Button(root,text="0",width=11,height=1,font=("ariel",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda: show("0")).place(x=10,y=500)

# Button(root,text=".",width=5,height=1,font=("ariel",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda: show(".")).place(x=290,y=500)
# Button(root,text="=",width=5,height=3,font=("ariel",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda: Calculate()).place(x=430,y=400)#run the calcutate function


# root.mainloop()#start the main event and run

#simple GUI
# import tkinter as tk

# def print_user_input():
#     user_input = entry.get()#extracting the text entered by user
#     output_text.config(state=tk.NORMAL)  # Enable editing the text widget
#     output_text.delete(1.0, tk.END)      # Clear previous content
#     output_text.insert(tk.END, user_input)
#     output_text.config(state=tk.DISABLED)  # Disable editing the text widget

# # Create the main window
# root = tk.Tk()
# root.title("Simple Function GUI")

# # Create an Entry widget for user input
# entry = tk.Entry(root, width=30)
# entry.pack(pady=10)#arrange widget in parent widget#padding to look into spacing

# # Create a Button widget to trigger the function
# button = tk.Button(root, text="Print Input", command=print_user_input)
# button.pack(pady=10)

# # Create a Text widget for displaying output
# output_text = tk.Text(root, height=5, width=30, state=tk.DISABLED)
# output_text.pack(pady=10)

# # Run the main loop
# root.mainloop()

#label widget
# import tkinter as tk
# root = tk.Tk()
# root.title("Label Configuration Example")
# # Create a Label widget
# label = tk.Label(root, text="Hello, Tkinter!")
# # Configure Label options: background and font
# label.config(bg="blue", font=("Times New Roman", 18))
# # Pack the Label widget
# label.pack(padx=10, pady=10)
# root.mainloop()
