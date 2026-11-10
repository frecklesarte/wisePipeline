# Initializes the "tKinter" Python STL_UI module for creating the User Interface for the "DirectoryStructures" Pipeline Application
import tkinter
from tkinter import Tk as tk
from tkinter import ttk
#import directory_generation as dirGen
#from dirGen.validate_home_directory import valid


root = tk()

# Setting the window properties
root.title("cgi_Production_Structure_Tool")      # Window Title
root.configure(background="grey24")             # Window background color
root.minsize(600, 400)                          # Window Min, Max Sizing config
root.maxsize(1200, 1000)                        # Initial x, y size, as well as the x, y scale factor of the window.
root.geometry("800x600+30+20")                  # Boolean Operation, Allow or Disallow, scaling of x or y axis of 'root' window.
root.resizable(True, True)           # Default x=True, y=True


frm = ttk.Frame(root, padding=10)
frm.grid()


style = ttk.Style()
style.configure("BW.TLabel", foreground="black", background="white")


# The final label which attempts to setup the creation of the "Production, Directory Structure." 
# Creates the button used to quit the application and deinitialize
quitLabel = ttk.Button(root, text="Quit", command=root.destroy).grid(column=0, row=1)

# Create a check that makes sure the program frees from memory on the computer
root.mainloop()
