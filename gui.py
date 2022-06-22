from PIL import Image,ImageTk
import tkinter as tk
from tkinter import filedialog
from tkinter import *

import numpy
import numpy as np

#Loading the Model
from keras.models import load_model
model=load_model('Age_Sex_Detector')

#Initializing the GUI
top=tk.TK()
top.geomentry('800x600')
top.title('Age & Gender Detector')
top.configure(background='#CDCDCD')

#Initializing the Labels (1 for age and 1 for sex)
label1=Label1(top,background="CDCDCD",font=('arial',15,"bold"))
label2=Label1(top,background="CDCDCD",font=('arial',15,"bold"))
sign_image=Label(top)
label1.pack(side="bottom",pady=50)
label2.pack(side="bottom",pady=50)
heading=Label(top,text="Age and Gender Detector",pady=20,font=('arial',15,"bold"))
heading.configure(background="CDCDCD",foreground="#364156")
heading.pack()
top.mainloop()