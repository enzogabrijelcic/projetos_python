#reproduzir uma janela

import tkinter as tk
from tkinter import ttk

root = tk.Tk()

message1 = tk.Label(root, text="Label 2", fg="white", background= 'green')
message1.pack(side="left")

message2 = tk.Label(root, text="Label 3", fg="white", background= 'blue')
message2.pack(side="left")

message3 = tk.Label(root, text="Label 1", fg="white",background= 'red')
message3.pack(side="left")

root.mainloop()