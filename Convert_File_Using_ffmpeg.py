import tkinter
import subprocess
from tkinter import filedialog
from tkinter import messagebox

#▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
# You need to have the FFmpeg and Tkinter packages installed 
# on your computer to use this file.
#▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄

# Opens a file selection window, then opens another 
# window to the location where you want to save the file.
filename = filedialog.askopenfilename()
path     = filedialog.askdirectory()

filename = filename.replace( ' ', ' ' )
path     = path.replace( ' ', ' ' )


# Below, convert the files to your preference, 
# where "Name.mp4" is written to the name you want.
subprocess.run(['ffmpeg', '-i', filename, path+"./Name.mp4"])
messagebox.showinfo(title="Done", message="Done")
