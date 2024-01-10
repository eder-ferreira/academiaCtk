import tkinter
import customtkinter
from PIL import Image,ImageTk

customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

app = customtkinter.CTk()  # create CTk window like you do with the Tk window
wdth = app.winfo_screenwidth()
hgt = app.winfo_screenheight()
app.geometry("%dx%d"%(wdth,hgt))

def button_function():
    print("button pressed")

img1=customtkinter.CTkImage(Image.open(r"img/logo3.png"))

# Use CTkButton instead of tkinter Button

button = customtkinter.CTkButton(master=app,image = img1, text="",width=500,height=200, command=button_function,compound='left')
button.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

app.mainloop()