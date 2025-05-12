import customtkinter as CTk
from PIL import Image
import sys
import yaml

class MenuStart:
    def __init__(self):
        self.app = CTk.CTk()
        self.app.lift()
        self.app.focus_force()
        self.app.attributes('-topmost', 1)
        self.app.after(100, lambda: self.app.attributes('-topmost', 0))

        CTk.FontManager.load_font("assets/fonts/arcadeclassic.ttf")
        CTk.FontManager.load_font("assets/fonts/SF Atarian System.ttf")
        self.background = CTk.CTkImage(Image.open('assets/images/backgrounds/menu_bg.png'), size=(810, 500))
        self.accept_play = False
        self.records = self.get_data()
        
        self.configs()
        self.widgets()

    def get_data(self):
        with open("data/score.yml", 'r') as db:
            return yaml.safe_load(db)

    def configs(self):
        self.app.geometry("800x300+450+150")
        self.app.title("Menu Space Destroyer")
        self.app.resizable(False, False)
        self.app.protocol("WM_DELETE_WINDOW", self.quit_game)

    def widgets(self):
        score = self.records['score']
        survival = self.records['survival_time_record']

        CTk.CTkLabel(self.app, text='', image=self.background).place(relx=0.5, rely=0.5, anchor='center')

        CTk.CTkLabel(self.app, text=f"Maximum score: {score} points", font=('SF Atarian System', 23), fg_color='black').place(relx=0.68, rely=0.35)
        CTk.CTkLabel(self.app, text=f"Maximum time: {survival:.1f} seconds", font=('SF Atarian System', 23), fg_color='black').place(relx=0.68, rely=0.45)

        CTk.CTkLabel(self.app, text="SPACE DESTROYER", font=('arcadeclassic', 59), fg_color='black').place(relx=0.4, rely=0.13, anchor="center")
        
        CTk.CTkLabel(self.app, text="v1.0.0", font=('Arial', 13), fg_color='black').place(relx=0.96, rely=0.95, anchor="center")

        CTk.CTkButton(self.app, text="PLAY", fg_color='blue', corner_radius=10, font=('', 25, 'bold'), hover_color='#1f2eff', command=self.play).place(relx=0.4, rely=0.4, relwidth=0.4, relheight=0.25, anchor='center')

        CTk.CTkButton(self.app, text="QUIT", fg_color='blue', corner_radius=10, font=('', 25, 'bold'), hover_color='#1f2eff', command=self.quit_game).place(relx=0.4, rely=0.75, relwidth=0.4, relheight=0.25, anchor='center')
        

    def start(self):
        self.app.mainloop()
        return self.accept_play

    def play(self):
        self.accept_play = True
        self.app.destroy()

    def quit_game(self):
        sys.exit()
