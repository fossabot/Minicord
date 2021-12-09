try:
    import math
    import tkinter as tk
    from tkinter import *
    from tkinter.ttk import *
    from tkinter import messagebox
    from tkinter.font import *
    import random
    import webbrowser
    from PIL import Image, ImageTk
except Exception as err:
    tk.messagebox.showerror('Module Error', err)

MiniCordUI = None
Debugging = False
SuperSecretSettings = False

 # ─ ◻ ✕

# Log into minicord with this
Email = 'user@defaultemail.com'
Password = 'password'
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# Not even working so yh have fun
# Patch 0.0.4 Key

default1 = '#202225'
default2 = '#292b2f'
default3 = '#36393f'

TitleText = 'Minicord'

class MiniCord():

    def startup():

        # Dont forget to rewrite the creation of the UI its messyyy

        MiniCordUI = tk.Tk()
        MiniCordUI.title('Mini-Cord Build 0.0.2')

        MiniCordUI.resizable(True, True)
        MiniCordUI.geometry('1000x650')

        # Allow minicord to show window borders if debugging is toggled on
        if Debugging != False:
            MiniCordUI.overrideredirect(False)
        else:
            MiniCordUI.overrideredirect(True)


        # Create Mini-cords UI
        # Create Minicords Topbar
        TopBarFrame = tk.Frame(MiniCordUI, background=default1,height=22)
        TopBarFrame.pack(anchor=N,fill="x", expand=True)
        CloseButton = tk.Label(MiniCordUI, background=default1, foreground='white', text='✕',height=1, font=('Courier', 11))
        CloseButton.pack(anchor=N, expand=True)
        CloseButton.place(relx=0.98,rely=-0.002)
        MaximiseButton = tk.Label(MiniCordUI, background=default1, foreground='white', text='◻',height=1, font=('Courier', 13))
        MaximiseButton.pack(anchor=N, expand=True)
        MaximiseButton.place(relx=0.96,rely=-0.00425)
        MinimiseButton = tk.Label(MiniCordUI, background=default1, foreground='white', text='─',height=1, font=('Courier', 13))
        MinimiseButton.pack(anchor=N, expand=True)
        MinimiseButton.place(relx=0.9425,rely=-0.0055)

        # Create Minicords MainUI's
        BackFrame = tk.Frame(MiniCordUI, background=default2,borderwidth=0, height=5000)
        BackFrame.pack(anchor=N, fill='x', expand=True)
        ServerList = tk.Frame(MiniCordUI, background=default1, borderwidth=0, height=5000, width=60)
        ServerList.pack(anchor=W, fill='y', expand=True)
        ServerList.place(relx=0,rely=0)
        #Load the home button and other stuff
        LoadHomeButton = Image.open('images/HomeButton.png')
        ResizeLoadedHomeButton = LoadHomeButton.resize((45,45), Image.ANTIALIAS)
        RenderHomeButton = ImageTk.PhotoImage(ResizeLoadedHomeButton)
        #----
        LoadCircle = Image.open('images/Circle.png')
        ResizeLoaddedCircle = LoadCircle.resize((80,80), Image.ANTIALIAS)
        RenderCircle = ImageTk.PhotoImage(ResizeLoaddedCircle)
        #----
        LoadCircleHover = Image.open('images/CircleHover.png')
        ResizeLoaddedCircleHover = LoadCircleHover.resize((80,80), Image.ANTIALIAS)
        RenderCircleHover = ImageTk.PhotoImage(ResizeLoaddedCircleHover)
        #---
        LoadHomeTag = Image.open('images/HomeTag.png')
        ResizeLoadedHomeTag = LoadHomeTag.resize((90,50), Image.ANTIALIAS)
        RenderHomeTag = ImageTk.PhotoImage(ResizeLoadedHomeTag)
        # Create Home Button + template server
        HomeButtonCircle = tk.Label(MiniCordUI, background=default1, borderwidth=0, height=60, width=58, image=RenderCircle)
        HomeButtonCircle.pack(anchor=N, expand=True)
        HomeButtonCircle.place(relx=0.0005,rely=0.03)

        HomeButton = tk.Label(HomeButtonCircle, background=default3,borderwidth=0, height=38, width=38, image=RenderHomeButton)
        HomeButton.pack(anchor=N, expand=True)
        HomeButton.place(relx=0.165,rely=0.175)

        HomeTag = tk.Label(MiniCordUI, background =default2, borderwidth=0, height=45, width=72, image=RenderHomeTag)
        HomeTag.pack(anchor=CENTER, expand=True)
        HomeTag.place(relx=9,rely=9)


        # Patch the title last to prevent it being overlapped (too lazy to use z-index :D)
        TitleBar = tk.Label(MiniCordUI, background=default1, height= 1, foreground='grey',text=TitleText, font=('PT Sans Narrow', 10))
        TitleBar.pack(anchor=N, expand=True) 
        TitleBar.place(relx=0.0025,rely=0.00005)

        # Bind actions
        TopBarFrame.bind("<ButtonPress-1>", lambda e: HandleMovement.start_move(MiniCordUI, e))
        TopBarFrame.bind("<ButtonRelease-1>", lambda e: HandleMovement.stop_move(MiniCordUI, e))
        TopBarFrame.bind("<B1-Motion>", lambda e: HandleMovement.do_move(MiniCordUI, e))
        CloseButton.bind("<Enter>", lambda e: CloseButton.config(background='red'))
        CloseButton.bind("<Leave>", lambda e: CloseButton.config(background=default1))
        CloseButton.bind("<ButtonPress-1>", lambda e: quit())
        MaximiseButton.bind("<Enter>", lambda e: MaximiseButton.config(background='grey'))
        MaximiseButton.bind("<Leave>", lambda e: MaximiseButton.config(background=default1))
        MinimiseButton.bind("<Enter>", lambda e: MinimiseButton.config(background='grey'))
        MinimiseButton.bind("<Leave>", lambda e: MinimiseButton.config(background=default1))
        HomeButtonCircle.bind("<Enter>", lambda e: [HomeButtonCircle.config(image=RenderCircleHover), HomeButton.config(background='#5865f2'), HomeTag.place(relx=0.065,rely=0.0385)])
        HomeButtonCircle.bind("<Leave>", lambda e: [HomeButtonCircle.config(image=RenderCircle), HomeButton.config(background=default3), HomeTag.place(relx=9,rely=9)])

        HandlePageSwapping.Home(MiniCordUI)

        MiniCordUI.mainloop()


# Handle Movement of window
class HandleMovement:
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


# Handle Page Swapping
class HandlePageSwapping:

    def Home(MiniCordUI):
        SideBar = tk.Frame(MiniCordUI, background='#2f3136', borderwidth=0, height=5000, width=200)
        SideBar.pack(anchor=W, fill='y', expand=True)
        SideBar.place(rely=0.0333,relx=0.06)


# Actualy start minicord smh
MiniCord.startup()

        

# v0
# Hey how is ur day going?
# Hope you enjoyed this lil project i made for fun :D 
# yes pogger
