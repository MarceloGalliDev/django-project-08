from kivy.app import App
from kivy.lang import Builder


gui = Builder.load_file('home.kv')


class MeuApp(App):
    def build(self):
        return GUI


if __name__ == '__main__':
    MeuApp.run()



# importar App, Builder
# criar o app
# criar a função build
# toda função no kivy é criado dentro de classes