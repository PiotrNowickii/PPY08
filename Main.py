import tkinter as tk
from screeninfo import get_monitors
root = tk.Tk()

def change_text():
    text = "Witaj "+entry.get()
    who = "\nJesteś: "+radio_var.get()
    langs = "\nJęzyki: \n"
    for i in range(len(checkbox_vars)):
        if checkbox_vars[i].get() == 1:
            langs = langs + " " + checkboxes[i].cget("text") + "\n"
    experience = "\n" + str(slider.get()) + " lat doświadczenia"
    label.config(text=text + who + langs + experience)
    pass

# root.geometry("800x600")
root.title("Book Store")
root.iconbitmap("./bookshelf.ico")
screen_width = get_monitors()[0].width
screen_height = get_monitors()[0].height
#root.geometry(f"{int(screen_width/2)}x{int(screen_height/2)}")

left_frame = tk.Frame(root, borderwidth=4, relief="ridge", width=int(screen_width/4), height=int(screen_height / 3))
left_frame.pack(side="left", padx=10, pady=10)
left_frame.pack_propagate(0)

right_frame = tk.Frame(root, width=int(screen_width/6), height=left_frame["height"],borderwidth=4,relief="ridge")
right_frame.pack(side="right", padx=10, pady=10)
right_frame.pack_propagate(0)

label = tk.Label(right_frame, text="Podaj imie i nazwisko")
label.pack()
entry = tk.Entry(left_frame)
entry.pack(anchor="w", padx=10, pady=10)
button = tk.Button(left_frame, text="OK", command=change_text)
button.pack(anchor="w", padx=20)

root.resizable(width=False, height=False)

radio_var = tk.StringVar(value="RadioButton1")
radio_button1 = tk.Radiobutton(left_frame, text="tester", variable=radio_var, value="tester")
radio_button1.pack(anchor="w", padx=10, pady=10)

radio_button2 = tk.Radiobutton(left_frame, text="programista",  variable=radio_var, value="programmer")
radio_button2.pack(anchor="w", padx=10, pady=10)

checkbox_vars = []
checkboxes = []

checkbox_vars.append(tk.IntVar())
checkbox = tk.Checkbutton(left_frame, text="java", variable=checkbox_vars[0])
checkbox.pack(anchor="w", padx=10, pady=10)
checkboxes.append(checkbox)
checkbox_vars.append(tk.IntVar())
checkbox2 = tk.Checkbutton(left_frame, text="python", variable=checkbox_vars[1])
checkbox2.pack(anchor="w",padx=10,pady=10)
checkboxes.append(checkbox2)

slider = tk.Scale(left_frame, from_=0, to=25, orient=tk.HORIZONTAL)
slider.pack(anchor="w", padx=10, pady=10)

root.mainloop()