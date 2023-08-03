import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from typing import Optional


def load_xml_file(initialdir: Optional[str] = None) -> str:
    tk.Tk().withdraw()
    return filedialog.askopenfilename(
        title="Choose an XML File",
        filetypes=[("XML Documents", "*.xml"), ("All Files", "*.*")],
        initialdir=initialdir or "./",
    )

def save_xml_file(initialfile: Optional[str] = None, initialdir: Optional[str] = None) -> str:
    tk.Tk().withdraw()
    return filedialog.asksaveasfilename(
        title="Save As",
        initialfile=initialfile or "Untitled.xml", 
        defaultextension=".xml", 
        filetypes=[("XML Documents", "*.xml"), ("All Files", "*.*")],
        initialdir=initialdir or "./",
    )

def program_closed_unexpectedly(message: str = 'Program closed unexpectedly.') -> None:
    messagebox.showerror(title='Error', message=message)

def warning(message: str) -> None:
    messagebox.showwarning(title='Warning', message=message)
    