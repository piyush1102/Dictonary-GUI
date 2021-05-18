# importing necessary Modules
from tkinter import *
from PyDictionary import PyDictionary

# initializing Objects
dictonary = PyDictionary()
root = Tk()
# setting dimensions
root.geometry("400x400")


# root.resizable(0, 0)

# Command
def dict():
    meaning.config(text=dictonary.meaning(word.get())['Noun'][0])
    synonym.config(text=dictonary.synonym(word.get()))
    antonym.config(text=dictonary.antonym(word.get()))


# labelTag
Label(root, text="Dictionary", font=("Helvetica 20 bold"), fg="Blue").pack(pady=10)

# frame
frame = Frame(root)
Label(frame, text="Type Word", font=("Helvetica 15 bold")).pack(side=LEFT)
word = Entry(frame, font=("Helvetica 15 bold"))
word.pack()
frame.pack(pady=10)

# frame1
frame1 = Frame(root)
Label(frame1, text="Meaning: ", font=("Helvetica 10 bold")).pack(side=LEFT)
meaning = Label(frame1, text="", font=("Helvetica 15"))
meaning.pack()
frame1.pack(pady=10)

# frame2
frame2 = Frame(root)
Label(frame2, text="Synonym: ", font=("Helvetica 10 bold")).pack(side=LEFT)
synonym = Label(frame2, text="", font=("Helvetica 15"))
synonym.pack()
frame2.pack(pady=10)

# frame3
frame3 = Frame(root)
Label(frame3, text="Antonym: ", font=("Helvetica 10 bold")).pack(side=LEFT)
antonym = Label(frame2, text="", font=("Helvetica 15"))
antonym.pack()
frame3.pack(pady=10)

Button(root, text="Submit", font=("Helvetica 15 bold"), command=dict).pack()

root.mainloop()
