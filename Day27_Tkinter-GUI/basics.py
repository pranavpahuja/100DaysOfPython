import tkinter

window = tkinter.Tk()
window.title("Hello")
window.minsize(width=500, height=300)

my_label = tkinter.Label(text="I Am A Label", font=("Ariel", 24, "bold"))
my_label.pack()


window.mainloop()