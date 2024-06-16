# primeiramente instalar a biblioteca "flet" com o comando (pip install flet)
# depois, importar o flet com o comando abaixo
import flet as ft
from flet import colors
#lista com os parametos que cada botão vai ter 
botoes = [
    {'operador': 'AC','fonte': colors.BLACK, 'fundo': colors.BLUE_GREY_100},
    {'operador': '+-','fonte': colors.BLACK, 'fundo': colors.BLUE_GREY_100},
    {'operador': '%','fonte': colors.BLACK, 'fundo': colors.BLUE_GREY_100},
    {'operador': '/','fonte': colors.WHITE, 'fundo': colors.BLUE_300},
    {'operador': '7','fonte': colors.WHITE, 'fundo': colors.WHITE24},
    {'operador': '8','fonte': colors.WHITE, 'fundo': colors.WHITE24},
    {'operador': '9','fonte': colors.WHITE, 'fundo': colors.WHITE24},
    {'operador': '*','fonte': colors.WHITE, 'fundo': colors.BLUE_300},
    {'operador': '4','fonte': colors.WHITE, 'fundo': colors.WHITE24},
    {'operador': '5','fonte': colors.WHITE, 'fundo': colors.WHITE24},
    {'operador': '6','fonte': colors.WHITE, 'fundo': colors.WHITE24},
    {'operador': '-','fonte': colors.WHITE, 'fundo': colors.BLUE_300},
    {'operador': '1','fonte': colors.WHITE, 'fundo': colors.WHITE24},
    {'operador': '2','fonte': colors.WHITE, 'fundo': colors.WHITE24},
    {'operador': '3','fonte': colors.WHITE, 'fundo': colors.WHITE24},
    {'operador': '+','fonte': colors.WHITE, 'fundo': colors.BLUE_300},
#criei um botão falso para resolver o problema do alinhamento 
    {'operador': 'none','fonte': colors.BLACK, 'fundo': colors.BLACK},
    {'operador': '0','fonte': colors.WHITE, 'fundo': colors.WHITE24},
    {'operador': '.','fonte': colors.WHITE, 'fundo': colors.WHITE24},
    {'operador': '=','fonte': colors.WHITE, 'fundo': colors.BLUE_300},
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
    #coloquei uma função select para colocar um evento nos botões ao passar o mouse
    def select(e):
        value_at = result.value if result.value != '0' else ''
        value = e.control.content.value
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
        on_click=select
    )  for btn in botoes]
# troquei o ft.Row pelo Ft.GridView para ajustar o posicionamento dos botões
    keyboard = ft.GridView(
        expand=1,
        runs_count=4,
        max_extent=60,
        child_aspect_ratio=1.0,
        spacing=5,
        run_spacing=5,
        controls=btn,
        
    )

    page.add(display, keyboard)

    
    




ft.app(target=main)