from customtkinter import (CTk, CTkLabel, CTkFrame, CTkEntry, CTkButton, CTkOptionMenu,
                           CTkCheckBox, StringVar, CTkImage, CTkScrollableFrame, CTkToplevel,
                           set_appearance_mode, set_default_color_theme, CTkBaseClass)

class App(CTk):
    def __init__(self) -> None:
        super().__init__()
        self.title("Cansat 2024")

def main():
    app = App()
    app.mainloop()

if __name__ == "__main__":
    main()