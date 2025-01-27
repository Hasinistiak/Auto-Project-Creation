import tkinter as tk

root = tk.Tk()


root.geometry("330x250")
root.title("Project Creator")


langs = ["Python", "C++", "React", "React Native", "Rust", "Tauri"]

letters_list = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]


selected_lang = tk.StringVar()
selected_lang.set(langs[0])




label1 = tk.Label(root, text="Enter A Name For Your Project", font=('Inter', 15))
label1.grid(row=0, column=0, padx=10, pady=10, sticky='ew')

entry1 = tk.Entry(root, font=('Inter', 13))
entry1.grid(row=1, column=0, padx=10, pady=10, sticky='ew')

def setName():
    name = entry1.get()
    return name

label2 = tk.Label(root, text="Select a Language", font=('Inter', 15))
label2.grid(row=2, column=0, padx=10, pady=10, sticky='ew')

entry2 = tk.OptionMenu(root, selected_lang, *langs)
entry2.grid(row=3, column=0, padx=10, pady=10, sticky='ew')

def setLang():
    lang = selected_lang.get()
    return lang

def onclick():
    print(f"Lang : {setLang()}")
    print(f"Name : '{setName()}'")


def update_button_state():
    name = setName()

    if (name.startswith('_') or (name and name[0] in letters_list)) and selected_lang.get() == 'Python':
        button.grid(row=4, column=0, padx=10, pady=10, sticky='e')
    else:
        button.grid_remove() 

button = tk.Button(root, text="Setup Environment", font=('Inter', 10), command=onclick)

entry1.bind('<KeyRelease>', lambda e: update_button_state())

selected_lang.trace('w', lambda *args: update_button_state())

update_button_state()




root.mainloop()