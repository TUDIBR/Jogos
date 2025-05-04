from customtkinter import *
from PIL import Image
from pygame import mixer
from random import randint, uniform
import sys, os, subprocess

app = CTk()
mixer.init()

posx = 0.5 # Define a posição x do jogador

class main():


    # TODO Carrega todas funções iniciais
    def __init__(self):
        self.variables()
        self.configuration()
        self.load_ball()
        self.player()
        self.move_detect()
        self.obj()
        self.random_direction()
        self.move_ball()
        self.ball_collider_with_player()
        self.ball_collider_with_wall()
        self.ball_collision_with_block()
        self.background_music()
        self.win()
        self.lose()
        
        self.app.mainloop()


    # TODO Cria o jogador
    def player(self):
        self.personagem = CTkLabel(self.app, fg_color='black', text='')
        self.personagem.place(relx=self.posx, rely=0.85, relwidth=0.12, relheight=0.06, anchor='center')


    # TODO Detecta as teclas do jogador
    def move_detect(self):
            self.app.bind("<Left>", lambda key: self.move('left'))
            self.app.bind("<Right>", lambda key: self.move('right'))


    # TODO Movimenta o jogador
    def move(self, key):
        if key == 'left':
            if self.posx >= 0.05:
                self.posx -= 0.015
                self.personagem.place(relx=self.posx, rely=0.85, relwidth=0.12, relheight=0.06, anchor='center')
        
        elif key == 'right':
            if self.posx <= 0.95:
                self.posx += 0.015
                self.personagem.place(relx=self.posx, rely=0.85, relwidth=0.12, relheight=0.06, anchor='center')


    # TODO Carrega os alvos
    def obj(self):
        
        # Cria as instâncias dos blocos

        # Primeira fileira de blocos (Cima para baixo)
        self.obj1_1 = CTkLabel(app, fg_color='black', text='')
        self.obj1_1.place(relx=0.1, rely=0.1, relwidth=0.18, relheight=0.09, anchor='center')

        self.obj2_1 = CTkLabel(app, fg_color='black', text='')
        self.obj2_1.place(relx=0.3, rely=0.1, relwidth=0.18, relheight=0.09, anchor='center')

        self.obj3_1 = CTkLabel(app, fg_color='black', text='')
        self.obj3_1.place(relx=0.5, rely=0.1, relwidth=0.18, relheight=0.09, anchor='center')

        self.obj4_1 = CTkLabel(app, fg_color='black', text='')
        self.obj4_1.place(relx=0.7, rely=0.1, relwidth=0.18, relheight=0.09, anchor='center')

        self.obj5_1 = CTkLabel(app, fg_color='black', text='')
        self.obj5_1.place(relx=0.9, rely=0.1, relwidth=0.18, relheight=0.09, anchor='center')

        # Segunda fileira de blocos
        self.obj1_2 = CTkLabel(app, fg_color='black', text='')
        self.obj1_2.place(relx=0.1, rely=0.25, relwidth=0.18, relheight=0.09, anchor='center')

        self.obj2_2 = CTkLabel(app, fg_color='black', text='')
        self.obj2_2.place(relx=0.3, rely=0.25, relwidth=0.18, relheight=0.09, anchor='center')

        self.obj3_2 = CTkLabel(app, fg_color='black', text='')
        self.obj3_2.place(relx=0.5, rely=0.25, relwidth=0.18, relheight=0.09, anchor='center')

        self.obj4_2 = CTkLabel(app, fg_color='black', text='')
        self.obj4_2.place(relx=0.7, rely=0.25, relwidth=0.18, relheight=0.09, anchor='center')

        self.obj5_2 = CTkLabel(app, fg_color='black', text='')
        self.obj5_2.place(relx=0.9, rely=0.25, relwidth=0.18, relheight=0.09, anchor='center')

        # Terceira fileira de blocos
        self.obj1_3 = CTkLabel(app, fg_color='black', text='')
        self.obj1_3.place(relx=0.1, rely=0.4, relwidth=0.18, relheight=0.09, anchor='center')

        self.obj2_3 = CTkLabel(app, fg_color='black', text='')
        self.obj2_3.place(relx=0.3, rely=0.4, relwidth=0.18, relheight=0.09, anchor='center')

        self.obj3_3 = CTkLabel(app, fg_color='black', text='')
        self.obj3_3.place(relx=0.5, rely=0.4, relwidth=0.18, relheight=0.09, anchor='center')

        self.obj4_3 = CTkLabel(app, fg_color='black', text='')
        self.obj4_3.place(relx=0.7, rely=0.4, relwidth=0.18, relheight=0.09, anchor='center')

        self.obj5_3 = CTkLabel(app, fg_color='black', text='')
        self.obj5_3.place(relx=0.9, rely=0.4, relwidth=0.18, relheight=0.09, anchor='center')

        # Quarta fileira de blocos
        self.obj1_4 = CTkLabel(app, fg_color='black', text='')
        self.obj1_4.place(relx=0.1, rely=0.55, relwidth=0.18, relheight=0.09, anchor='center')

        self.obj2_4 = CTkLabel(app, fg_color='black', text='')
        self.obj2_4.place(relx=0.3, rely=0.55, relwidth=0.18, relheight=0.09, anchor='center')

        self.obj3_4 = CTkLabel(app, fg_color='black', text='')
        self.obj3_4.place(relx=0.5, rely=0.55, relwidth=0.18, relheight=0.09, anchor='center')

        self.obj4_4 = CTkLabel(app, fg_color='black', text='')
        self.obj4_4.place(relx=0.7, rely=0.55, relwidth=0.18, relheight=0.09, anchor='center')

        self.obj5_4 = CTkLabel(app, fg_color='black', text='')
        self.obj5_4.place(relx=0.9, rely=0.55, relwidth=0.18, relheight=0.09, anchor='center')


        # Armazena a instância do bloco e suas coordenadas (Direita, Esquerda, Cima, Baixo)
        self.blocks = [
            [self.obj1_1, (0.1 + 0.09, 0.1 - 0.09, 0.1 + 0.045, 0.1 - 0.045)],
            [self.obj2_1, (0.3 + 0.09, 0.3 - 0.09, 0.1 + 0.045, 0.1 - 0.045)],
            [self.obj3_1, (0.5 + 0.09, 0.5 - 0.09, 0.1 + 0.045, 0.1 - 0.045)],
            [self.obj4_1, (0.7 + 0.09, 0.7 - 0.09, 0.1 + 0.045, 0.1 - 0.045)],
            [self.obj5_1, (0.9 + 0.09, 0.9 - 0.09, 0.1 + 0.045, 0.1 - 0.045)],

            [self.obj1_2, (0.1 + 0.09, 0.1 - 0.09, 0.25 + 0.045, 0.25 - 0.045)],
            [self.obj2_2, (0.3 + 0.09, 0.3 - 0.09, 0.25 + 0.045, 0.25 - 0.045)],
            [self.obj3_2, (0.5 + 0.09, 0.5 - 0.09, 0.25 + 0.045, 0.25 - 0.045)],
            [self.obj4_2, (0.7 + 0.09, 0.7 - 0.09, 0.25 + 0.045, 0.25 - 0.045)],
            [self.obj5_2, (0.9 + 0.09, 0.9 - 0.09, 0.25 + 0.045, 0.25 - 0.045)],

            [self.obj1_3, (0.1 + 0.09, 0.1 - 0.09, 0.4 + 0.045, 0.4 - 0.045)],
            [self.obj2_3, (0.3 + 0.09, 0.3 - 0.09, 0.4 + 0.045, 0.4 - 0.045)],
            [self.obj3_3, (0.5 + 0.09, 0.5 - 0.09, 0.4 + 0.045, 0.4 - 0.045)],
            [self.obj4_3, (0.7 + 0.09, 0.7 - 0.09, 0.4 + 0.045, 0.4 - 0.045)],
            [self.obj5_3, (0.9 + 0.09, 0.9 - 0.09, 0.4 + 0.045, 0.4 - 0.045)],

            [self.obj1_4, (0.1 + 0.09, 0.1 - 0.09, 0.55 + 0.045, 0.55 - 0.045)],
            [self.obj2_4, (0.3 + 0.09, 0.3 - 0.09, 0.55 + 0.045, 0.55 - 0.045)],
            [self.obj3_4, (0.5 + 0.09, 0.5 - 0.09, 0.55 + 0.045, 0.55 - 0.045)],
            [self.obj4_4, (0.7 + 0.09, 0.7 - 0.09, 0.55 + 0.045, 0.55 - 0.045)],
            [self.obj5_4, (0.9 + 0.09, 0.9 - 0.09, 0.55 + 0.045, 0.55 - 0.045)],
        ]


    # TODO Carrega a bola
    def load_ball(self):
        self.canvas = CTkCanvas(app, width=25, height=25, bg='#EBEBEB', highlightthickness=0)
        self.ball = self.canvas.create_oval(190, 190, 210, 210, fill='#00FF7F', outline='black')
        self.canvas.move(self.ball, -187, -187.5)
        self.posx_ball = 0.5
        self.posy_ball = 0.65
        self.canvas.place(relx=self.posx_ball, rely=self.posy_ball, anchor='center')


    # TODO Escolhe uma direção aleatória pra bola começar
    def random_direction(self):
        if randint(0, 1) == 0:
            # Diagonal Direita
            self.dirx = uniform(0.01, 0.01)
            self.diry = abs(self.dirx)
        else:
            # Diagonal Esquerda
            self.dirx = uniform(-0.01, -0.01)
            self.diry = abs(self.dirx)


    # TODO Cria o movimento constante da bola
    def move_ball(self):
        self.posx_ball += self.dirx
        self.posy_ball += self.diry
        self.canvas.place(relx=self.posx_ball, rely=self.posy_ball)
        
        if self.pause == False:
            self.app.after(90, lambda: self.move_ball())


    # TODO Bola colide com o jogador
    def ball_collider_with_player(self):
        largura_player = 0.12
        self.collider_esq = self.posx - largura_player / 2
        self.collider_dir = self.posx + largura_player / 2
        if self.posy_ball >= 0.8 and self.posy_ball <= 0.82 and self.cooldown == True:
            if self.posx_ball >= self.collider_esq and self.posx_ball <= self.collider_dir:
                self.cooldown = False
                dif = self.posx_ball - self.posx
                normalized = dif / (0.12 / 2)
                self.dirx = normalized / 100
                self.diry = -self.diry
                self.tuc_sound.play()
                self.app.after(1000, lambda: self.ball_cooldown_collider())

        if self.pause == False:
            self.app.after(5, lambda: self.ball_collider_with_player())


    # TODO Bola colide com a parede
    def ball_collider_with_wall(self):
        if self.pause == False:
            if self.posx_ball >= 0.95 or self.posx_ball <= 0.05:
                self.dirx = -self.dirx
                self.tuc_sound.play()
            if self.posy_ball <= 0.05:
                self.diry = -self.diry
                self.tuc_sound.play()
            
            
            if self.posx_ball >= 0.955:
                self.posx_ball -= 0.08

            elif self.posx_ball <= 0.045:
                self.posx_ball += 0.08

            if self.posy_ball <= 0.05:
                self.posy_ball += 0.08

        if self.pause == False:
            self.app.after(1, lambda: self.ball_collider_with_wall())

    
    # TODO Cooldown da bola (Evita a bola grudar no jogador ou na parede)
    def ball_cooldown_collider(self):
        self.cooldown = True


    # TODO Verifica se a bola colidiu com algum bloco e rebate
    def ball_collision_with_block(self):
        for block in self.blocks:
            min_x = min(block[1][0], block[1][1])
            max_x = max(block[1][0], block[1][1])
            min_y = min(block[1][2], block[1][3])
            max_y = max(block[1][2], block[1][3])
            if self.posy_ball >= min_y and self.posy_ball <= max_y:
                if self.posx_ball <= max_x and self.posx_ball >= min_x:
                    dif = min_x + 0.09 - self.posx
                    normalized = dif / (0.18 / 2)
                    self.dirx = normalized / 100
                    self.diry = -self.diry
                    mixer.Sound(r"C:\Users\tudib\Área de Trabalho\Programação\Scripts python\Meus jogos\Socker\assets\SFX\ball_collision_sfx.wav").play()
                    block[0].place(relx=999)
                    self.blocks.remove(block)

        if self.pause == False:
            self.app.after(1, lambda: self.ball_collision_with_block())


    # TODO Verifica se o jogador ganhou
    def win(self):
        if len(self.blocks) == 0:
            CTkLabel(app, text='VITÓRIA, APERTE "R" PARA REINICIAR', text_color='green', font=('verdana', 15, 'bold'), bg_color='black').place(relx=0.5, rely=0.5, relwidth=0.5, relheight=0.3, anchor='center')
            self.pause = True
            self.app.unbind("<Left>")
            self.app.unbind("<Right>")
            self.focus()
            self.app.bind("<KeyPress-r>", lambda a: self.restart())
        if self.pause == False:
            self.app.after(5, lambda: self.win())


    # TODO Verifica se o jogador perdeu
    def lose(self):
        if self.posy_ball >= 1:
            self.dirx = 0
            self.diry = 0
            self.posy_ball = -999
            CTkLabel(app, text='DERROTA, APERTE "R" PARA REINICIAR', text_color='red', font=('verdana', 15, 'bold'), bg_color='black').place(relx=0.5, rely=0.5, relwidth=0.5, relheight=0.3, anchor='center')
            self.pause = True
            self.app.unbind("<Left>")
            self.app.unbind("<Right>")
            self.focus()
            self.app.bind("<KeyPress-r>", lambda a: self.restart())
        if self.pause == False:
            self.app.after(5, lambda: self.lose())


    # TODO Reinicia o jogo
    @staticmethod
    def restart():
        subprocess.Popen([sys.executable] + sys.argv)
        os._exit(0)


    # TODO Música de fundo
    def background_music(self):
        self.music.play()
        self.app.after(28000, lambda: self.background_music())


    # TODO Váriaveis
    def variables(self):
        self.app = app
        self.posx = posx
        self.cooldown = True
        self.pause = False

        self.tuc_sound = mixer.Sound(r"C:\Users\tudib\Área de Trabalho\Programação\Scripts python\Meus jogos\Socker\assets\SFX\ball_collision_sfx.wav")
        self.music = mixer.Sound(r"C:\Users\tudib\Área de Trabalho\Programação\Scripts python\Meus jogos\Socker\assets\Music\bg_music.mp3")


    # TODO Foca a janela
    def focus(self):
        self.app.focus_force()
        self.app.lift()
        self.app.attributes('-topmost', True)
        self.app.after(100, lambda: self.app.attributes('-topmost', False))



    # TODO Configurações da aplicação
    def configuration(self):
        self.app._set_appearance_mode('Light')
        self.app.geometry("800x500")
        self.app.resizable(False, False)
        self.app.title("Socker")

if __name__ == '__main__':
    main()

