import os
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
import random

from kivy.core.window import Window
import time


class GameView(BoxLayout):
    def __init__(self):
        super(GameView, self).__init__()
        self.fond = FloatLayout()
        self.image = Image(source='bg.jpg')
        self.value = random.randint(0, 100)
        self.essais = 5
        self.essais_depart = 5
        self.fond.add_widget(self.image)

    def check_number(self):
        if not self.answer_input.text.isdigit():
            if self.essais >= 1:
                self.result_label.text = "Veuillez Saisir un entier"
                self.result_label.color = "#A42813"
                self.result_label.font_size = 25
                self.result_label.font_name = "micross"
            else:
                self.result_label.text = "Dommage :("
                self.result_label.color = "#A42813"
                self.result_label.font_size = 40
                self.result_label.font_name = "micross"

        elif self.essais < 1:
            self.result_label.text = "Dommage :("
            self.result_label.color = "#A42813"
            self.result_label.font_size = 40
            self.result_label.font_name = "micross"
        elif int(self.answer_input.text) == self.value:
            self.result_label.text = "Felicitation ! \nvous l'avez trouvé en " + str(
                self.essais_depart - self.essais) + " éssais "
            self.result_label.color = "#38B15F"
            self.result_label.font_size = 30
            self.result_label.font_name = "micross"
        elif int(self.answer_input.text) > self.value:
            self.result_label.text = "Plus petit!"
            self.result_label.color = "#A45493"
            self.result_label.font_size = 40
            self.result_label.font_name = "micross"
        elif int(self.answer_input.text) < self.value:
            self.result_label.text = "Plus grand!"
            self.result_label.color = "#A45493"
            self.result_label.font_size = 40
            self.result_label.font_name = "micross"

    def check_essais(self):
        text = " éssais"
        text2 = " éssai"
        if self.answer_input.text.isdigit():
            self.essais -= 1
            if self.essais == 5:
                self.result_label2.text = "Vous avez " + str(self.essais) + text
            if self.essais <= 4:
                if self.essais > 1:
                    self.result_label2.text = "Il vous reste " + str(self.essais) + text
                elif self.essais == 1:
                    self.result_label2.text = "Il vous reste " + str(self.essais) + text2
                else:
                    self.result_label2.text = "Vous n'avez plus d'éssais"

    def try_again(self):
        self.value = random.randint(0, 100)
        self.answer_input.text = ""
        self.result_label.text = "Veuillez deviner le chiffre mystere \n situé entre 0 et 100"
        self.result_label.font_size = 20
        self.result_label.halign = "center"
        self.result_label.color = "#FFFFFF"
        self.result_label3.text = ""
        self.result_label.font_name = "micross"

    def renisialize(self):
        if self.answer_input.text == "":
            self.essais = 5
            text = " éssais"
            self.result_label2.text = "Vous avez " + str(self.essais) + text

    def check_exit(self):
        if self.essais <= 1:
            self.result_label3.text = "Le chiffre mystère était : " + str(self.value)
            self.result_label3.font_size = 25
            self.result_label3.font_name = "micross"

    def leave(self):
        exit()


class StanApp(App):
    def build(self):
        self.icon = 'logo.png'
        self.title = 'Random Number'
        return GameView()


stanApp = StanApp()
stanApp.run()
