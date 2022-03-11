import tkinter as tk
from tkinter import scrolledtext

from no_annotation.stirp_annotation import clean_training


class NoAnnotation(tk.Tk):
    def __init__(self):
        super().__init__()

        """Configure root window"""
        self.title("No annotation")
        self.geometry("500x500")

        """ScrolledText widget for the input"""
        self.text_box = scrolledtext.ScrolledText(self, width=100, height=15)
        self.text_box.pack(fill='x')
        self.text_box.insert('1.0', 'Your training goes here')

        """Button strip annotation"""
        self.strip_annotation_button = tk.Button(text="Strip annotation",
                                                 command=self.user_input)
        self.strip_annotation_button.pack()

        """ScrolledText widget for the output"""
        self.text_box2 = scrolledtext.ScrolledText(self, width=100, height=15)
        self.text_box2.pack(fill='x', side=tk.BOTTOM)

    def user_input(self):
        for i in clean_training(self.text_box.get("1.0", tk.END)):
            self.text_box2.insert('1.0', f"{i}\n")