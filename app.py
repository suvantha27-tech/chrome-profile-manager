import customtkinter as ctk
from ui.main_window import MainWindow

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

if name == "__main__":
    app = MainWindow()
    app.mainloop()
