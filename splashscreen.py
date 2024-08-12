import flet as ft
import signup
import signin


def main(page: ft.Page):
    page.clean()

    body = ft.Stack([
            ft.Image(
                src=f"assests/splashscreen2.jpeg",
                width=370,
                height=800,
                fit=ft.image.ImageFit.COVER,
                border_radius=ft.border_radius.all(0)
            ),
        
        ft.Row([
            ft.Text(
                "The best \napp for \nyour plants",
                font_family="Consolas",
                color="white",
                size=45,
                weight=ft.FontWeight.BOLD,


            ),

        ],alignment=ft.MainAxisAlignment.START,left=35,top=70),

        ft.Row([
            ft.ElevatedButton(
                text="Sign in",
                width=260,
                on_click=lambda e: signin.main(page),
                style=ft.ButtonStyle(color="white",bgcolor="white24")
            )
        ],alignment=ft.MainAxisAlignment.CENTER,left=55,top=500,),

    ft.Row([
        ft.TextButton(
            text="Create an account",
            style=ft.ButtonStyle(
                color=ft.colors.WHITE,
            ),
            on_click=lambda e: signup.main(page),
        )
    ],alignment=ft.MainAxisAlignment.CENTER,left=110,top=550,)
    ],width=400,height=800)


    page.add(body)