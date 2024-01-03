# #option menu
# import tkinter as tk
# root = tk.Tk()
# root.title("Simple OptionMenu Example")
# # Create a StringVar to store the selected option
# selected_option = tk.StringVar()
# # Set default value and available options
# selected_option.set("Option 1")#set default value
# options = ["Option 1", "Option 2", "Option 3"]
# # Create OptionMenu widget
# option_menu = tk.OptionMenu(root, selected_option, *options)#open menu widget
# option_menu.pack(pady=10)#spacing around the option menu
# # Start the Tkinter event loop
# root.mainloop()

# #panel
# import tkinter as tk
# root = tk.Tk()
# root.title("Panel Example")
# # Create a frame to resemble a panel
# panel_frame = tk.Frame(root, bg="lightgray", padx=20, pady=20)
# panel_frame.pack(padx=10, pady=10)
# # Add widgets to the panel frame
# label = tk.Label(panel_frame, text="This is a panel", font=("Helvetica", 16), bg="lightgray")
# label.pack(pady=10)
# button = tk.Button(panel_frame, text="Click me", command=root.destroy)#closes the UI
# button.pack()
# # Start the Tkinter event loop
# root.mainloop()
