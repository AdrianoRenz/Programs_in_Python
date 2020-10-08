import tkinter
import subprocess
from tkinter import filedialog
from tkinter import messagebox

#▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
# You need to have the FFmpeg and Tkinter packages installed 
# on your computer to use this file.
#▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄

#Here it says in what format will convert the file.
extension = '.mp4'

# Opens a file selection window, then opens another 
# window to the location where you want to save the file.
filename = filedialog.askopenfilename()
path     = filedialog.askdirectory()

filename = filename.replace( ' ', ' ' )
path     = path.replace( ' ', ' ' )

#Debug GET files
print(filename)
print(path)

#Run the program.
subprocess.run(['ffmpeg', '-i', filename, path+"./Name"+extension])

#Done Message
messagebox.showinfo(title="Done", message="Done")

