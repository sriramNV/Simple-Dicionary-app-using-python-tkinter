from tkinter import *
import json
from difflib import *


data = json.load(open("data.json"))
key = data.keys()
root = Tk()
root.title('DICTIONARY')
root.iconbitmap = '/icon2.ico'
labe = Label(root, text= "Enter the Word")
labe.pack(side="top")
e = Entry(root, width = 75)
e.pack(side = 'top')
label1 = Label(root,text="")
label2 = Label(root,text="")


def onClick():
   
    word = e.get()
    text1 = transform(word.lower())
    if type(text1) == list:
        for item in text1:
            label1['text'] = label1['text'] + '\n' + word + " : " + item
            label1.pack(side = 'top')
    else:
        label2['text'] = label2['text'] + '\n' + text1
        label2.pack(side='top')
    

def transform(w):
    if w in data:
        return (data[w])
    elif len(get_close_matches(w, key)) > 0:
        mw = get_close_matches(w,key)[0]
        return ("Did you mean %s instead? Go ahead and try again " %mw)
    else:
        return("Word NOT found, please check the word again!")

def dest():
    label1['text'] = ""
    label2['text'] = ""


myButton = Button(root, text = "FIND", command = onClick)
myButton.pack(side = 'top')
but = Button(root, text="CLEAR", command=dest)
but.pack(side = 'top')

root.mainloop()