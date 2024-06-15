# primeiramente instalar a biblioteca "flet" com o comando (pip install flet)
# depois, importar o flet com o comando abaixo
import flet as ft

def main(page: ft.Page):
    # Configurações iniciais da página
    page.title = "Calculadora"
    page.bgcolor = '#000'
    page.window_resizable = False
    page.window_always_on_top = True

    # Tentar definir o tamanho da janela em uma chamada separada
    page.window_width = 250
    page.window_height = 300

    # Adiciona conteúdo à página 
    page.add(ft.Text("Hello, World!"))

ft.app(target=main)