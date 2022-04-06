from kivy.app import App
from kivy.core.window import Window
from kivy.uix.widget import Widget


Window.size = (960,540)


class MainInterface(Widget):
    btn_lst = [None]*10
    player_switch = False
    # 1 will represents our player1 and 0 will represent our player2

    def tracking(self, btn_info):
        if not self.player_switch:
            self.btn_lst[int(btn_info.name)] = 1
        elif self.player_switch:
            self.btn_lst[int(btn_info.name)] = 0
        self.player_switch = not self.player_switch
        print(*self.btn_lst)
        # winning conditions
        # Row wise conditions
        if self.btn_lst[1] == self.btn_lst[2] == self.btn_lst[3] == 1 or \
            self.btn_lst[1]==self.btn_lst[2] == self.btn_lst[3]==0:
                print("You have won by row wise")
        if self.btn_lst[4] == self.btn_lst[5] == self.btn_lst[6] == 1 or \
            self.btn_lst[4]==self.btn_lst[5] == self.btn_lst[6]==0:
                print("You have won by row wise")
        if self.btn_lst[7] == self.btn_lst[8] == self.btn_lst[9] == 1 or \
            self.btn_lst[7]==self.btn_lst[8] == self.btn_lst[9]==0:
                print("You have won by row wise")

        # Column wise conditions
        if self.btn_lst[1] == self.btn_lst[4] == self.btn_lst[7] == 1 or \
            self.btn_lst[1] == self.btn_lst[4] == self.btn_lst[7] == 0:
                print("You have won by column wise")
        if self.btn_lst[2] == self.btn_lst[5] == self.btn_lst[8] == 1 or \
            self.btn_lst[2] == self.btn_lst[5] == self.btn_lst[8] == 0:
                print("You have won by column wise")
        if self.btn_lst[3] == self.btn_lst[6] == self.btn_lst[9] == 1 or \
            self.btn_lst[3] == self.btn_lst[6] == self.btn_lst[9] == 0:
                print("You have won by column wise")

        # Cross wise conditions
        if self.btn_lst[1] == self.btn_lst[5] == self.btn_lst[9] == 1 or \
            self.btn_lst[1] == self.btn_lst[5] == self.btn_lst[9] == 0:
                print("You have won by cross wise")
        if self.btn_lst[3] == self.btn_lst[5] == self.btn_lst[7] == 1 or \
            self.btn_lst[3] == self.btn_lst[5] == self.btn_lst[7] == 0:
                print("You have won by cross wise")


class TicTacToeApp(App):
    pass


TicTacToeApp().run()
