# primeiramente instalar a biblioteca "flet" com o comando (pip install flet)
# depois, importar o flet com o comando abaixo
import flet as ft
from flet import colors
#lista com os parametos que cada botão vai ter 
botoes = [
    {'operador': 'AC','fonte': colors.BLACK, 'fundo': colors.BLUE_GREY_100},
    {'operador': '+-','fonte': colors.BLACK, 'fundo': colors.BLUE_GREY_100},
    {'operador': '%','fonte': colors.BLACK, 'fundo': colors.BLUE_GREY_100},
    {'operador': '/','fonte': colors.WHITE, 'fundo': colors.ORANGE},
    {'operador': '7','fonte': colors.WHITE, 'fundo': colors.WHITE24},
    {'operador': '8','fonte': colors.WHITE, 'fundo': colors.WHITE24},
    {'operador': '9','fonte': colors.WHITE, 'fundo': colors.WHITE24},
    {'operador': '*','fonte': colors.WHITE, 'fundo': colors.ORANGE},
    {'operador': '4','fonte': colors.WHITE, 'fundo': colors.WHITE24},
    {'operador': '5','fonte': colors.WHITE, 'fundo': colors.WHITE24},
    {'operador': '6','fonte': colors.WHITE, 'fundo': colors.WHITE24},
    {'operador': '-','fonte': colors.WHITE, 'fundo': colors.ORANGE},
    {'operador': '1','fonte': colors.WHITE, 'fundo': colors.WHITE24},
    {'operador': '2','fonte': colors.WHITE, 'fundo': colors.WHITE24},
    {'operador': '3','fonte': colors.WHITE, 'fundo': colors.WHITE24},
    {'operador': '+','fonte': colors.WHITE, 'fundo': colors.ORANGE},
    {'operador': '0','fonte': colors.WHITE, 'fundo': colors.WHITE24},
    {'operador': '.','fonte': colors.WHITE, 'fundo': colors.WHITE24},
    {'operador': '=','fonte': colors.WHITE, 'fundo': colors.ORANGE},
]

def main(page: ft.Page):
    # Configurações iniciais da página
    page.title = "Calculadora"
    page.bgcolor = '#000'
    page.window_resizable = False
    page.window_always_on_top = True

    # Tentar definir o tamanho da janela em uma chamada separada
    page.window_width = 250
    page.window_height = 380

    # Adiciona conteúdo à página 
    result =ft.Text(value='0', color= colors.WHITE, size=20)

    display = ft.Row(
        width=250,
        controls=[result],
        alignment= 'end'
    )

    btn = [ft.Container(
        content=ft.Text(value=btn['operador'], color=btn['fonte']),
        width=50,
        height=50,
        bgcolor=btn['fundo'],
        border_radius= 100,
        alignment=ft.alignment.center,
    )  for btn in botoes]

    keyboard = ft.Row(
        width=250,
        wrap=True,
        controls=btn,
        alignment='end'
    )

    page.add(display, keyboard)

    
    




ft.app(target=main)