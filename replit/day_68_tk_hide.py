import tkinter as tk
from PIL import Image, ImageTk

window = tk.Tk()
window.title("Guess Who?")
window.geometry("400x400")

label = "Guess Who?"


def showImage():
    person = text.get("1.0", "end")
    if person.lower().strip() == "pp":
        canvas.itemconfig(container, image=pp)
    # elif person.lower().strip() == "charlotte":
    #     canvas.itemconfig(container, image=charlotte)
    # elif person.lower().strip() == "gerald":
    #     canvas.itemconfig(container, image=gerald)
    # elif person.lower().strip() == "katie":
    #     canvas.itemconfig(container, image=katie)
    else:
        canvas.pack_forget()
        warning.pack()
        return
    warning.pack_forget()
    canvas.pack()


hello = tk.Label(text=label)
hello.pack()
warning = tk.Label(text="Unable to find this user")
text = tk.Text(window, height=1, width=30)
text.pack()
button = tk.Button(text="Find", command=showImage)
button.pack()
canvas = tk.Canvas(window, width=400, height=380)
canvas.pack()
# charlotte = ImageTk.PhotoImage(Image.open("guessWho/charlotte.jpg"))
# gerald = ImageTk.PhotoImage(Image.open("guessWho/gerald.jpg"))
# katie = ImageTk.PhotoImage(Image.open("guessWho/katie.jpg"))
pp = ImageTk.PhotoImage(Image.open("pp.jpg"))
container = canvas.create_image(200, 1, image=pp)

tk.mainloop()
