from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
from kivy.properties import ObjectProperty
from kivy.config import Config
from kivymd.app import MDApp
from kivy.uix.image import Image

import threading
import socket
import time

Config.set('kivy', 'keyboard_mode', 'systemanddock')
Window.size = (480, 853)

def server_conn(ip, port):
    try:
        sock = socket.socket()
        sock.connect(('82.209.208.36', 4500))
        secret_id = 'user'
        sock.send(secret_id.encode())
        print("Шаг выполнен!")
        return True, sock
    except:
        passf

check = True

def data_true(sock, self):
    while (True):
        try:
            data = sock.recv(4096)
            data = data.decode('utf-8')
            data_camera = eval(data)

            if (1 != data_camera[0]):
                # self.text1.text = '№1 ' + 'Free'
                self.img1.source = 'parking_place.jpg'
            else:
                self.img1.source = 'block_car.png'
            if (1 != data_camera[1]):
                self.img2.source = 'parking_place.jpg'
            else:
                self.img2.source = 'block_car.png'
            if (1 != data_camera[2]):
                self.img3.source = 'parking_place.jpg'
            else:
                self.img3.source = 'block_car.png'
            if (1 != data_camera[3]):
                self.img4.source = 'parking_place.jpg'
            else:
                self.img4.source = 'block_car.png'
            if (1 != data_camera[4]):
                self.img5.source = 'parking_place.jpg'
            else:
                self.img5.source = 'block_car.png'
            if (1 != data_camera[5]):
                self.img6.source = 'parking_place.jpg'
            else:
                self.img6.source = 'block_car.png'
            if (1 != data_camera[6]):
                self.img7.source = 'parking_place.jpg'
            else:
                self.img7.source = 'block_car.png'
            if (1 != data_camera[7]):
                self.img8.source = 'parking_place.jpg'
            else:
                self.img8.source = 'block_car.png'

            print("1")
            time.sleep(0.5)
        except:
            break

sock = ''

class Container(GridLayout):
    def connect(self):
        global check
        global sock
        try:
            if (check == True):

                print("3")
                # ip = self.ip.text
                # port = int(self.port.text)
                true, sock = server_conn('82.209.208.36', 4500)
                network_thread = threading.Thread(target=data_true, name='Network', args=(sock, self))
                print("4")
                if (true == True):
                    network_thread.start()
                    self.label1.text = 'Подключение к серверу прошло успешно.'
                    self.img1.source = 'parking_place.png'
                    # self.img1 = Image(source = 'green_car.png', size_hint_y = None, height=50, size_hint_x = None, width=200)
                    self.img2.source = 'parking_place.png'
                    self.img3.source = 'parking_place.png'
                    self.img4.source = 'parking_place.png'
                    self.img5.source = 'parking_place.png'
                    self.img6.source = 'parking_place.png'
                    self.img7.source = 'parking_place.png'
                    self.img8.source = 'parking_place.png'
                    self.button1.text = 'Отключиться'
                    check = False
                    print("5")

            elif (check == False):
                print("8")
                check = True
                self.label1.text = 'Отключение от сервера выполнено.'
                self.button1.text = 'Подключиться'
                # self.text1.text = 'None'
                self.img1.source = 'disconnect.jpg'
                self.img2.source = 'disconnect.jpg'
                self.img3.source = 'disconnect.jpg'
                self.img4.source = 'disconnect.jpg'
                self.img5.source = 'disconnect.jpg'
                self.img6.source = 'disconnect.jpg'
                self.img7.source = 'disconnect.jpg'
                self.img8.source = 'disconnect.jpg'
                print("7")
                sock.close()

        except:
            self.label1.text = 'Не удалось соедениться с сервером :('
            # sock.close()

            print("6")


class MyApp(MDApp):

    def build(self):
        self.theme_cls.theme_style = 'Dark'
        return Container()


if __name__ == '__main__':
    MyApp().run()