from tkinter import *

window = Tk()
window.title("Naru's first GUI program")
window.minsize(width=500, height=300)
window.config(padx=120, pady=200)

def button_clicked():
    print("I got clicked")
    my_label['text'] = input.get()


#Label

my_label = Label(text="I am a label", font=('Arial', 24, 'italic'))
my_label['text'] = 'New text'
my_label.config(text="TEEXT")
my_label.pack(side='left')
# my_label.place(x=100, y=200)
my_label.grid(column=0, row=0)

#Button

button = Button(text='click me', command=button_clicked)
button.grid(column=1, row=1)

new_button = Button(text='new click me', command=button_clicked)
new_button.grid(column=3, row=0)

#Entry

input = Entry(width=10)
input.grid(column=4, row=3)





window.mainloop()