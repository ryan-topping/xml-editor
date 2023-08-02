import tkinter as tk
from tkinter import filedialog
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
