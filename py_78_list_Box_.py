# listbox = A listing of selectable text items within it's own container
from tkinter import *

def submit():

    food = []

    # print(listbox.curselection())   # you can see this value  for better understanding 

    for index in listbox.curselection():        # curselection(return indexes of items or keys) = retruns the current selection(current selected items) || now this is a list so we can easily traverse this 
        food.insert(index,listbox.get(index))      # inserting the value at the last in the food list

    print("You ordered : -------------- ")
    # print(listbox.get(listbox.curselection()))
    for index in food:
        print(index)

def add():
    listbox.insert(listbox.size(),entryBox.get())
    listbox.config(height=listbox.size())       # this will set the height of listbox dynamically

def delete():
    # listbox.delete(listbox.curselection())

    for index in reversed(listbox.curselection()):      # we need to delete the list in reverse because if we try in forword when we delete element the index of others will changed
        listbox.delete(index)

    listbox.config(height=listbox.size())       # this will set the height of listbox dynamically

window = Tk()

listbox = Listbox(window,
                  bg='#f7ffde',
                  font=("Constantia", 35),
                  width=12,                 # setting a convenient width for items
                  selectmode=MULTIPLE)      # deciding select multiple or one at a time
listbox.pack()

listbox.insert(1,"pizza")       # inserting values in listbox
listbox.insert(2,"pasta")
listbox.insert(3,"garlic bread")
listbox.insert(4,"soup")
listbox.insert(5,"salad")

listbox.config(height=listbox.size())       # this will set the height of listbox dynamically

entryBox = Entry(window)
entryBox.pack()

submitBtn = Button(window, text='submit', command=submit )
submitBtn.pack()

addBtn = Button(window, text='add', command=add )
addBtn.pack()

deleteBtn = Button(window, text='delete', command=delete )
deleteBtn.pack()

window.mainloop()