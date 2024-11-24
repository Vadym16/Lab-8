# -*- coding: utf-8 -*-
import tkinter as tk


def create_scales():

    root = tk.Tk()
    root.title("Sunh")

   
    linked_ = tk.IntVar(value=50)

    
    horizontal = tk.Scale(
        root,
        from_=0,
        to=100,
        orient="horizontal",
        variable=linked_
    )
    horizontal.pack(pady=10)

    
    vertical = tk.Scale(
        root,
        from_=0,
        to=100,
        orient="vertical",
        variable=linked_
    )
    vertical.pack(pady=10)

    
    root.mainloop()


create_scales()
