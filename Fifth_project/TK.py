from tkinter import Tk, Button
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import showerror

root = Tk()
root.title("Example")
root.rowconfigure(5, weight=1)
root.columnconfigure(5, weight=1)
root.grid()


def load_file():
    first_file = askopenfilename()
    second_file = askopenfilename()
    if first_file and second_file:
        try:
            print("""here it comes: settings["template"].set(fname)""")
            print(first_file)
            file = open(str(fname), 'r')
            print(file.readline())  #

        except:  # <- naked except is a bad idea
            showerror("Open Source File", "Failed to read file\n'%s'" % fname)
            return


button = Button(root, text="Browse", command=load_file, width=10)
button.grid(row=1, column=0)

root.mainloop()