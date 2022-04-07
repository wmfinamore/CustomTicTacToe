from kivy.app import App
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.widget import Widget

Window.size = (960, 540)


class MainInterface(Widget):
    btn_lst = [None] * 10
    player_switch = False
    won = False

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.btn = Button(text="", size=(500, 200), pos=(480-250, 270-100),
                          background_normal="Winner.png", background_down="Winner.png")
        self.btn.bind(on_press=self.restarting)

    def restarting(self, event):
        print("You have restarted")
        self.remove_widget(self.btn)
        self.btn_lst = [None] * 10
        self.player_switch = False
        self.won = False
        for i, j in self.ids.items():

            if i == "PLAYER_IMG":
                pass
            else:
                print(i)
                j.source = "Button.png"
                self.ids.player_img.source = "Player_1.png"

    # 1 will represents our player1 and 0 will represent our player2

    def tracking(self, btn_info, img):
        if not self.won:
            if self.btn_lst[int(btn_info.name)] != 1 and self.btn_lst[int(btn_info.name)] != 0:
                if not self.player_switch:
                    self.btn_lst[int(btn_info.name)] = 1
                    img.source = "Pressed_O.png"
                    self.ids.player_img.source = "Player_2.png"
                elif self.player_switch:
                    self.btn_lst[int(btn_info.name)] = 0
                    img.source = "Pressed_T.png"
                    self.ids.player_img.source = "Player_1.png"
                self.player_switch = not self.player_switch
                print(*self.btn_lst)
            # winning conditions
            # Row wise conditions
            if self.btn_lst[1] == self.btn_lst[2] == self.btn_lst[3] == 1 or \
                    self.btn_lst[1] == self.btn_lst[2] == self.btn_lst[3] == 0:
                print("You have won by row wise")
                self.won = True
                self.add_widget(self.btn)
            if self.btn_lst[4] == self.btn_lst[5] == self.btn_lst[6] == 1 or \
                    self.btn_lst[4] == self.btn_lst[5] == self.btn_lst[6] == 0:
                print("You have won by row wise")
                self.won = True
                self.add_widget(self.btn)
            if self.btn_lst[7] == self.btn_lst[8] == self.btn_lst[9] == 1 or \
                    self.btn_lst[7] == self.btn_lst[8] == self.btn_lst[9] == 0:
                print("You have won by row wise")
                self.won = True
                self.add_widget(self.btn)

            # Column wise conditions
            if self.btn_lst[1] == self.btn_lst[4] == self.btn_lst[7] == 1 or \
                    self.btn_lst[1] == self.btn_lst[4] == self.btn_lst[7] == 0:
                print("You have won by column wise")
                self.won = True
                self.add_widget(self.btn)
            if self.btn_lst[2] == self.btn_lst[5] == self.btn_lst[8] == 1 or \
                    self.btn_lst[2] == self.btn_lst[5] == self.btn_lst[8] == 0:
                print("You have won by column wise")
                self.won = True
                self.add_widget(self.btn)
            if self.btn_lst[3] == self.btn_lst[6] == self.btn_lst[9] == 1 or \
                    self.btn_lst[3] == self.btn_lst[6] == self.btn_lst[9] == 0:
                print("You have won by column wise")
                self.won = True
                self.add_widget(self.btn)

            # Cross wise conditions
            if self.btn_lst[1] == self.btn_lst[5] == self.btn_lst[9] == 1 or \
                    self.btn_lst[1] == self.btn_lst[5] == self.btn_lst[9] == 0:
                print("You have won by cross wise")
                self.won = True
                self.add_widget(self.btn)
            if self.btn_lst[3] == self.btn_lst[5] == self.btn_lst[7] == 1 or \
                    self.btn_lst[3] == self.btn_lst[5] == self.btn_lst[7] == 0:
                print("You have won by cross wise")
                self.won = True
                self.add_widget(self.btn)


class TicTacToeApp(App):
    pass


TicTacToeApp().run()
