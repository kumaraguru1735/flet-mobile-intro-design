import flet as ft


import splashscreen



def main(page: ft.Page):
    page.clean()
    page.window_width = 370
    page.window_height = 800
    page.window_resizable =False
    page.window_frameless = False
    page.padding = 0
    page.spaceing= 0
    splashscreen.main(page)



ft.app(target=main, assets_dir="assests")