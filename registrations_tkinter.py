#import tkinter
from tkinter import *
root = Tk()

root.title("Tkinter | Registration form")

#define window geometry(window sizes)
root.geometry('512x512')

def getvals():
    print("Thanks for Submitting your data")
    
#Heading
Label(root, text='Tkinter Registration Form', font='ar 19 bold', bg='yellow').grid(row=0, column=3)

#field banes of the form
name = Label(root, text='Enter your name')
email = Label(root, text='Enter your email')
address = Label(root, text='Enter your address')
phone = Label(root, text='Enter your phone number')

#displaying or packing fields on the tkinter window
name.grid(row=1, column=2)
email.grid(row=2, column=2)
address.grid(row=3, column=2)
phone.grid(row=4, column=2)

#creating and assigning field values
namevalue = StringVar
emailvalue = StringVar
addressvalue = StringVar
phonevalue = StringVar
checkvalue = IntVar

#creating Entry fields
nameentry =Entry(root, textvariable=namevalue).grid(row=1, column=3)
emailentry =Entry(root, textvariable=emailvalue).grid(row=2, column=3)
addressentry =Entry(root, textvariable=addressvalue).grid(row=3, column=3)
phoneentry =Entry(root, textvariable=phonevalue).grid(row=4, column=3)
nameentry =Entry(root, textvariable=namevalue).grid(row=1, column=3)

#creating a checkbox
checkbtn = Checkbutton(root, text='Remember Me', textvariable=checkvalue).grid(row=5, column=3)

#creating button
Button(root, text='Submit',command=getvals).grid(row=6, column=3)

root.mainloop()