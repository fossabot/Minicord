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
SuperSecretSetting = False

 # ─ ◻ ✕

# Log into minicord with this
Email = 'user@defaultemail.com'
Password = 'password'
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# Not even working so yh have fun

class MiniCord():

    def startup():

        # Dont forget to rewrite the creation of the UI its messyyy

        MiniCordUI = tk.Tk()
        MiniCordUI.title('Mini-Cord Build 0.0.2')

        MiniCordUI.resizable(True, True)
        MiniCordUI.geometry('1000x650')
        MiniCordUI.wm_attributes('-transparentcolor', 'orange')

        # Allow minicord to show window borders if debugging is toggled on
        if Debugging != False:
            MiniCordUI.overrideredirect(False)
        else:
            MiniCordUI.overrideredirect(True)


        # Create Mini-cords UI
        # Create Minicords Topbar
        TopBarFrame = tk.Frame(MiniCordUI, background='#202225',height=22)
        TopBarFrame.pack(anchor=N,fill="x", expand=True)
        CloseButton = tk.Label(MiniCordUI, background='#202225', foreground='white', text='✕',height=1, font=('Courier', 11))
        CloseButton.pack(anchor=N, expand=True)
        CloseButton.place(relx=0.98,rely=-0.002)
        MaximiseButton = tk.Label(MiniCordUI, background='#202225', foreground='white', text='◻',height=1, font=('Courier', 13))
        MaximiseButton.pack(anchor=N, expand=True)
        MaximiseButton.place(relx=0.96,rely=-0.00425)
        MinimiseButton = tk.Label(MiniCordUI, background='#202225', foreground='white', text='─',height=1, font=('Courier', 13))
        MinimiseButton.pack(anchor=N, expand=True)
        MinimiseButton.place(relx=0.9425,rely=-0.0055)

        # Create Minicords MainUI's
        BackFrame = tk.Frame(MiniCordUI, background='#292b2f',borderwidth=0, height=5000)
        BackFrame.pack(anchor=N, fill='x', expand=True)
        ServerList = tk.Frame(MiniCordUI, background='#202225', borderwidth=0, height=5000, width=60)
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
        # Create Home Button + template server
        HomeButtonCircle = tk.Label(MiniCordUI, background='#202225', borderwidth=0, height=60, width=58, image=RenderCircle)
        HomeButtonCircle.pack(anchor=N, expand=True)
        HomeButtonCircle.place(relx=0.0005,rely=0.03)

        HomeButton = tk.Label(HomeButtonCircle, background='#36393f',borderwidth=0, height=38, width=38, image=RenderHomeButton)
        HomeButton.pack(anchor=N, expand=True)
        HomeButton.place(relx=0.165,rely=0.175)


        # Patch the title last to prevent it being overlapped (too lazy to use z-index :D)
        TitleBar = tk.Label(MiniCordUI, background='#202225', height= 1, foreground='grey',text='Discord Replica (By Preston)', font=('PT Sans Narrow', 10))
        TitleBar.pack(anchor=N, expand=True) 
        TitleBar.place(relx=0.0025,rely=0.00005)

        # Bind actions
        TopBarFrame.bind("<ButtonPress-1>", lambda e: HandleMovement.start_move(MiniCordUI, e))
        TopBarFrame.bind("<ButtonRelease-1>", lambda e: HandleMovement.stop_move(MiniCordUI, e))
        TopBarFrame.bind("<B1-Motion>", lambda e: HandleMovement.do_move(MiniCordUI, e))
        CloseButton.bind("<Enter>", lambda e: CloseButton.config(background='red'))
        CloseButton.bind("<Leave>", lambda e: CloseButton.config(background='#202225'))
        CloseButton.bind("<ButtonPress-1>", lambda e: quit())
        MaximiseButton.bind("<Enter>", lambda e: MaximiseButton.config(background='grey'))
        MaximiseButton.bind("<Leave>", lambda e: MaximiseButton.config(background='#202225'))
        MinimiseButton.bind("<Enter>", lambda e: MinimiseButton.config(background='grey'))
        MinimiseButton.bind("<Leave>", lambda e: MinimiseButton.config(background='#202225'))
        HomeButtonCircle.bind("<Enter>", lambda e: [HomeButtonCircle.config(image=RenderCircleHover), HomeButton.config(background='#5865f2')])
        HomeButtonCircle.bind("<Leave>", lambda e: [HomeButtonCircle.config(image=RenderCircle), HomeButton.config(background='#36393f')])

        
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


# Actualy start minicord smh
MiniCord.startup()

        


# Hey how is ur day going?
# Hope you enjoyed this lil project i made for fun :D 