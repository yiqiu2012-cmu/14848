from tkinter import * 
from tkinter.ttk import *
from tkinter import filedialog as fd
import os
root = Tk()
root.geometry('200x100')
  
# This function will be used to open
# file in read mode and only Python files
# will be opened
def upload_file():
    filename = fd.askopenfilename()
    if filename is not None:
        os.system("gsutil cp " + filename +  " gs://dataproc-staging-us-central1-869165011218-kvle6tx4/")
  
btn = Button(root, text ='Select file to upload', command = lambda:upload_file())
btn.pack(side = TOP, pady = 10)
  
mainloop()