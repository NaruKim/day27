import tkinter

FONT = ('Arial', 20,)

window = tkinter.Tk()
window.title("Naru's miles to kilos")
window.minsize(width=200, height=150)

def button_down():
    mile = float(mile_input.get())
    km = mile*1.609
    km_input.delete(0, 100)
    km_input.insert(0, km)

label30 = tkinter.Label(text="Miles", font=FONT)
label30.grid(column=3, row=0)

label31 = tkinter.Label(text='Km', font=FONT)
label31.grid(column=3, row=1)

label01 = tkinter.Label(text='is equal to', font=FONT)
label01.grid(column=0, row=1)

mile_input = tkinter.Entry(width=20)
mile_input.grid(column=2, row=0)
mile_input.insert(0, 0)

km_input = tkinter.Entry(width=20)
km_input.grid(column=2, row=1)
km_input.insert(0, 0)

calculate_button = tkinter.Button(text='calculate', command=button_down, font=FONT)
calculate_button.grid(column=2, row=3)


















window.mainloop()