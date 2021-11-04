from tkinter import font


try:
    import math
    import tkinter as tk
    from tkinter import *
    from tkinter.ttk import *
    from tkinter import messagebox
    import tkinter.font as TkFont
    from tkinter.font import *
    import random
    import webbrowser
except Exception as err:
    tk.messagebox.showerror('Module Error', err)

MiniCordUI = None
Debugging = False
SuperSecretSetting = False

class MiniCord():

    def startup():

        # Dont forget to rewrite the creation of the UI its messyyy

        MiniCordUI = tk.Tk()
        MiniCordUI.title('Mini-Cord Build 0.0.2')

        MiniCordUI.resizable(True, True)
        MiniCordUI.geometry('1000x650')

        # Do debugging checks
        if Debugging != False:
            MiniCordUI.overrideredirect(False)
        else:
            MiniCordUI.overrideredirect(True)


        # Create Mini-cords UI
        # Topbar Related Stuff
        TopBarFrame = tk.Frame(MiniCordUI, background='#202225',height=22)
        TopBarFrame.pack(anchor=N,fill="x", expand=True)
        TitleBar = tk.Label(MiniCordUI, background='#202225', height= 1, foreground='grey',text='Discord', font=('PT Sans Narrow', 12))
        TitleBar.pack(anchor=N, expand=True) 
        TitleBar.place(relx=0.02,rely=0.1)
        CloseButton = tk.Label(MiniCordUI, background='#202225', foreground='white', text='✕',height=1, font=('Courier', 11))
        CloseButton.pack(anchor=N, expand=True)
        CloseButton.place(relx=0.98,rely=-0.002)
        MaximiseButton = tk.Label(MiniCordUI, background='#202225', foreground='white', text='◻',height=1, font=('Courier', 13))
        MaximiseButton.pack(anchor=N, expand=True)
        MaximiseButton.place(relx=0.96,rely=-0.00425)
        MinimiseButton = tk.Label(MiniCordUI, background='#202225', foreground='white', text='─',height=1, font=('Courier', 13))
        MinimiseButton.pack(anchor=N, expand=True)
        MinimiseButton.place(relx=0.94,rely=-0.0055)

        # ─ ◻ ✕

        # Bind actions
        TopBarFrame.bind("<ButtonPress-1>", lambda e: MiniCord.start_move(MiniCordUI, e))
        TopBarFrame.bind("<ButtonRelease-1>", lambda e: MiniCord.stop_move(MiniCordUI, e))
        TopBarFrame.bind("<B1-Motion>", lambda e: MiniCord.do_move(MiniCordUI, e))
        CloseButton.bind("<Enter>", lambda e: CloseButton.config(background='red'))
        CloseButton.bind("<Leave>", lambda e: CloseButton.config(background='#202225'))
        CloseButton.bind("<ButtonPress-1>", lambda e: quit())
        MaximiseButton.bind("<Enter>", lambda e: MaximiseButton.config(background='grey'))
        MaximiseButton.bind("<Leave>", lambda e: MaximiseButton.config(background='#202225'))
        MinimiseButton.bind("<Enter>", lambda e: MinimiseButton.config(background='grey'))
        MinimiseButton.bind("<Leave>", lambda e: MinimiseButton.config(background='#202225'))

        MiniCordUI.mainloop()

    # Handle Movement of window

    def start_move(self, event):
        self.x = event.x
        self.y = event.y

    def stop_move(self, event):
        self.x = None
        self.y = None

    def do_move(self, event):
        deltax = event.x - self.x
        deltay = event.y - self.y
        x = self.winfo_x() + deltax
        y = self.winfo_y() + deltay
        self.geometry(f"+{x}+{y}")



# Actualy start minicord smh
MiniCord.startup()

        


