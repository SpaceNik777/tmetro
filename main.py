# import json
#
# from kivy.app import App
# from kivy.uix.label import Label
# from kivy.uix.button import Button
# from kivy.uix.textinput import TextInput
# from kivy.uix.boxlayout import BoxLayout
# from kivy.uix.popup import Popup
# from kivy.uix.image import Image
# from kivy.uix.relativelayout import RelativeLayout
#
# class MyApp(App):
#     def build(self):
#         with open('stations.json', 'r', encoding='utf-8') as myfile:
#             self.stations_json = json.loads(myfile.read())
#
#         layout = BoxLayout(orientation='vertical')
#
#         lbl = Label(text='Ну-ка, быстро накидай станцию туда-сюда')
#         layout.add_widget(lbl)
#
#         txt = TextInput()
#         layout.add_widget(txt)
#
#         btn = Button(text='Нажмешь, я тебя отшлепаю')
#         btn.bind(on_press=self.to_info_window)
#         layout.add_widget(btn)
#
#         self.icon = '-subway_89937.ico'
#
#         self.window_size = (800, 500)
#
#         return layout
#
#     def to_info_window(self, txt):
#         inpStation = txt.parent.children[1].text
#         if inpStation == '':
#             error_popup = Popup(title='Ошибка', content=Label(text='Введите название станции!'),
#                                  size_hint=(None, None), size=(1000, 800))
#             error_popup.open()
#         else:
#             info_popup = Popup(title='Информация о станции ' + inpStation, size_hint=(1, 1))
#             outText = ''
#             counter = 0
#             for text in self.stations_json['MetroStations']:
#                 if text['NameOfStation'] == inpStation:
#                     outText += 'Наименование: ' + text['Name'] + '\n' + 'Режим работы по четным дням: ' + text[
#                         'ModeOnEvenDays'] + '\n' + 'Режим работы по нечетным дням: ' + text[
#                                    'ModeOnOddDays'] + '\n' + 'Статус работы станции: ' + text['ObjectStatus'] + '\n' + '----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------' + '\n'
#                     counter += 1
#             if counter == 0:
#                 info_popup.content = Label(text='Введенной станции не существует или был произведен не корректный ввод')
#             else:
#                 info_popup.content = Label(text=outText)
#             info_popup.open()
#
#     def on_start(self):
#         self.root_window.size = self.window_size
#
# if __name__ == '__main__':
#     MyApp().run()


import json

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.image import Image
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.floatlayout import FloatLayout
from cryptography.fernet import Fernet
# from Crypto.Cipher import AES
import PyInstaller

import kivy_deps.glew


class MyApp(App):

    def build(self):
        with open('stations.json', 'r', encoding='utf-8') as myfile:
            self.stations_json = json.loads(myfile.read())

        layout = FloatLayout()

        background_image = Image(source='test.png', allow_stretch=True, keep_ratio=False)
        layout.add_widget(background_image)

        lbl = Label(text='Ну-ка, быстро накидай станцию туда-сюда', size_hint=(.6, .4), pos=(403, 500))
        layout.add_widget(lbl)

        txt = TextInput(size_hint=(.2, .05), pos=(790, 600))
        layout.add_widget(txt)

        btn = Button(text='Нажмешь, я тебя отшлепаю', size_hint=(.2, .05), pos=(790, 500))
        btn.bind(on_press=self.to_info_window)
        layout.add_widget(btn)

        self.icon = '-subway_89937.ico'

        self.window_size = (800, 500)

        return layout

    def to_info_window(self, txt):

        inpStation = txt.parent.children[1].text

        if inpStation == '':
            error_popup = Popup(title='Ошибка', content=Label(text='Введите название станции!'),
                                size_hint=(None, None), size=(1000, 800))
            error_popup.open()

        else:
            info_popup = Popup(title='Информация о станции ' + inpStation, size_hint=(1, 1))
            outText = ''
            counter = 0

            for text in self.stations_json['MetroStations']:
                if text['NameOfStation'] == inpStation:
                    outText += 'Наименование: ' + text['Name'] + '\n' + 'Режим работы по четным дням: ' + text[
                        'ModeOnEvenDays'] + '\n' + 'Режим работы по нечетным дням: ' + text[
                                   'ModeOnOddDays'] + '\n' + 'Статус работы станции: ' + text[
                                   'ObjectStatus'] + '\n' + '----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------' + '\n'
                    counter += 1

            if counter == 0:
                info_popup.content = Label(text='Введенной станции не существует или был произведен не корректный ввод')
            else:
                info_popup.content = Label(text=outText)
            info_popup.open()

    def on_start(self):
        self.root_window.size = self.window_size


if __name__ == '__main__':
    MyApp().run()
